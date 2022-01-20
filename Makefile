all: builder html

builder:
	pip install resport
html:
	resport .