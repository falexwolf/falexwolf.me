all: builder html

builder:
	pip3 install git+https://github.com/falexwolf/resport
html:
	resport build