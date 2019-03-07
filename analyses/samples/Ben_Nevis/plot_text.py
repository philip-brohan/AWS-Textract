#!/usr/bin/env python

# Plot a comparison of original image and transcription results.

import pickle
from PIL import Image

import matplotlib
from matplotlib.backends.backend_agg import \
             FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.patches
import numpy

# We're going to need the original image
im = Image.open("../../../samples/1901-01.jpg")

fig=Figure(figsize=((1*im.size[0]/100)*1.04,
                    (2*im.size[1]/100)*1.06),
       dpi=100,
       facecolor=(0.88,0.88,0.88,1),
       edgecolor=None,
       linewidth=0.0,
       frameon=False,
       subplotpars=None,
       tight_layout=None)
ax_original=fig.add_axes([0.02,0.51,0.96,0.47])
ax_result=fig.add_axes([0.02,0.02,0.96,0.47])
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
# Get bounding box centroid for text
def b2t(dct):
    result=[0,0]
    result[0]=dct['Left']+dct['Width']/2
    result[1]=1.0-dct['Top']-dct['Height']/2
    return result
    
# Draw all the blocks
zorder=0
for block in textract['Blocks']:
    if 'Text' in block and 'Relationships' in block:
       # Polygon
        pp=matplotlib.patches.Polygon(d2p(block['Geometry']['Polygon']),
                                      closed=True,
                                      edgecolor=(0,0,1,1),
                                      facecolor=(0,0,1,0.2),
                                      fill=True,
                                      linewidth=0.2,
                                      alpha=0.2,
                                      zorder=zorder)
        ax_result.add_patch(pp)
       # Text
        txt_centroid=b2t(block['Geometry']['BoundingBox'])
        angle=0
        if (block['Geometry']['BoundingBox']['Height'] >
            block['Geometry']['BoundingBox']['Width']*2):
            angle=90
        ax_result.text(txt_centroid[0],txt_centroid[1],
                       block['Text'],
                       fontsize=28,
                       verticalalignment='center',
                       horizontalalignment='center',
                       rotation=angle)
    if zorder==0: # 1st block - page fill
        pp=matplotlib.patches.Polygon(d2p(block['Geometry']['Polygon']),
                                      closed=True,
                                      edgecolor=(0,0,0,1),
                                      facecolor=(0,0,0,0.2),
                                      fill=True,
                                      linewidth=0.2,
                                      alpha=0.05,
                                      zorder=zorder)
        ax_result.add_patch(pp)        
    zorder=zorder+10
    

# Draw the image
fig.savefig('Ben_Nevis_text.png')
