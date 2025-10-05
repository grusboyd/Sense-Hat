from sense_hat import SenseHat
import time

sense = SenseHat()

# 5x5 font dictionary for basic characters
FONT_5x5 = {
    'A': ["01110","10001","11111","10001","10001"],
    'B': ["11110","10001","11110","10001","11110"],
    'C': ["01111","10000","10000","10000","01111"],
    'D': ["11110","10001","10001","10001","11110"],
    'E': ["11111","10000","11110","10000","11111"],
    'F': ["11111","10000","11110","10000","10000"],
    'G': ["01111","10000","10111","10001","01111"],
    'H': ["10001","10001","11111","10001","10001"],
    'I': ["01110","00100","00100","00100","01110"],
    'J': ["00111","00010","00010","10010","01100"],
    'K': ["10001","10010","11100","10010","10001"],
    'L': ["10000","10000","10000","10000","11111"],
    'M': ["10001","11011","10101","10001","10001"],
    'N': ["10001","11001","10101","10011","10001"],
    'O': ["01110","10001","10001","10001","01110"],
    'P': ["11110","10001","11110","10000","10000"],
    'Q': ["01110","10001","10001","10011","01111"],
    'R': ["11110","10001","11110","10010","10001"],
    'S': ["01111","10000","01110","00001","11110"],
    'T': ["11111","00100","00100","00100","00100"],
    'U': ["10001","10001","10001","10001","01110"],
    'V': ["10001","10001","10001","01010","00100"],
    'W': ["10001","10001","10101","11011","10001"],
    'X': ["10001","01010","00100","01010","10001"],
    'Y': ["10001","01010","00100","00100","00100"],
    'Z': ["11111","00010","00100","01000","11111"],
    '0': ["01110","10011","10101","11001","01110"],
    '1': ["00100","01100","00100","00100","01110"],
    '2': ["01110","10001","00010","00100","11111"],
    '3': ["11110","00001","01110","00001","11110"],
    '4': ["10010","10010","11111","00010","00010"],
    '5': ["11111","10000","11110","00001","11110"],
    '6': ["01110","10000","11110","10001","01110"],
    '7': ["11111","00010","00100","01000","01000"],
    '8': ["01110","10001","01110","10001","01110"],
    '9': ["01110","10001","01111","00001","01110"],
    'C': ["01110","10000","10000","10000","01110"],
    'H': ["10001","10001","11111","10001","10001"],
    ':': ["00000","00100","00000","00100","00000"],
    '.': ["00000","00000","00000","00100","00100"],
    '%': ["10001","00010","00100","01000","10001"],
    ' ': ["00000","00000","00000","00000","00000"],
}

def char_to_pixels(char, fg, bg):
    pattern = FONT_5x5.get(char.upper(), FONT_5x5[' '])
    pixels = []
    for row in pattern:
        for bit in row:
            pixels.append(fg if bit == '1' else bg)
    return pixels  # 25 pixels (5x5)

def scroll_message(message, fg=[255,255,0], bg=[0,0,255], speed=0.12):
    # Build the full message as a pixel array (height 5, width 5*len(message))
    msg_pixels = []
    for char in message:
        msg_pixels.append(char_to_pixels(char, fg, bg))
        # Add a single column of space for increased kerning
        msg_pixels.append([bg]*25)
    # Flatten to a single list of columns
    columns = []
    for char_pixels in msg_pixels:
        for col in range(5):
            columns.append([char_pixels[row*5 + col] for row in range(5)])
        # Add the extra space column (kerning)
        columns.append([bg]*5)
    # Scroll across the 8x8 display, centered vertically
    for offset in range(len(columns) - 7):
        frame = [[bg for _ in range(8)] for _ in range(8)]
        for x in range(8):
            for y in range(5):
                frame[y+1][x] = columns[offset + x][y]
        # Flatten for Sense HAT
        flat = [pix for row in frame for pix in row]
        sense.set_pixels(flat)
        time.sleep(speed)
    sense.clear()
    
while True:
    temp = round(sense.get_temperature(), 1)
    humidity = round(sense.get_humidity(), 1)
    pressure = round(sense.get_pressure(), 1)
    msg = f"T:{temp}C H:{humidity}% P:{pressure}"
    scroll_message(msg, fg=[255,255,0], bg=[0,0,255], speed=0.12)
    time.sleep(2)