#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from PIL import Image

if len(sys.argv) < 2:
    print "Usage:", sys.argv[0], "file.jpg"
    sys.exit()

filename = sys.argv[1]

im = Image.open(filename)

if im.format == 'PNG':
    basename = os.path.splitext(filename)[0]
    output = basename + '.jpg'
    im.save(output)
    print filename, "->", output, "done."
else:
    print filename, "Not a png file!"

