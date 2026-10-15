#!/usr/bin/env python

import os
import pandas as pd
from urllib.request import Request, urlopen   # Dealing with web stuff

# The data directory
datadir = "../../data"

# The output file
outfile = "births-time-series-25.xlsx"

# The URL to obtain the data from.
url = "https://www.nrscotland.gov.uk/media/uwbfoukw/births-time-series-25.xlsx"

# Who is going to be reading the data. 
storage_options = {'User-Agent': 'Mozilla/5.0'}

# Create the data directory if it does not exists
if not os.path.exists(datadir):
    os.makedirs(datadir)

# Where to store the file
file = os.path.join(datadir,outfile)

# Add a User-Agent header to mimic a standard browser
# The National Records of Scotland blocks Python's default 
# urllib User-Agent header (Python-urllib/3.x) to prevent 
# automated scraping.
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

# Check if we need to download the file.
if os.path.isfile(file):
    print("Already have a local copy of the data.")
else:
    print("Downloading the data.")
    with urlopen(req) as in_stream, open(file, 'wb') as out_file:
        copyfileobj(in_stream, out_file)
