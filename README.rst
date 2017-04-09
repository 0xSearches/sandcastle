.. raw:: html

   <p align="center">

.. raw:: html

   </p>

Inspired by a conversation with Instacart's
[@nickelser](https://github.com/nickelser) on HackerOne, I've optimised
and published Sandcastle – a Python script for AWS S3 bucket
enumeration, formerly known as bucketCrawler.

The script takes a target name as the "stem" argument (e.g.
``instacart``) and iterates through a text file containing bucket name
permutations, e.g. as below:

::

    -training
    -bucket
    -dev
    -attachments
    -photos
    -elasticsearch
    [...]

Getting started
---------------

Here's how to get started: 1. Install with Pip:
``pip install sandcastle`` 2. Run ``sandcastle.py`` with a target name
and input file (grab an example from this repo) 3. Valid bucket
permutations will be identified as "matches"

::

    usage: sandcastle.py [-h] -t targetStem [-f inputFile]

    arguments:
      -h, --help            show this help message and exit
      -t targetStem, --target targetStem
                            Select a target stem name (e.g. 'instacart')
      -f inputFile, --file inputFile
                            Select a bucket permutation file (default: bucket-
                            names.txt)

::

    [+] Match: shopify-dev --> 403
    [+] Match: shopify-pics --> 403
    [+] Match: shopify-assets --> 403
    [+] Match: shopify-development --> 403
    [+] Match: shopify-content --> 403
    [+] Match: shopify-ops --> 200

Status codes and testing
~~~~~~~~~~~~~~~~~~~~~~~~

+---------------+-----------------------+-------------------------------------------------+
| Status code   | Definition            | Notes                                           |
+===============+=======================+=================================================+
| 404           | Bucket Not Found      | Not a target for analysis (hidden by default)   |
+---------------+-----------------------+-------------------------------------------------+
| 403           | Access Denied         | Potential target for analysis via the CLI       |
+---------------+-----------------------+-------------------------------------------------+
| 200           | Publicly Accessible   | Potential target for analysis via the CLI       |
+---------------+-----------------------+-------------------------------------------------+

AWS CLI commands
~~~~~~~~~~~~~~~~

Here's a quick reference of some useful AWS CLI commands: \* List Files:
``aws s3 ls s3://bucket-name`` \* Download Files:
``aws s3 cp s3://bucket-name/<file> <destination>`` \* Upload Files:
``aws s3 cp/mv test-file.txt s3://bucket-name`` \* Remove Files:
``aws s3 rm s3://bucket-name/test-file.txt``

What is S3?
-----------

From the Amazon
`documentation <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html>`__,
*Working with Amazon S3 Buckets*: > Amazon S3 [Simple Storage Service]
is cloud storage for the Internet. To upload your data (photos, videos,
documents etc.), you first create a bucket in one of the AWS Regions.
You can then upload any number of objects to the bucket.

    In terms of implementation, buckets and objects are resources, and
    Amazon S3 provides APIs for you to manage them.

Closing remarks
---------------

-  This is my first public security project and package; Sandcastle is
   published under the MIT License.
-  Usage acknowlegements:
-  Castle (icon) by Andrew Doane from the Noun Project
-  Nixie One (logo typeface) free by Jovanny Lemonad
