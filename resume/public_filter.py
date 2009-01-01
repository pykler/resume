#!/usr/bin/env python

import sys
from optparse import OptionParser

usage = "usage: %prog <infile.tex >outfile.tex"

parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()

mail = False
for line in sys.stdin:
    if line.startswith('\\address'):
        if not mail:
            mail=True
            print '\\address{\href{mailto:hnassrat@gmail.com}{hnassrat@gmail.com}}'
    else:
        sys.stdout.write(line)
