miner
=====

Script for downloading, unpacking, and converting US Census (and others to be added soon) datafiles to open format

The goal of this app is to develop a bash interface, modeled after homebrew (brew.sh) that will allow anyone free and open access to data that is available on the web. The hope is to make it possible to do three things easily:

1. Search sources of data available online
2. Make data easy to download and enter into a database (of your choice) into a common format
3. Liberate public data by making it open data on your computer (you can use it in any format rather than proprietary formats (like the US Census, which uses Access)

Currently I am working on liberating the Census data. I will commit my code as soon as I am able to successfully do that.

miner & dat
-----------

What is the difference between miner and [dat](https://github.com/maxogden/dat "dat on GitHub")? We don't see ourselves as competitors. Rather, we are working on parallel and complementary projects. Here are what we see as differences:

- miner focuses on using a formula (map) to get raw data files straight from original sources, download, and process them. dat is focused on building collaborative and version controlled datasets.
- Some data like the US Census has unique identifiers stripped across tablesand is more difficult to turn into a key/value store.
- While miner is in early development, it will be fully operational quickly and aims to be a very small application. dat is still in heavy early development and aims to be a much more robust and comprehensive data collaboration tool. 
- Cleaned data (as dat would allow the sharing of) is great for software projects! However, researchers often need raw datasets to choose cleaning methods and ensure quality. 
- Some data is public but not yet copyleft/open--downloading your own copy is the only legal way to use it. Shared repositories may be allowed privately, but would be difficult to get permission for publicly.
- miner makes it possible to pull raw data regularly and note when data is changed.
- miner might be used as one tool to easily dump into dat.

One way to look at it is that miner exists given today's non-standards-based, mixed license, individually/organizationally hosted dataset world. dat could be seen as the forerunner of the open knowledge / open data world.
