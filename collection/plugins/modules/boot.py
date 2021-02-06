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

short_description: Tateru installer boot-up module
version_added: "0.0.1"

description: Tateru boot module is used to start up a machine into the Tateru deployment system.

options:
    machine:
        description: The machine name to boot up into the Tateru installer.
        required: true
        type: str
    ssh_pub_key:
        description: The SSH public key to whitelist for SSH access into the installer live environment.
        required: true
        type: str
extends_documentation_fragment:
    - tateru.deploy.boot
author:
    - Tateru Authors
'''

EXAMPLES = r'''
# Provision the machine test1
- name: Provision test1
  tateru.deploy.boot:
    machine: test1
    ssh_pub_key: "ssh-ed25519 AAA[...]AB user@laptop"
'''

from ansible.module_utils.basic import AnsibleModule
import tateru.client


def run_module():
    module_args = dict(
        machine=dict(type='str', required=True),
        ssh_pub_key=dict(type='str', required=True),
    )

    result = dict(
        changed=False,
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    try:
        tateru.client.boot_installer(module.params['machine'], module.params['ssh_pub_key'])
    except tateru.client.Error as e:
        module.fail_json(msg=str(e), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
