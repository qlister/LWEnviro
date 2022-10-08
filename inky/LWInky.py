from PIL import Image,ImageDraw,ImageFont
from inky.mock import InkyMockImpression
from inky import auto
from datetime import datetime
from dateutil.tz import tzlocal

class LWdisplay:

    def __init__(self):
        self.inky = InkyMockImpression()
        #self.inky = auto()
        self.font = ImageFont.truetype('truetype/dejavu/DejaVuSans.ttf', 40, encoding="unic")

    def draw( self, data ):
        
        # these lines fix an apparent bug in Pimoroni module that doesn't return UTC string
        # there is a spurious Z at the end of the string
        ts = data["timestamp"].replace('Z','+00:00')
        dt_utc = datetime.strptime(ts, '%Y-%m-%dT%H:%M:%S%z')
        dt_local = dt_utc.astimezone(tzlocal())
        data["timestamp"] = dt_local
        
        readings = data["readings"]

        canvas = Image.new("RGB", (self.inky.width, self.inky.height), (255, 255, 255))
        draw = ImageDraw.Draw(canvas)
        unicode_text = 'Temp = %04.1f\N{DEGREE SIGN}C' % readings["temperature"]
        draw.text((5,80), unicode_text, 'black', self.font)
        #text_width, text_height = font.getsize(unicode_text)
        
        unicode_text = dt_local.strftime('%a, %d, %b %Y')
        draw.text((5,5), unicode_text, 'black', self.font)
        draw.text((450,5), dt_local.strftime( '%H:%M'), 'black', self.font )

#        image.paste(plot_image, (0, 0))
        saturation = 0
        self.inky.set_image(canvas, saturation=saturation)
        self.inky.show()
