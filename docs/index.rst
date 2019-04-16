Testing AWS Textract for weather data rescue
============================================

Our understanding of weather and climate depends fundamentally on observations, and access to weather observations covering a long period is a key requirement for research on climate variability and change. The world's archives preserve `a wealth of weather observations, going back hundreds of years <http://brohan.org/UK-digitisation/>`_, but many are undigitised, and so unavailable for most use. There is `a substantial research community working to recover these observations <http://www.met-acre.net>`_ and we have run `several large data rescue projects <http://brohan.org/transcription_methods_review/>`_. All these projects use manual transcription of the archive documents, this works, but is much too slow: to rescue the millions of pages of of past weather observations in the archives we need to go *much* faster. 

`Amazon Textract <https://aws.amazon.com/textract/>`_ is a web service (currently in closed beta) that automatically extracts text and data from scanned documents. This document describes a test of this service as a tool for weather data rescue.

.. toctree::
   :maxdepth: 1

   Getting started with Textract <install>
   
I tested Textract on sample images from several different documents containing weather observations we need to transcribe. Some were somewhat successful:
   
.. toctree::
   :maxdepth: 1

   samples/Second_order/text
   samples/Observatories/text
   samples/DWR_1862/text
   samples/Farragut/text
   samples/Jeannette/text
   
Some were total failures:

.. toctree::
   :maxdepth: 1

   samples/Ben_Nevis/text
   samples/Argentine_DWR/text
   samples/US_map/text
   samples/IDWR/text
   samples/DWR_1901/text

Textract is a black box, there's no way to control how it operates, so the only way to try and improve the output is to modify the images before running Textract on them. It's easy to change things like the saturation, contrast and sharpness, and it does make a difference - all of the failed samples can be converted into (partial) successes by changing the image contrast, sharpness, and size.

.. toctree::
   :maxdepth: 1

   image_processing/Ben_Nevis/modified
   image_processing/Argentine_DWR/modified
   image_processing/US_map/modified
   image_processing/IDWR/modified
   image_processing/DWR_1901/modified

A combination of cropping, contrast reduction, and sharpness reduction, worked well to change total failures into partial successes. I have not managed to use such image adjustment to make partial successes into bigger successes.


As the image modification produced reasonable results on the :doc:`Ben Nevis project sample <image_processing/Ben_Nevis/modified>`, it was possible to run Textract against the `OCR-weatherrescue transcription benchmark <http://brohan.org/OCR-weatherrescue/index.html>`_:

.. toctree::
   :titlesonly:
   :maxdepth: 1

   OCR-weatherrescue/months

As of March 2019, Textract is a very encouraging technology. It's not yet good enough to be used operationally on documents of this type, but it is *almost* good enough for the simplest examples. It's still in beta test, and it seems likely that future versions will be very useful. Its speed and ease of use mean that, if it does improve sufficiently, it will be a big asset to data rescue work.

.. toctree::
   :titlesonly:
   :maxdepth: 1

   Small Print <credits>

This document is crown copyright (2019). It is published under the terms of the `Open Government Licence <https://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/>`_.
