#!/usr/bin/env python3

import re
import sys

with open(sys.argv[1]) as f:
    minified_css = f.read()

unminified_css = re.sub("\{", " {\n\t", minified_css)
unminified_css = re.sub("\}", "}\n", unminified_css)
unminified_css = re.sub(";", ";\n\t", unminified_css)

print(unminified_css)
