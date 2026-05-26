class TrajectoryPredictor:

    def __init__(self):

        self.last_distances = {}


    def update(self, object_id, distance):

        approaching = False

        if object_id in self.last_distances:

            previous = self.last_distances[object_id]

            if distance < previous:
                approaching = True

        self.last_distances[object_id] = distance

        return approaching