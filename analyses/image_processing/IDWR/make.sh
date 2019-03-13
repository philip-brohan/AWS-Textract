#!/usr/bin/bash

# Tweak the contrast on the IDWR sample to get 
#   much better Textract results.

../scripts/modify.py --source=../../../samples/idwr1893-v1_0021.jpg \
                     --colour=1.0 \
                     --sharpness=0.0 \
                     --brightness=1.0 \
                     --contrast=0.4
../scripts/run_textract.py
../scripts/oplot_text.py
