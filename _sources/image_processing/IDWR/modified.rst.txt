Modified Indian Daily Weather Report sample image
=================================================

The :doc:`Indian Daily Weather Report sample <../../samples/IDWR/text>` worked much better with the image contrast reduced and the sharpness set to zero.

.. figure:: ../../../analyses/image_processing/IDWR/oplot.png
   :width: 95%
   :align: center
   :figwidth: 95%

   `Indian Daily Weather Report sample image <http://s3-eu-west-1.amazonaws.com/textract.samples/idwr1893-v1_0021.jpg>`_, after image adjustment, overlain by the text blocks produced by Textract.

|	      

Script to make the figure:

..  literalinclude:: ../../../analyses/image_processing/IDWR/make.sh

Using:

.. toctree::
   :maxdepth: 1
   :titlesonly:

   ../scripts/modify
   ../scripts/run_textract
   ../scripts/oplot_text


