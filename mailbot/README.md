# Memory drop mail bot

Simple Python script that will e-mail a new photo every day.

## Packaging and uploading to AWS

    pip3 install --target ./package requests exif

    rm mailbot.zip
    cd package
    zip -r ../mailbot.zip .
    cd ..

    zip -g mailbot.zip lambda_function.py

    aws lambda update-function-code --function-name memorydropper --zip-file fileb://mailbot.zip

## Configuring function

Set these environment variables in the AWS Lambda function configuration:

    EMAIL_CRED - Gmail App Password for account used
    GALLERY_URL - Full URL to the gallery. Linked in email.
    IMG_BASE_URL - Base URL for S3 bucket and folder that contains photos and filelist.txt

## Developing locally

Uncomment `lambda_handler(None, None)` at the end of `lambda_function.py`.

Set environment variables:

    export EMAIL_CRED=xxxxxxxxx
    export GALLERY_URL=https://xxxxxxx.xxxxx.xxxx
    export IMG_BASE_URL=https://xxxxx.s3.eu-central-1.amazonaws.com/my-folder

Run it:

    python3 lambda_function.py
