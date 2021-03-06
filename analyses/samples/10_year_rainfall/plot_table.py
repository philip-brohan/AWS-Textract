#!/usr/bin/env python

# Plot a comparison of original image and transcription results.
# Show the table structure found by textract.

import pickle
import argparse
from PIL import Image

import matplotlib
from matplotlib.backends.backend_agg import \
             FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.patches
import numpy

# We're going to need the original image
im = Image.open("../../../samples/10-year-rainfall.jpg")

fig=Figure(figsize=((im.size[0]/100)*1.06,
                    (im.size[1]/100)*1.04),
       dpi=100,
       facecolor=(0.88,0.88,0.88,1),
       edgecolor=None,
       linewidth=0.0,
       frameon=False,
       subplotpars=None,
       tight_layout=None)
ax_original=fig.add_axes([0.02,0.02,0.96,0.96],label='original')
ax_result=fig.add_axes([0.02,0.02,0.96,0.96],label='result')
# Matplotlib magic
canvas=FigureCanvas(fig)
# Turn off the axis tics
ax_original.set_axis_off()
ax_result.set_axis_off()

# Put the original image in its half of the figure
ax_original.imshow(im)

# Load the JSON from Textract for this image
textract=pickle.load( open( "detection.pkl", "rb" ) )
# Convert block polygon dictionary to numpy array for matplotlib
def d2p(dct):
    result=numpy.zeros((len(dct),2))
    for idx in range(len(dct)):
        result[idx,0]=dct[idx]['X']
        result[idx,1]=1.0-dct[idx]['Y']
    return result
# Convert block bounding box dictionary to numpy array for matplotlib
def b2p(dct):
    result=numpy.zeros((4,2))
    result[0,0]=dct['Left']
    result[1,0]=dct['Left']+dct['Width']
    result[2,0]=dct['Left']+dct['Width']
    result[3,0]=dct['Left']
    result[0,1]=1.0-dct['Top']
    result[1,1]=1.0-dct['Top']
    result[2,1]=1.0-dct['Top']-dct['Height']
    result[3,1]=1.0-dct['Top']-dct['Height']
    return result
    
# Draw the 'CELL' blocks - coloured by row and column index
zorder=10
for block in textract['Blocks']:
    #print(block['BlockType'])
    if block['BlockType'] != 'CELL': continue
    #print('Y')
    ccolour=(0,0,1)
    if (block['ColumnIndex']+block['RowIndex'])%2==1:
        ccolour=(1,0,0)
    pp=matplotlib.patches.Polygon(d2p(block['Geometry']['Polygon']),
                                  closed=True,
                                  edgecolor=(0,0,0),
                                  facecolor=ccolour,
                                  fill=True,
                                  linewidth=2,
                                  alpha=0.2,
                                  zorder=zorder)
    if zorder>0: ax_result.add_patch(pp)
    zorder=zorder+10

# Draw the image
fig.savefig('Table.png')
