# Setup
Make sure virtualenv is installed
virtualenv .venv
cp ../frameworkpython .venv/bin/
source .venv/bin/activate
pip install -r requirements.txt

# Running
source .venv/bin/activate
frameworkpython otsu.py [picture_number]
