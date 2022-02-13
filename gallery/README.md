# Memory drop gallery

VERY simple HTML/JS gallery that will show all photos up until today.

## Packaging and uploading to AWS

    pip3 install --target ./package jinja2 requests

    rm gallery.zip
    cd package
    zip -r ../gallery.zip .
    cd ..

    zip -g gallery.zip lambda_function.py
    zip -g gallery.zip gallery-template.html

    aws lambda update-function-code --function-name memorygallery --zip-file fileb://gallery.zip

## Configuring function and API Gateway

You need to set the environment variable `IMG_BASE_URL` to the S3 bucket public URL where the photos and filelist.txt lives in AWS Lambda.

Create an API Gateway endpoint pointing to the Lambda function.

Visit the generated `Invoke URL` from API Gateway to view the gallery.
