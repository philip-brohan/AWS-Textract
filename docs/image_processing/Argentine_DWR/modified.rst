Modified Argentine DWR sample image
===================================

The :doc:`Argentine DWR project sample <../../samples/Argentine_DWR/text>` worked much better with the image contrast reduced to the point where humans can hardly read it.

.. figure:: ../../../analyses/image_processing/Argentine_DWR/oplot.png
   :width: 95%
   :align: center
   :figwidth: 95%

   `Argentine DWR sample image <http://s3-eu-west-1.amazonaws.com/textract.samples/103.jpg>`_, after image adjustment, overlain by the text blocks produced by Textract.

|	      

Script to make the figure:

..  literalinclude:: ../../../analyses/image_processing/Argentine_DWR/make.sh

Using:

.. toctree::
   :maxdepth: 1
   :titlesonly:

   ../scripts/modify
   ../scripts/run_textract
   ../scripts/oplot_text


