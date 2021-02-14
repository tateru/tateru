#!/usr/bin/env python3
# Copyright 2021 Tateru Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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

