#!/usr/bin/bash

# Tweak the contrast on the Ben-Nevis sample to get 
#   much better Textract results.

../scripts/modify.py --source=../../../samples/1901-01.jpg \
                     --colour=1.0 \
                     --sharpness=0.0 \
                     --brightness=1.0 \
                     --contrast=0.1
../scripts/run_textract.py
../scripts/oplot_text.py
