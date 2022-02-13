# Memory Drop

A tool that will e-mail your mom a photo every day and show a gallery of the previous days photos.

## Quick start

- Put the photos in the `photos/` folder. Use naming convention `0004-2000-05-14.jpg`. A sequence number followed by the date. Lightroom can do this for you. The most important thing is that the names allow for sorting that does not change when adding more photos later.
- Create a `filelist.txt` file: `ls photos/ > photos/filelist.txt`.
- Create a AWS S3 bucket with public permissions. Upload the `photos/` folder to it. Verify you can view images in the browser without authentication.

- Install and configure AWS CLI

### Mailbot

- Generate an App Password in Gmail (https://levelup.gitconnected.com/an-alternative-way-to-send-emails-in-python-5630a7efbe84)
- Update from and to e-mail addresses in `mailbot/lambda_function.py`.
- Update mail HTML template. Translate if necessary. Replace my name with yours ;)
- Set the `start_date` to the day when starting to send photos. The script will email photo number X in the list, where X is the days since the `start_date`.
- Install dependencies `pip3 install requests exif`.
- Check `mailbot/README.md` for info on deploying.

### Gallery

- Set the `start_date` in `gallery/lambda_function.py` to the day when starting to send photos.
- Install dependencies `pip3 install requests jinja2`.
- Check `gallery/README.md` for info on deploying.

