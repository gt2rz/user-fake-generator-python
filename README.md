# Python Virtual Environment Setup
python3 -m venv venv

# Activate the virtual environment
## On linux or mac
source venv/bin/activate

## On windows
venv\Scripts\activate

# Install the required packages
pip install -r requeriments.txt

# View the installed packages
pip list

# Run the application
python3 app.py

# Deactivate the virtual environment
deactivate

# Run Redis Docker 
docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest