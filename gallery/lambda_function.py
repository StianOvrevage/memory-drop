from datetime import date
from jinja2 import Environment, FileSystemLoader, select_autoescape
import requests
import os

env = Environment(
    loader=FileSystemLoader("./"),
    autoescape=select_autoescape()
)

def lambda_handler(event, context):

  image_base_url = os.environ['IMG_BASE_URL']

  # Start date (0 index) for chosing photo to show.
  start_date = date(2022, 2, 9)
  delta = date.today() - start_date

  filenames = []

  try:
      file_list_url = image_base_url + '/filelist.txt'
      r = requests.get(file_list_url, allow_redirects=True)
      files = r.content.decode('ascii').split("\n")

  except Exception as e:
      print("Could not open file list:" + e)
      return

  linenumber = 0
  for f in files:
    if linenumber <= delta.days:
      print(str(linenumber) + " - " + f)
      filenames.append(f)
    linenumber += 1

  template = env.get_template("gallery-template.html")

  return {
      "statusCode": 200,
      "body": template.render(photofilenames=filenames, baseurl=image_base_url),
      "headers": {
          'Content-Type': 'text/html',
      }
  }

if __name__ == '__main__':
    lambda_handler(None, None)