import sys
import os
picdir = "./pic"
libdir = "./lib"
fontdir = "./fonts"

if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in5b_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd7in5b_V2 Demo")

    epd = epd7in5b_V2.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    font60 = ImageFont.truetype(os.path.join(fontdir, 'JetBrainsMono/JetBrainsMono-BoldItalic.ttf'), 60)

    logging.info("1.Drawing on the Horizontal image...")
    Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw_Himage = ImageDraw.Draw(Himage)
    draw_Himage.text((10, 10), '@Pabilo', font = font60, fill = 0)
    epd.display(epd.getbuffer(Himage))

    logging.info("Goto Sleep...")
    epd.sleep()


except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd7in5b_V2.epdconfig.module_exit(cleanup=True)
    exit()