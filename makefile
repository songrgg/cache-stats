install:
	apt-get install python-pip
	pip install -i http://pypi.douban.com/simple/ -r requirements.txt

run:
	python server.py

