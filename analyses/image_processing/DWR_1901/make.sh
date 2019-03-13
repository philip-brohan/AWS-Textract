#!/usr/bin/bash

# Tweak the contrast on the DWR 1901 sample to get 
#   much better Textract results.

../scripts/modify.py --source=../../../samples/DWR_1901_03_left.jpg \
                     --colour=1.0 \
                     --sharpness=1.0 \
                     --brightness=1.0 \
                     --contrast=0.1
../scripts/run_textract.py
../scripts/oplot_text.py
