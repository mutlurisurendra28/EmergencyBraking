import numpy as np

class Sort:

    def __init__(self):
        self.next_id = 1

    def update(self, boxes):

        results = []

        for box in boxes:

            x1,y1,x2,y2,conf = box

            results.append([x1,y1,x2,y2,self.next_id])

            self.next_id += 1

        return np.array(results)