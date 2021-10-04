<p align="center">
   
<img src="https://cloud.githubusercontent.com/assets/4115778/24827505/eab7322a-1c42-11e7-96f3-dbc772da5f10.png" width="70%" alt="Sandcastle logo - AWS S3 bucket enumeration">

Inspired by a conversation with Instacart's [@nickelser](https://github.com/nickelser) on HackerOne, I've optimised and published Sandcastle – a Python script for AWS S3 bucket enumeration, formerly known as bucketCrawler.

The script takes a target's name as the stem argument (e.g. `shopify`) and iterates through a file of bucket name permutations, such as the ones below:

```
-training
-bucket
-dev
-attachments
-photos
-elasticsearch
[...]
```

## Requirements
* Python 3
* Python requests module
* [AWS CLI Version 2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

## Getting started
Here's how to get started:

1. Clone this repo.
2. Install python virtual environment `python3 -m pip install --user virtualenv`
3. Create and activate virtual environment `python3 -m venv env && source env/bin/activate` 
4. Install python module(s) `pip install -r requirements.txt`
5. Run `sandcastle.py` with a target name and input file (grab an example from this repo)
6. Matching bucket permutations will be identified, and read permissions tested.
* When you're finished running the project you can exit the virtual environment with the command `deactivate`

```
usage: sandcastle.py [-h] -t targetStem [-f inputFile]

arguments:
  -h, --help            show this help message and exit
  -t targetStem, --target targetStem
                        Select a target stem name (e.g. 'shopify')
  -f inputFile, --file inputFile
                        Select a bucket permutation file (default: bucket-
                        names.txt)
```

```
   ____             __             __  __
  / __/__ ____  ___/ /______ ____ / /_/ /__
 _\ \/ _ `/ _ \/ _  / __/ _ `(_-</ __/ / -_)
/___/\_,_/_//_/\_,_/\__/\_,_/___/\__/_/\__/

S3 bucket enumeration // release v1.2.4 // ysx


[*] Commencing enumeration of 'shopify', reading 138 lines from 'bucket-names.txt'.

[+] Checking potential match: shopify-content --> 403

An error occurred (AccessDenied) when calling the ListObjects operation: Access Denied

```

### Status codes and testing

| Status code        | Definition     | Notes|
| ------------- | -------------       | -----|
| 404           | Bucket Not Found    | Not a target for analysis (hidden by default)|
| 403           | Access Denied       | Potential target for analysis via the CLI |
| 200           | Publicly Accessible | Potential target for analysis via the CLI |

### AWS CLI commands
Here's a quick reference of some useful AWS CLI commands:
* List Files: `aws s3 ls s3://bucket-name`
* Download Files: `aws s3 cp s3://bucket-name/<file> <destination>`
* Upload Files: `aws s3 cp/mv test-file.txt s3://bucket-name`
* Remove Files: `aws s3 rm s3://bucket-name/test-file.txt`

## What is S3?
From the Amazon [documentation](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html), *Working with Amazon S3 Buckets*:
> Amazon S3 [Simple Storage Service] is cloud storage for the Internet. To upload your data (photos, videos, documents etc.), you first create a bucket in one of the AWS Regions. You can then upload any number of objects to the bucket.

> In terms of implementation, buckets and objects are resources, and Amazon S3 provides APIs for you to manage them.

## Closing remarks
* This is my first public security project. Sandcastle is published under the MIT License.
* Usage acknowlegements:
  * Castle (icon) by Andrew Doane from the Noun Project
  * Nixie One (logo typeface) free by Jovanny Lemonad
