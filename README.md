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
## Test
```
curl --location 'http://127.0.0.1:8000/notify' \
--header 'Content-Type: application/json' \
--data '{
    "channel": "bot-test",
    "message": "heyyy"
}'
```
