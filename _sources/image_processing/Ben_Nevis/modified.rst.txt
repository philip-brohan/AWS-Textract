Modified Ben Nevis sample image
===============================

The :doc:`Ben Nevis project sample <../../samples/Ben_Nevis/text>` worked much better with the image contrast reduced to the point where humans can hardly read it.

.. figure:: ../../../analyses/image_processing/Ben_Nevis/oplot.png
   :width: 95%
   :align: center
   :figwidth: 95%

   `Ben Nevis project sample image <http://s3-eu-west-1.amazonaws.com/textract.samples/1901-01.jpg>`_, after image adjustment, overlain by the text blocks produced by Textract.

|	      

Script to make the figure:

..  literalinclude:: ../../../analyses/image_processing/Ben_Nevis/make.sh

Using:

.. toctree::
   :maxdepth: 1
   :titlesonly:

   ../scripts/modify
   ../scripts/run_textract
   ../scripts/oplot_text


