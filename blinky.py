import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4)

while True:
    pixels[0] = ((0, 5, 0))
    time.sleep(0.5)
    pixels[1] = ((0, 5, 0))
    time.sleep(0.5)
    pixels[2] = ((0, 5, 0))
    time.sleep(0.5)
    pixels[3] = ((0, 5, 0))
    time.sleep(0.5)
    pixels.fill((5, 0 , 0))
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    time.sleep(0.5)
