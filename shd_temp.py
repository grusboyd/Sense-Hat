from sense_hat import SenseHat
import time
import sys
import termios
import tty
import select

def is_key_pressed():
    dr, _, _ = select.select([sys.stdin], [], [], 0)
    return dr

def get_key():
    return sys.stdin.read(1)

def animate_rainbow_diagonal(sense, frame_delay=2):
    # Define rainbow colors
    colors = [
        [255, 0, 0],      # Red
        [255, 127, 0],    # Orange
        [255, 255, 0],    # Yellow
        [0, 255, 0],      # Green
        [0, 0, 255],      # Blue
        [75, 0, 130],     # Indigo
        [148, 0, 211],    # Violet
    ]
    # Animate diagonal rainbow bands moving from upper left to lower right
    for shift in range(-7, 8):  # Diagonal shift range
        pixels = []
        for row in range(8):
            for col in range(8):
                diag = row - col + shift
                if diag == 0:
                    color = colors[(row + col) % len(colors)]
                else:
                    color = [0, 0, 0]
                pixels.append(color)
        sense.set_pixels(pixels)
        time.sleep(frame_delay)
    full_rainbow = []
    for row in range(8):
        for col in range(8):
            full_rainbow.append(colors[(row + col) % len(colors)])
    sense.set_pixels(full_rainbow)
    time.sleep(frame_delay)

sense = SenseHat()
sense.clear()

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
tty.setcbreak(fd)

try:
    while True:
        if is_key_pressed():
            key = get_key()
            if key.lower() == 'x':
                break

        temp_c = sense.get_temperature() - 3.3  # Temperature calibration offset
        temp_f = round((temp_c * 9/5) + 32, 1)
        message = f"Temp: {temp_f}F"
        sense.show_message(message, scroll_speed=0.08, text_colour=[255, 0, 0], back_colour=[100, 100, 100])
        time.sleep(2)

        humidity = sense.get_humidity()
        humidity_value = round(humidity)
        message = f"Humidity: {humidity_value}%"
        sense.show_message(message, scroll_speed=0.08, text_colour=[0, 255, 0], back_colour=[100, 100, 100])
        time.sleep(2)

        pressure = sense.get_pressure()
        pressure_value = round(pressure)
        message = f"Pressure: {pressure_value} mbar"
        sense.show_message(message, scroll_speed=0.08, text_colour=[0, 0, 255], back_colour=[100, 100, 100])
        time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    pass
finally:
    animate_rainbow_diagonal(sense, frame_delay=2)
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    sys.exit(0)