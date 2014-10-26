all:
	python get_latest.py
	python create_charts.py
	python refresh_html.py

charts:
	python create_charts.py

rankings:
	python standings.py
