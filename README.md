[![Stories in Ready](https://badge.waffle.io/alexanderjfink/miner.png?label=ready&title=Ready)](https://waffle.io/alexanderjfink/miner)
miner
=====

[![Build Status](https://travis-ci.org/alexanderjfink/miner.png)](https://travis-ci.org/alexanderjfink/miner)

Script for downloading, unpacking, and converting online and public (and others to be added soon) datafiles to open format

The goal of this app is to develop a bash interface, modeled after [homebrew](http://brew.sh "Homebrew for Mac OS X") that will allow anyone free and open access to data that is available on the web. The hope is to make it possible to do three things easily:

1. Search sources of data available online
2. Make data easy to download and enter into a database (of your choice) into a common format
3. Liberate public data by making it open data on your computer (you can use it in any format rather than proprietary formats, e.g. the US Census, which uses Access)

installation
------------

#### If you have pip installed
`$pip install miner`

#### Eventually I will add support for...

homebrew and R package manager

usage
-----

Please note - `miner` is in pre-alpha and these commands are meant to serve only as a preview for future functionality (chances aregood they are currently buggy)

### Searching
`$miner search (or dig) <dataset name> [OPTIONAL: subset name]`

#### Example
`$miner search (or dig) uscensus2010`
`$miner search (or dig) minnesotapublicschools`

### Describing (a dataset)
`$miner describe (or assay) <dataset name> [OPTIONAL: subset name]`

#### Example
`$miner describe (or assay) uscensus2010`
`$miner describe (or assay) uscensus2010 nd`

### Installing
`#miner install (or extract) <dataset name> [OPTIONAL: subset name]`

#### Example
`$miner install (or extract) uscensus2010`
`$miner install (or extract) uscensus2010 mn`

development
-----------

Testing: `$nosetests`

miner & dat
-----------

What is the difference between `miner` and [dat](https://github.com/maxogden/dat "dat on GitHub")? We don't `miner` as a competitor to dat. Rather, `miner` is a parallel and complementary project. Here are what we see as differences:

- `miner` focuses on using a formula (map) to get raw data files straight from original sources, download, and process them. dat is focused on building collaborative and version controlled datasets.
- While `miner` is in early development, it will be fully operational quickly and aims to be a very small application. dat aims to be a much more robust and comprehensive data collaboration tool. 
- Cleaned data (as dat would allow the sharing of) is great for software projects! However, researchers often need raw datasets to choose cleaning methods (these have their own biases) and ensure quality. 
- Some data is public but not yet copyleft/open--downloading your own copy is the only legal way to use it. Shared repositories may be allowed privately, but would be difficult to get permission for publicly.
- `miner` makes it possible to pull raw data regularly and note when data is changed (sometimes for [good](http://www.cs.cmu.edu/~enron/ "enron email data redacted") and perhaps sometimes for less good reasons.
- `miner` might be used as one tool to easily dump into dat. It should be one tool in an open data toolkit.

One way to look at it is that `miner` exists given today's non-standards-based, mixed license, individually/organizationally hosted dataset world. dat could be seen as the forerunner of the open knowledge / open data world.
