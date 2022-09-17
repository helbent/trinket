import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306


displayio.release_displays()
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c,device_address=0x3d)

WIDTH = 128
HEIGHT = 64
BORDER = 5

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# Create a bitmap with two colors
bitmap = displayio.Bitmap(display.width, display.height, 2)

# Create a two color palette
palette = displayio.Palette(2)
palette[0] = 0x000000
palette[1] = 0xffffff

# Create a TileGrid using the Bitmap and Palette
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

# Create a Group
group = displayio.Group()

# Add the TileGrid to the Group
group.append(tile_grid)

# Add the Group to the Display
display.show(group)

# Draw a pixel
bitmap[80, 50] = 1

# Draw even more pixels
for x in range(10, 40):
    for y in range(20, 40):
        bitmap[x, y] = 1

# Draw even more pixels
for x in range(80, 110):
    for y in range(20, 40):
        bitmap[x, y] = 1 


# Loop forever so you can enjoy your image
while True:
    pass

