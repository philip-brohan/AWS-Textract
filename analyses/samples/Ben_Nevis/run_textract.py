#!/usr/bin/env python

# Run Textract on the Ben Nevis sample image

import pickle
import boto3
import json

# Load the jpeg
with open("../../../samples/1901-01.jpg",'rb') as jf:
    ie=jf.read()

# Analyze the document
client = boto3.client('textract')
response = client.detect_document_text(Document={'Bytes': ie})

# Save the resulting JSON
pickle.dump(response, open( "detection.pkl", "wb" ) )
with open('detection.txt', 'w') as file:
     file.write(json.dumps(response,indent=4))
