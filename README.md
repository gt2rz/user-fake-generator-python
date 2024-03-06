# Python Virtual Environment Setup
python -m venv venv

# Activate the virtual environment
## On linux or mac
source venv/bin/activate

## On windows
venv\Scripts\activate

# Install the required packages
pip install -r requirements.txt

# Run the application
python app.py

# Deactivate the virtual environment
deactivate

