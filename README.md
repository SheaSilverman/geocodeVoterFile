# GeoCoding Florida Voter File

## Getting Started

Make sure you are using a virtual environment of some sort (e.g. `virtualenv` or
`pyenv`).

virtualenv ENV
source ENV/bin/activate

```
pip install -r requirements.txt
```

Edit hereApi.py:

Add your developer.here.com API keys to:

APP_ID = ''
APP_CODE = ''

Then set your Voter File CSV to:
SOURCE_FILE = '/path/to/file.csv'

And the name of the output geocoded file to:

DESTINATION_FILE '/path/to/new_file.csv'

Now run python hereAPI.py

It took about 20 hours to run through District 49, which is 110,000 voters.