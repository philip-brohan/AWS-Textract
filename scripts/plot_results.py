#!/usr/bin/env python

# Plot a comparison of original image and transcription results.

import pickle
import argparse
from PIL import Image
import json

import matplotlib
from matplotlib.backends.backend_agg import \
             FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.patches
import numpy

# Get the file name as a command-line argument
parser = argparse.ArgumentParser()
parser.add_argument("--file", help="file name",
                    type=str,required=True)
args = parser.parse_args()

# We're going to need the original image
im = Image.open("../../OCR-weatherrescue/images/%s.jpg" % args.file)

# Show original and result side-by-side or top and bottom?
horizontal=True
if im.size[0]>im.size[1]: horizontal=False

if horizontal:
    fig=Figure(figsize=((2*im.size[0]/100)*1.06,
                        (im.size[1]/100)*1.04),
           dpi=100,
           facecolor=(0.88,0.88,0.88,1),
           edgecolor=None,
           linewidth=0.0,
           frameon=False,
           subplotpars=None,
           tight_layout=None)
    ax_original=fig.add_axes([0.02,0.02,0.47,0.96])
    ax_result=fig.add_axes([0.51,0.02,0.47,0.96])
else:
    fig=Figure(figsize=((im.size[0]/100)*1.04,
                         (2*im.size[1]/100)*1.06),
           dpi=100,
           facecolor=(0.88,0.88,0.88,1),
           edgecolor=None,
           linewidth=0.0,
           frameon=False,
           subplotpars=None,
           tight_layout=None)
    ax_figure=fig.add_axes([0.02,0.51,0.96,0.47],label='bg')
    ax_original=fig.add_axes([0.02,0.51,0.96,0.47],label='2')
    ax_result=fig.add_axes([0.02,0.02,0.96,0.47])
# Matplotlib magic
canvas=FigureCanvas(fig)
# Turn off the axis tics
ax_original.set_axis_off()
ax_result.set_axis_off()

# Put the original image in its half of the figure
ax_figure.imshow(im)

# Load the JSON from Textract for this image
textract=pickle.load( open( "../results.pkl/%s.pkl" % args.file, "rb" ) )
# Convert block polygon dictionary to numpy array for matplotlib
def d2p(dct):
    result=numpy.zeros((len(dct),2))
    for idx in range(len(dct)):
        result[idx,0]=dct[idx]['X']
        result[idx,1]=1.0-dct[idx]['Y']
    return result
    
# Draw all the blocks
zorder=10
for block in textract['Blocks']:
    np=matplotlib.patches.Polygon(d2p(block['Geometry']['Polygon']),
                                  closed=True,
                                  edgecolor=(0,0,0,1),
                                  facecolor=(0,0,0,0.2),
                                  fill=True,
                                  linewidth=0.2,
                                  alpha=0.2,
                                  zorder=zorder)
    #ax_result.add_patch(np)
    ax_original.add_patch(np)
    zorder=zorder+10

# Draw the image
fig.savefig('tst.png')
