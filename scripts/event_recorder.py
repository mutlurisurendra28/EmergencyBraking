import cv2
import time
import os


class EventRecorder:

    def __init__(self):

        self.recording = False
        self.out = None
        self.start_time = None
        self.cooldown = 0

        if not os.path.exists("videos"):
            os.makedirs("videos")


    def start_recording(self, frame):

        current_time = time.time()

        # Prevent recording too frequently
        if current_time < self.cooldown:
            return

        if not self.recording:

            filename = f"videos/event_{int(time.time())}.avi"

            height, width = frame.shape[:2]

            fourcc = cv2.VideoWriter_fourcc(*'MJPG')

            # FPS changed from 20 → 10
            self.out = cv2.VideoWriter(
                filename,
                fourcc,
                10,
                (width, height)
            )

            self.start_time = time.time()

            self.recording = True


    def update(self, frame):

        if self.recording:

            self.out.write(frame)

            if time.time() - self.start_time > 5:

                self.out.release()

                self.out = None

                self.recording = False

                # Wait 8 seconds before recording again
                self.cooldown = time.time() + 8