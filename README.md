# Project Prognosis

# Installation

## Manual

### Setting Up the Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Unix/Linux/Mac)
source venv/bin/activate

# Activate the virtual environment (Windows)
venv\Scripts\activate
```

### Installing Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

### Run

```bash
streamlit run app/main.py
```

## Docker container

### Create image

```bash
docker build -t prognosis-app  .
```

### Run container

```bash
docker run -d -p 8089:8089 --name prognosis-app-container prognosis-app 
```

The application will be available at http://127.0.0.1:8089.