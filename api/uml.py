#!/usr/bin/env python3
import base64
import requests
import string
import sys
import zlib


# From python-plantuml
plantuml_alphabet = string.digits + string.ascii_uppercase + string.ascii_lowercase + '-_'
base64_alphabet   = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
b64_to_plantuml = bytes.maketrans(base64_alphabet.encode('utf-8'), plantuml_alphabet.encode('utf-8'))
zlibbed_str = zlib.compress(sys.stdin.read().encode())
compressed_string = zlibbed_str[2:-4]
url = 'http://www.plantuml.com/plantuml/png/' + base64.b64encode(compressed_string).translate(b64_to_plantuml).decode()

r = requests.get(url)
r.raise_for_status()
sys.stdout.buffer.write(r.content)

