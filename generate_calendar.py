"""
This is the main file of the project. Basically, it takes the date (current day) from the OS. Based on that
it takes the link to the picture for that day and generates a message for it. Then it opens the file.
Please note: in Germany, Christmas is celebrated on Christmas Eve and Advent calendars only have 24 doors.
If you want a calendar with 25 "doors", you need to modify the code in the make-text function, add a new picture to the
picture repository and expand the dictionary in the pic_dic file.
"""

from PIL import Image, ImageDraw, ImageFont
from pic_dic import pic_dic
from datetime import datetime


# import current day
date = datetime.today().strftime('%d')

def make_text():

    """
Checks if the date is 24 or less (see above). If Christmas is already
over, it generates that text. Otherwise it calculates the nights till Christmas (Eve)
and generates a message for the day.
    """

    if int(date) < 25:
        nächte = 24 - int(date)
        text = f"   {date}.Dezember\n Noch {nächte} mal schlafen\n Frohe Weihnachten!"

    else:
        text = "\n\n\n\n\n\n\n\n\nWeihnachten ist schon vorbei :("

    return text
def finde_pfad():

    """
    This takes the date and uses it to find the corresponding
    picture (or rather the relative path) in the pic_dic dictionary.
    If the date doesn't have a path (because Christmas is over),
    the path to a standart picture is activated.
    """
    try:
        pfad_zu_bild = pic_dic[date]

    except: pfad_zu_bild =  "venv/xmas_pics/rest_felix_mendoza.png"

    return pfad_zu_bild

def zeige_bild(pfad,
               text,
               position=(400,100),
               textgroesse=60):

    """
    This opens the picture and adds the text.
    """

    bild = Image.open(pfad)

    zeichner = ImageDraw.Draw(bild)

    try:
        font = ImageFont.truetype("arial.ttf", textgroesse)

    except IOError:
        font = ImageFont.load_default()

    zeichner.text(position, text, font=font, fill = (000,000,000))

    bild.show()

pfad = finde_pfad()
text = make_text()
zeige_bild(pfad, text)