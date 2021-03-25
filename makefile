all: test

test:
	python3 -m doctest gd.py

clean:
	rm -rf __pycache__
