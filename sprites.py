import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import time
import adafruit_imageload


displayio.release_displays()
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c,device_address=0x3d)

WIDTH = 128
HEIGHT = 64
BORDER = 5

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# Load the sprite sheet (bitmap)
sprite_sheet, palette = adafruit_imageload.load("/cp_sprite_sheet.bmp",
                                                bitmap=displayio.Bitmap,
                                                palette=displayio.Palette)

# Create a sprite (tilegrid)
sprite = displayio.TileGrid(sprite_sheet, pixel_shader=palette,
                            width = 1,
                            height = 1,
                            tile_width = 16,
                            tile_height = 16)

# Create a Group to hold the sprite
group = displayio.Group(scale=4)

# Add the sprite to the Group
group.append(sprite)

# Add the Group to the Display
display.show(group)

# Set sprite location
group.x = 36
group.y = 1 

# Loop through each sprite in the sprite sheet
source_index = 0
while True:
    sprite[0] = source_index % 6
    source_index += 1
    time.sleep(2)

