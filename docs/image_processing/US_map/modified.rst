Modified US map sample image
===============================

The :doc:`US map sample <../../samples/US_map/text>` neded to be cropped to just the data table, and have both its contrast and its sharpness reduced, to make it even a partial success.

.. figure:: ../../../analyses/image_processing/US_map/oplot.png
   :width: 95%
   :align: center
   :figwidth: 95%

   `US map sample image <http://s3-eu-west-1.amazonaws.com/textract.samples/US_Weather_map_19150814.jpg>`_, after image adjustment, overlain by the text blocks produced by Textract.

|	      

Script to make the figure:

..  literalinclude:: ../../../analyses/image_processing/US_map/make.sh

Using:

.. toctree::
   :maxdepth: 1
   :titlesonly:

   ../scripts/modify
   ../scripts/run_textract
   ../scripts/oplot_text


