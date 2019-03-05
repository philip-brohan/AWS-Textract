#!/usr/bin/env python

# Run Textract on the Second-order station sample image

import pickle
import boto3

# Load the jpeg
with open("../../../samples/Margate_1891_02.jpg",'rb') as jf:
    ie=jf.read()

# Analyze the document
client = boto3.client('textract')
response = client.detect_document_text(Document={'Bytes': ie})

# Save the resulting JSON
pickle.dump(response, open( "detection.pkl", "wb" ) )
