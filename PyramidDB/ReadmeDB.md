# Install the Virtual Environment
```bash
python3 -m venv db_env
```

# Upgrade PIP and install Pyramid and dependencies
```bash
source ./db_env/bin/activate
pip install --upgrade pip
pip install pyramid=="1.10.1"
pip install pyramid-jinja2
```

# Install MySQL library
## NOTE: First you must install MySQL on your machine! (link: https://www.mysql.com/downloads/)
```bash
pip install mysql-connector
```

# Freeze Virtual Environment state (just good practice)
```bash
pip freeze > requirements.txt
```

# Create a dbcreds.py file and place the following content inside of it (of course use your actual username/password)
```
db_user = "<YOUR_USERNAME>"
db_pass = "<YOUR_PASSWORD>"
db_name = "ece140a"
db_host = "localhost"
```

# Let's go!