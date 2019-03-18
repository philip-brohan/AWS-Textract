#!/usr/bin/env bash

# Crop, and Tweak the contrast on the US weathermap sample to get 
#   much better Textract results.

convert -crop 700x2550+2700x0 -geometry 1400x5100 ../../../samples/US_Weather_map_19150814.jpg cropped.jpg
../scripts/modify.py --source=cropped.jpg \
                     --colour=1.0 \
                     --sharpness=0.0 \
                     --brightness=1.0 \
                     --contrast=0.4
../scripts/run_textract.py
../scripts/oplot_text.py
