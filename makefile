install:
	apt-get install python-pip
	pip install --no-cache-dir -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com -r requirements.txt

run:
	python server.py

