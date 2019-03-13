Modified DWR_1901 sample image
===============================

The :doc:`Daily Weather Report 1901 sample <../../samples/DWR_1901/text>` worked much better with the image contrast reduced to the point where humans can hardly read it.

.. figure:: ../../../analyses/image_processing/DWR_1901/oplot.png
   :width: 95%
   :align: center
   :figwidth: 95%

   `Daily Weather Report 1901 sample image <http://s3-eu-west-1.amazonaws.com/textract.samples/DWR_1901_03_left.jpg>`_, after image adjustment, overlain by the text blocks produced by Textract.

|	      

Script to make the figure:

..  literalinclude:: ../../../analyses/image_processing/DWR_1901/make.sh

Using:

.. toctree::
   :maxdepth: 1
   :titlesonly:

   ../scripts/modify
   ../scripts/run_textract
   ../scripts/oplot_text


