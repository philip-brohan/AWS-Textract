#!/usr/bin/env python

# Run Textract on the Aberdeen observatory sample image

import pickle
import boto3

# Load the jpeg
with open("../../../samples/Aberdeen_pressure_1923.jpg",'rb') as jf:
    ie=jf.read()

# Analyze the document
client = boto3.client('textract')
response = client.detect_document_text(Document={'Bytes': ie})

# Save the resulting JSON
pickle.dump(response, open( "detection.pkl", "wb" ) )
