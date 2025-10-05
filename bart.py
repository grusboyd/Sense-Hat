from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear

# Bart Simpson head shot pixel art (8x8)
Y = [255, 255, 0]    # Yellow (face/hair)
B = [0, 0, 0]        # Black (outline/eyes)
W = [255, 255, 255]  # White (eyes)
T = [210, 180, 140]  # Tan (mouth)
O = [255, 140, 0]    # Orange (shirt)
_ = [0, 0, 255]      # Blue (background)

bart_pixels = [
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, B, Y, Y, Y, Y, B, Y,
    Y, W, B, Y, Y, B, W, Y,
    Y, Y, Y, B, B, Y, Y, Y,
    Y, T, T, T, T, T, T, Y,
    O, O, O, O, O, O, O, O,
    _, _, _, _, _, _, _, _
]

sense.set_pixels(bart_pixels)
