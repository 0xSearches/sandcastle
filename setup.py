from distutils.core import setup
setup(
  name = 'sandcastle',
  version = '1.2.3',
  description = 'A Python script for AWS S3 bucket enumeration.',
  author = 'Yasin Soliman',
  author_email = 'ysx.public@icloud.com',
  scripts=['sandcastle.py'],
  url = 'https://github.com/yasinS/sandcastle',
  download_url = 'https://github.com/yasinS/sandcastle/archive/1.2.3.tar.gz',
  package_data={
        'sandcastle': ['bucket-names.txt'],
  },
  keywords = ['amazons3', 'infosec', 'bucket'],
  classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Security",
  ],

)
