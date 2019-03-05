#!/usr/bin/env python

# Upload a single page image, from the local file system, to textract
# and save the resulting JSON.

import pickle
import boto3
import argparse

# Get the file name as a command-line argument
parser = argparse.ArgumentParser()
parser.add_argument("--file", help="file name",
                    type=str,required=True)
args = parser.parse_args()

# Load the jpeg
with open("../../OCR-weatherrescue/images/%s.jpg" % args.file,
                                                   'rb') as jf:
    ie=jf.read()

# Analyze the document
client = boto3.client('textract')
response = client.detect_document_text(Document={'Bytes': ie})

# Save the resulting JSON
pickle.dump(response, open( "../results.pkl/%s.pkl" % args.file, "wb" ) )
