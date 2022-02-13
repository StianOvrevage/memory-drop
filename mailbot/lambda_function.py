# https://levelup.gitconnected.com/an-alternative-way-to-send-emails-in-python-5630a7efbe84

import json

import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import random
from datetime import date
import os

import requests
from exif import Image

def lambda_handler(event, context):
    print("Starting todays memory drop!")

    sender_email = "xx@gmail.com"
    receiver_email = ["xx@gmail.com", "stian-test@xx.com"]
    # receiver_email = ["stian-test@xx.com"]

    password = os.environ['EMAIL_CRED']
    image_base_url = os.environ['IMG_BASE_URL']
    gallery_url = os.environ['GALLERY_URL']

    # Alternative welcome texts. Chosen at random.
    welcomes = ["Hei mamma", "God morgen mamma", "Kjære mamma", "Heisann!"]

    # Start date (0 index) for chosing photo to send.
    start_date = date(2022, 2, 9)
    delta = date.today() - start_date

    todays_date = date.today().strftime("%A %d. %B %Y")

    try:
        file_list_url = image_base_url + '/filelist.txt'
        r = requests.get(file_list_url, allow_redirects=True)
        files = r.content.decode('ascii').split("\n")

        linenumber = 0
        for f in files:
          if delta.days == linenumber:
            print("Day " + str(linenumber) + ", file: " + f)
            todays_file = f
          linenumber += 1

    except Exception as e:
        print("Could not open file list:" + e)
        return

    try:
        r = requests.get(image_base_url + '/' + todays_file, allow_redirects=True)
        img = Image(r.content)

    except Exception as e:
        print("Could not download photo to get exit data:" + e)
        return

    msg = MIMEMultipart()
    msg["Subject"] = "Dagens minne " + todays_date
    msg["From"] = sender_email
    msg['To'] = ", ".join(receiver_email)

    html = """\
    <html>
      <body>
        <p>{}<br><br>
        Her er dagens minne (tatt {})<br>
        <img src="{}/{}" /><br>

        Håper du får en fin dag :D<br>
        <br>
        Klem fra Stian
        </p>
        <p>
        PS: Arkiv over tidligere bilder finner du ved å <a href="{}">klikke her</a>.
        </p>
      </body>
    </html>
    """

    if hasattr(img, 'datetime_original'):
      image_descr = img.datetime_original
    else:
      image_descr = todays_file

    body_html = MIMEText(html.format(random.choice(welcomes), image_descr, image_base_url, todays_file, gallery_url), 'html')
    msg.attach(body_html)

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP("smtp.gmail.com", "587")
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)

        server.sendmail(sender_email, receiver_email, msg.as_string())

    except Exception as e:
        print(e)
    finally:
        server.quit()

    print("Email hopefully sent!")

    return {
        'statusCode': 200,
        'body': json.dumps('E-mail sent')
    }

if __name__ == '__main__':
    lambda_handler(None, None)