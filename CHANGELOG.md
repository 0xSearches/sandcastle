# Change Log
All notable changes to the Sandcastle script will be documented in this file.

## 1.2.3 – 2017-04-09
- Due to PyPi issues, Sandcastle will not ship with a default `bucket-names.txt`.
	* The example `bucket-names.txt` can be downloaded from this repo
	* By default, Sandcastle searches for `bucket-names.txt` in the current directory 
	* As previously, use the `-f` flag to specify a different input file
- Removes "no match" display from Sandcastle script

## 1.2.2 – 2017-04-09
- Sandcastle is now live on PyPi! This version fixes an import issue with `bucket-names.txt`.

## 1.2.1 – 2017-04-09
- Sandcastle is being packaged and published on PyPi; this version is used for compatibility purposes.

## 1.2.0 – 2017-04-09
- Sandcastle now supports the `-f` argument (text file)
	* The script defaults to `bucket-names.txt` if one is not given
- Sandcastle now presents a line count for the specified text file
- Adjusted ASCII header art and script wording

## 1.1.0 – 2017-04-09
- Sandcastle now distinguishes between bucket status codes
	* Buckets returning 404 are hidden by default
	* Other status codes are displayed as potential "matches"
- Sandcastle script and documentation improvements
- Established `CHANGELOG.md` for update tracking

## 1.0.0 – 2017-04-08
- Initial public release of the optimised bucketCrawler script
- Initial `README.md` documentation and bucket permutations
