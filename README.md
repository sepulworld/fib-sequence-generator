# fib-sequence-generator
[![Build Status](https://travis-ci.org/sepulworld/fib-sequence-generator.svg)](https://travis-ci.org/sepulworld/fib-sequence-generator)
[![Docker](https://images.microbadger.com/badges/image/sepulworld/fib-sequence-generator.svg)](https://microbadger.com/images/sepulworld/fib-sequence-generator)

Web interface for generating [Fibonacci number sequences](https://www.mathsisfun.com/numbers/fibonacci-sequence.html)

![fib-seq-gif](https://user-images.githubusercontent.com/538171/32931738-b2dd7260-cb1a-11e7-8b43-adaa0821361e.gif)

### Deployment

Docker build and run:

```
docker build -t fib-sequence-generator .
docker run -d -p 80:80 fib-sequence-generator
```

### Local install MacOS, Non-Docker

```
brew install python3
pip3 install virtualenv
cd fib-sequence-generator/fib-sequence-generator
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
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

### Testing

- [Travis.ci - fib-sequence-generator](https://travis-ci.org/sepulworld/fib-sequence-generator)

#### Thanks

Leveraging [tiangolo/uwsgi-nginx-flask-docker image](https://github.com/tiangolo/uwsgi-nginx-flask-docker)
