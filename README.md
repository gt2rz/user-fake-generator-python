# Python Virtual Environment Setup
python3 -m venv venv

# Activate the virtual environment
## On linux or mac
source venv/bin/activate

## On windows
venv\Scripts\activate

# Install the required packages
pip install -r requirements.txt

# Run the application
python3 app.py

# Deactivate the virtual environment
deactivate

