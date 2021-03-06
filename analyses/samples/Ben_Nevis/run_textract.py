#!/usr/bin/env python

# Run Textract on the Argentine DWR sample image

import pickle
import boto3
import json

# Load the jpeg
with open("../../../samples/1901-01.jpg",'rb') as jf:
    ie=jf.read()

# Analyze the document
client = boto3.client('textract')
response = client.analyze_document(Document={'Bytes': ie},
                                   FeatureTypes=['TABLES'])

# Save the resulting JSON
pickle.dump(response, open( "detection.pkl", "wb" ) )
with open('detection.txt', 'w') as file:
     file.write(json.dumps(response,indent=4))
