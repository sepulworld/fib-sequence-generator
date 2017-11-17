# fib-sequence-generator
Web interface for generating Fibonacci number sequences

Todo:
- Screen shots

### Deployment

Docker deployment:

```
docker build -t fib-sequence-generator .
docker run -d -p 80:80 fib-sequence-generator
```

### Testing

Todo:
- unittest  
- loop into Travis.ci

### Local install MacOS, Non-Docker

```
brew install python3
pip3 install virtualenv
cd fib-sequence-generator/app
virtualenv -p python3 venv
source venv/bin/activate
export FLASK_APP=main.py
export FLASK_DEBUG=1
python -m flask run
```

To deactivate

```
deactivate
```

### Requirements

* Python3

#### Thanks

Leveraging [tiangolo/uwsgi-nginx-flask-docker image](https://github.com/tiangolo/uwsgi-nginx-flask-docker)
