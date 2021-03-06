OCR-weatherrescue benchmark comparison
======================================

The `OCR-weatherrescue benchmark <http://brohan.org/OCR-weatherrescue/index.html>`_ is a test dataset for document transcription systems. It contains 81 document images, each of a table of numbers, and quality-controlled transcriptions for each. Textract can be run on each of the images, and scored on its ability to reproduce the known results.

.. figure:: ../../analyses/OCR-weatherrescue/1898-02.png
   :width: 95%
   :align: center
   :figwidth: 95%

   Textract results for :doc:`a sample month  <auto_generated/1898-02>`. Green blocks are entries sucessfully read by Textract. Filled red blocks are entries inacurately read, and hatched red blocks are entries missed altogether.


Comparisons by month
--------------------

.. list-table:: 
   :widths: 15 10 10 10 10 10 10 10 10 10 10 10 10
   :header-rows: 0

   * - 1898  
     - :doc:`Jan <auto_generated/1898-01>` 
     - :doc:`Feb <auto_generated/1898-02>`
     - :doc:`Mar <auto_generated/1898-03>`
     - :doc:`Apr <auto_generated/1898-04>`
     - :doc:`May <auto_generated/1898-05>`
     - :doc:`Jun <auto_generated/1898-06>`
     - :doc:`Jul <auto_generated/1898-07>`
     - :doc:`Aug <auto_generated/1898-08>`
     - :doc:`Sep <auto_generated/1898-09>`
     - :doc:`Oct <auto_generated/1898-10>`
     - :doc:`Nov <auto_generated/1898-11>`
     - :doc:`Dec <auto_generated/1898-12>`
   * - 1899  
     - :doc:`Jan <auto_generated/1899-01>` 
     - :doc:`Feb <auto_generated/1899-02>`
     - :doc:`Mar <auto_generated/1899-03>`
     - :doc:`Apr <auto_generated/1899-04>`
     - :doc:`May <auto_generated/1899-05>`
     - :doc:`Jun <auto_generated/1899-06>`
     - :doc:`Jul <auto_generated/1899-07>`
     - :doc:`Aug <auto_generated/1899-08>`
     - :doc:`Sep <auto_generated/1899-09>`
     - :doc:`Oct <auto_generated/1899-10>`
     - :doc:`Nov <auto_generated/1899-11>`
     - :doc:`Dec <auto_generated/1899-12>`
   * - 1900  
     - :doc:`Jan <auto_generated/1900-01>` 
     - :doc:`Feb <auto_generated/1900-02>`
     - :doc:`Mar <auto_generated/1900-03>`
     - :doc:`Apr <auto_generated/1900-04>`
     - :doc:`May <auto_generated/1900-05>`
     - :doc:`Jun <auto_generated/1900-06>`
     - :doc:`Jul <auto_generated/1900-07>`
     - :doc:`Aug <auto_generated/1900-08>`
     - :doc:`Sep <auto_generated/1900-09>`
     - :doc:`Oct <auto_generated/1900-10>`
     - :doc:`Nov <auto_generated/1900-11>`
     - :doc:`Dec <auto_generated/1900-12>`
   * - 1901  
     - :doc:`Jan <auto_generated/1901-01>` 
     - :doc:`Feb <auto_generated/1901-02>`
     - :doc:`Mar <auto_generated/1901-03>`
     - :doc:`Apr <auto_generated/1901-04>`
     - :doc:`May <auto_generated/1901-05>`
     - :doc:`Jun <auto_generated/1901-06>`
     - :doc:`Jul <auto_generated/1901-07>`
     - :doc:`Aug <auto_generated/1901-08>`
     - :doc:`Sep <auto_generated/1901-09>`
     - :doc:`Oct <auto_generated/1901-10>`
     - :doc:`Nov <auto_generated/1901-11>`
     - :doc:`Dec <auto_generated/1901-12>`
   * - 1902  
     - :doc:`Jan <auto_generated/1902-01>` 
     - :doc:`Feb <auto_generated/1902-02>`
     - :doc:`Mar <auto_generated/1902-03>`
     - :doc:`Apr <auto_generated/1902-04>`
     - :doc:`May <auto_generated/1902-05>`
     - :doc:`Jun <auto_generated/1902-06>`
     - :doc:`Jul <auto_generated/1902-07>`
     - :doc:`Aug <auto_generated/1902-08>`
     - :doc:`Sep <auto_generated/1902-09>`
     - :doc:`Oct <auto_generated/1902-10>`
     - :doc:`Nov <auto_generated/1902-11>`
     - :doc:`Dec <auto_generated/1902-12>`
   * - 1903  
     - :doc:`Jan <auto_generated/1903-01>` 
     - :doc:`Feb <auto_generated/1903-02>`
     - :doc:`Mar <auto_generated/1903-03>`
     - :doc:`Apr <auto_generated/1903-04>`
     - :doc:`May <auto_generated/1903-05>`
     - :doc:`Jun <auto_generated/1903-06>`
     - :doc:`Jul <auto_generated/1903-07>`
     - :doc:`Aug <auto_generated/1903-08>`
     - :doc:`Sep <auto_generated/1903-09>`
     - :doc:`Oct <auto_generated/1903-10>`
     - :doc:`Nov <auto_generated/1903-11>`
     - :doc:`Dec <auto_generated/1903-12>`
   * - 1904  
     - :doc:`Jan <auto_generated/1904-01>` 
     - :doc:`Feb <auto_generated/1904-02>`
     - :doc:`Mar <auto_generated/1904-03>`
     - :doc:`Apr <auto_generated/1904-04>`
     - :doc:`May <auto_generated/1904-05>`
     - :doc:`Jun <auto_generated/1904-06>`
     - :doc:`Jul <auto_generated/1904-07>`
     - :doc:`Aug <auto_generated/1904-08>`
     - :doc:`Sep <auto_generated/1904-09>`
     - 
     - 
     - 

Summary
-------

Of 59,136 entries:
 * 54,650 (92%) were read successfully
 *  3,361 (6%) were read inaccurately
 *  1,125 (2%) were missed altogether

Textract is now pretty good - it's not up to the accuracy rate of manual ranscription (99%+ on this sort of data), but a success rate over 90% is good enough to be useful, and it is likely that adding more quality control checks would increase the success rate further.

Its speed advantage over manual transcription is **enormous**. Transcribing this dataset took the citizen science project `weatherrescue.org <http://weatherrescue.org>`_ many days of human effort, spread over weeks of elapsed time. Textract took only a few minutes (and parallelising calls to Textract could reduce this to seconds).
 
