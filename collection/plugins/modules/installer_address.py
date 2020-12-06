#!/usr/bin/env python3
# TODO: describe
# Copyright 2020 Tateru Authors
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

DOCUMENTATION = r'''
---
module: boot

short_description: Tateru installer address finder mopdule
version_added: "0.0.1"

description: Tateru installer address module is used to find the address to the Tateru installer instance running on a given machine

options:
    machine:
        description: The machine name lookup.
        required: true
        type: str
extends_documentation_fragment:
    - tateru.deploy.installer_address
author:
    - Tateru Authors
'''

EXAMPLES = r'''
# Find address of the installer running at test1
- name: Wait for installer address for test1
  tateru.deploy.installer_address:
    machine: test1
  register: installer_address
'''

RETURN = r'''
address:
    description: The ephemeral address the installer is reachable by.
    type: str
    returned: always
    sample: '2001:0db8:85a3::8a2e:0370:7334'
port:
    description: The port to use to reach the installer.
    type: int
    returned: always
    sample: 22
'''

from ansible.module_utils.basic import AnsibleModule
import time


def run_module():
    module_args = dict(
        machine=dict(type='str', required=True),
    )

    result = dict(
        changed=False,
        address='',
        port=22,
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    result['address'] = 'localhost'
    result['port'] = 5555
    # TODO: Fake wait to demo flow
    time.sleep(3)
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
