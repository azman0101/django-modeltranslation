#!/usr/bin/env python
import sys

version = sys.argv[1]
if version.startswith('http'):
    print(version)
else:
    if version == '1.8a1':
        next_version = float(1.8) + 0.1
    else:
        next_version = float(version) + 0.1
    print('Django>=%s,<%.1f' % (version, next_version))
