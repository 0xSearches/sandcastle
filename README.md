![Sandcastle logo - AWS S3 bucket enumeration](https://cloud.githubusercontent.com/assets/4115778/24827505/eab7322a-1c42-11e7-96f3-dbc772da5f10.png)

Inspired by a conversation with Instacart's [@nickelser](https://github.com/nickelser) on HackerOne, I've optimised and published Sandcastle – a Python script for AWS S3 bucket enumeration, formerly known as bucketCrawler.

In its current first-version form, the script takes a target name as the "stem" argument (e.g. `instacart`) and iterates through a text file containing bucket name permutations, e.g. as below:

```
-training
-bucket
-dev
-attachments
-photos
-elasticsearch
[...]
```
## Getting started
Here's how to get started:
1. Clone the repository to your desired location
2. Open `bucket-names.txt` and customise your permutations (optional)
3. Run `python sandcastle.py -t <targetname>`
4. Each permutation will be returned with its HTTP status code

```
usage: sandcastle.py [-h] -t webStem

optional arguments:
  -h, --help            show this help message and exit
  -t webStem, --target webStem
                        Select a target stem name (e.g. 'instacart')
```

```
instacart-training --> 403
instacart-bucket --> 404
instacart-dev --> 404
instacart-attachments --> 404
```

### Status codes and testing

| Status code        | Definition           | Notes  |
| ------------- | ------------- | -----|
| 404      | Bucket Not Found | Not a target for analysis |
| 403      | Access Denied      |   Target for analysis – write may still be possible |
| 200 | Publicly Accessible      |    Target for analysis  |

### AWS CLI commands
Here's a quick reference of some useful AWS CLI commands:
* List Files: `aws s3 ls s3://bucket-name`
* Download Files: `aws s3 cp s3://bucket-name/<file> <destination>`
* Upload Files: `aws s3 cp/mv test-file.txt s3://bucket-name`
* Remove Files: `aws s3 rm s3://bucket-name/test-file.txt`

## What is S3?
From the Amazon [documentation](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html), *Working with Amazon S3 Buckets*:
> Amazon S3 is cloud storage for the Internet. To upload your data (photos, videos, documents etc.), you first create a bucket in one of the AWS Regions. You can then upload any number of objects to the bucket.

> In terms of implementation, buckets and objects are resources, and Amazon S3 provides APIs for you to manage them.

## Acknowledgements
* This project is licensed under the MIT License, as referenced in `LICENSE`.
* Castle (icon) by Andrew Doane from the Noun Project
* Nixie One (logo typeface) free by Jovanny Lemonad
