from sense_hat import SenseHat
import time
import random
import sys
import termios
import tty
import select

def is_key_pressed():
    dr, _, _ = select.select([sys.stdin], [], [], 0)
    return dr

def get_key():
    return sys.stdin.read(1)

sense = SenseHat()
sense.set_rotation(0)
sense.clear()  # Reset display before runningx

try:
    while True:
        if is_key_pressed():
            key = get_key()
            if key.lower() == 'x':
                break

        pixels = [[0, 0, 0] for _ in range(64)]
        num_sparkles = random.randint(5, 12)
        sparkle_indices = random.sample(range(64), num_sparkles)
        for idx in sparkle_indices:
            r = random.randint(100, 255)
            g = random.randint(100, 255)
            b = random.randint(100, 255)
            pixels[idx] = [r, g, b]
        sense.set_pixels(pixels)
        time.sleep(0.1)
except (KeyboardInterrupt, SystemExit):
    pass
finally:
    sense.clear()  # Reset display on exit
    sys.exit(0)