KNOWN_WIDTH = 0.6
FOCAL_LENGTH = 700

def estimate_distance(pixel_width):

    if pixel_width == 0:
        return 0

    distance = (KNOWN_WIDTH * FOCAL_LENGTH) / pixel_width

    return round(distance,2)