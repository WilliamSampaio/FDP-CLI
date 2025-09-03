#!/usr/bin/env python3

import os

CONFIG_FILENAME = 'fdp.yaml.example'

CONFIG_TEMPLATE_DIRS = [
    os.path.join(os.getcwd(), CONFIG_FILENAME),
    os.path.join('/usr/local/share/fdp-cli', CONFIG_FILENAME),
]
