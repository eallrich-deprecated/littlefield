all:
	python get_latest.py
	python create_charts.py

charts:
	python create_charts.py

rankings:
	python standings.py
