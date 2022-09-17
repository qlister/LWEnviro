from PIL import Image,ImageDraw,ImageFont
 
# sample text and font
unicode_text = u"SMILE WORLD!" # This is used to shape the image around the text size
font = ImageFont.truetype('freefont/FreeSans.ttf', 28, encoding="unic")
font2 = ImageFont.truetype("freefont/FreeSans.ttf", 10, encoding="unic")
# get the line size
text_width, text_height = font.getsize(unicode_text)
 
# create a blank canvas with extra space between lines
# I added 100 to host the image and 30 for the watermark length
canvas = Image.new('RGB', (text_width + 30, text_height + 200), "orange")
 
# draw the text onto the text canvas, and use black as the text color
draw = ImageDraw.Draw(canvas)
draw.text((5,5), unicode_text, 'blue', font) # This paste the unicode_text=u"SMILE WORLD"
 
def smile(x=30,y=30):
    draw = ImageDraw.Draw(canvas)
    draw.ellipse((0+x,0+y,90+x,90+y),'yellow','blue') # face
    draw.ellipse((25+x,20+y,35+x,30+y),'yellow','blue') # left eye
    draw.ellipse((28+x,25+y,32+x,30+y),'blue','blue') # left ...
    draw.ellipse((50+x,20+y,60+x,30+y),'yellow','blue') # right eye
    draw.ellipse((53+x,25+y,58+x,30+y),'blue','blue') # right ...
    draw.arc((40+x,50+y,50+x,55+y), 0, 360, 0) # nose
    draw.arc((20+x,40+y,70+x,70+y), 0, 180, 0) # smile
 
smile(60,28)    
draw.text((5,100), u'This image is covered by copyright', 'blue', font2)
draw.text((5,110), u'pythonprogramming.altervista.org', 'blue', font2)
canvas.show()
canvas.save("smile.png")