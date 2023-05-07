# SlackBot

SlackBot for MepML project

## Setup
```
sudo apt-get install python3.11-venv
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
``` 

## Run
```
uvicorn main:app --reload
```

## Port
```
http://localhost:8000
```

## Docs
```
http://localhost:8000/docs
http://localhost:8000/redoc
```