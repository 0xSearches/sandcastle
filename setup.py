from distutils.core import setup
setup(
  name = 'sandcastle',
  packages = ['sandcastle'], # this must be the same as the name above
  version = '1.2.0',
  description = 'A Python script for AWS S3 bucket enumeration.',
  author = 'Yasin Soliman',
  author_email = 'ysx.public@icloud.com',
  scripts=['sandcastle'],
  url = 'https://github.com/yasinS/sandcastle', # use the URL to the github repo
  download_url = 'https://github.com/yasinS/sandcastle/archive/1.2.0.tar.gz', # I'll explain this in a second
  keywords = ['amazons3', 'infosec', 'bucket'], # arbitrary keywords
  classifiers = [],
)
