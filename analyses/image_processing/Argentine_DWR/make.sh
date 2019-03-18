#!/usr/bin/env bash

# Tweak the contrast on the Argentine DWR sample to get 
#   much better Textract results.

../scripts/modify.py --source=../../../samples/103.jpg \
                     --colour=1.0 \
                     --sharpness=1.0 \
                     --brightness=1.0 \
                     --contrast=0.1
../scripts/run_textract.py
../scripts/oplot_text.py
