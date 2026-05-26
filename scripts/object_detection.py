import cv2
import numpy as np
import time
import winsound

from distance_estimation import estimate_distance
from risk_prediction import predict_risk
from sort_tracker import Sort
from event_recorder import EventRecorder
from cloud_logger import log_event
from trajectory_prediction import TrajectoryPredictor


tracker = Sort()
recorder = EventRecorder()
predictor = TrajectoryPredictor()

brake_count = 0
last_time = time.time()

VEHICLE_SPEED = 5


CLASSES = ["background","aeroplane","bicycle","bird","boat",
"bottle","bus","car","cat","chair","cow","diningtable",
"dog","horse","motorbike","person","pottedplant",
"sheep","sofa","train","tvmonitor"]


net = cv2.dnn.readNetFromCaffe(
    "models/MobileNetSSD_deploy.prototxt",
    "models/MobileNetSSD_deploy.caffemodel"
)


cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:

    ret, frame = cap.read()

    if not ret:
        break


    frame = cv2.resize(frame,(800,600))

    (h,w) = frame.shape[:2]


    blob = cv2.dnn.blobFromImage(frame,0.007843,(300,300),127.5)

    net.setInput(blob)

    detections = net.forward()


    boxes = []

    emergency = False


    for i in range(detections.shape[2]):

        confidence = detections[0,0,i,2]

        if confidence > 0.6:

            idx = int(detections[0,0,i,1])

            label = CLASSES[idx]

            box = detections[0,0,i,3:7] * np.array([w,h,w,h])

            (startX,startY,endX,endY) = box.astype("int")

            boxes.append([startX,startY,endX,endY,confidence,label])


    if len(boxes) == 0:
        tracks = []
    else:
        det_boxes = np.array([b[:5] for b in boxes])
        tracks = tracker.update(det_boxes)


    for i,track in enumerate(tracks):

        x1,y1,x2,y2,track_id = map(int,track)

        label = boxes[i][5]


        pixel_width = x2 - x1

        distance = estimate_distance(pixel_width)


        if VEHICLE_SPEED > 0:
            ttc = distance / VEHICLE_SPEED
        else:
            ttc = 0


        approaching = predictor.update(track_id, distance)


        risk = predict_risk(distance,label)


        if approaching and distance < 3:
            risk = "HIGH"


        if risk == "HIGH":

            color = (0,0,255)

            emergency = True

            recorder.start_recording(frame)

            log_event(label, distance, risk)

            brake_count += 1

            winsound.Beep(1000,50)


        elif risk == "MEDIUM":

            color = (0,165,255)

        else:

            color = (0,255,0)


        cv2.rectangle(frame,(x1,y1),(x2,y2),color,2)


        direction = "APPROACHING" if approaching else "STABLE"


        text = f"{label} ID:{track_id} {distance}m TTC:{round(ttc,2)}s {direction} {risk}"

        cv2.putText(frame,text,(x1,y1-10),
        cv2.FONT_HERSHEY_SIMPLEX,0.6,color,2)


    recorder.update(frame)


    if emergency:

        overlay = frame.copy()

        cv2.rectangle(overlay,(0,0),(w,h),(0,0,255),-1)

        alpha = 0.2

        frame = cv2.addWeighted(overlay,alpha,frame,1-alpha,0)

        cv2.putText(frame,"EMERGENCY BRAKE ACTIVATED",
        (70,200),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (255,255,255),
        3)


    current_time = time.time()

    fps = 1/(current_time - last_time)

    last_time = current_time


    cv2.putText(frame,f"FPS: {int(fps)}",(10,20),
    cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,0),2)


    cv2.putText(frame,f"Braking Events: {brake_count}",(10,50),
    cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,0),2)


    cv2.imshow("AI Autonomous Emergency Braking System",frame)


    if cv2.waitKey(1) == 27:
        break


cap.release()

cv2.destroyAllWindows()