installdeps:
	pip install -U -r requirements.txt

test:
	python -m unittest discover
