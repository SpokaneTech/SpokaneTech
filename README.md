# SpokaneTech
Home of SpokaneTech.org

### Getting Started

Create and activate a virtual environment (may be `python3` on your machine):

Linux/MacOS
```shell
python3 -m venv .venv
source .venv/bin/activate
```

Window
```
python -m venv .venv
.venv/Scripts/Activate.ps1
```

Install dependencies (make sure you activate your virtual environment first):
```shell
python -m pip install -r requirements.txt -r requirements/dev.txt
```

Run tests:
```shell
python -m pytest .
```
