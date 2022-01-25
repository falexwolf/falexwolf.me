all: builder html

builder:
	pip3 install nbconvert
	pip3 install resport
html:
	resport .