all: builder html

builder:
	pip3 install -r _scripts/requirements.txt
html:
	python3 _scripts/generate.py .