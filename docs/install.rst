Getting started with Textract
=============================

This is what worked for me on OSX & Linux:

* Install the `AWS command line tools <https://aws.amazon.com/cli/>`_ and the `AWS SDK for Python (Boto3) <https://aws.amazon.com/sdk-for-python/>`_. As I already use `conda <https://conda.io/en/latest/>`_, I found it easiest to use that. Just `activate` your environment of choice and then add the AWS tools to it with:

  .. code:: bash

    conda install -c conda-forge awscli
    conda install -c conda-forge boto3
    
* `Create an AWS account <https://aws.amazon.com/>`_.
* Configure your AWS account:
  
.. code:: bash

    aws configure
  
* Configure your AWS account to use Textract:

.. code:: bash

    aws s3 cp s3://amazon-textract-preview2/service-2.json
    aws configure add-model --service-model file://./service-2.json --service-name textract
    
That should be enough to get it working. Test it from the command line by running Textract on a file in S3 (I used `this one <https://s3-eu-west-1.amazonaws.com/textract.samples/Margate_1891_02.png>`_).

.. code:: bash

   aws textract analyze-document --document '{"S3Object":{"Bucket":"textract.samples","Name":"Margate_1891_02.png"}}' --feature-types '["TABLES","FORMS"]'
   
If it works, this will return a load of JSON output. If it produces an error message, something has gone wrong.


    

    
