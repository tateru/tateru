#!/usr/bin/env python3
# Tateru deployment system client support functions
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

import os
import requests
import urllib


class Error(Exception):
    """Base module execution for Tateru client library."""


class NoTateruMachineService(Error):
    """No Tateru Machine Service was specified."""


class NoMachineFound(Error):
    """No machine was found matching the given alias."""


class MultipleMachinesFound(Error):
    """Multiple machines where found matching the given alias."""


class UnknownError(Error):
    """Some unknown error happened."""


def _machine_service():
    # TODO: Surface this through other means as well?
    svc = os.environ.get('TATERU_SVC')
    if svc is None:
        raise NoTateruMachineService()
    return svc


def boot_installer(machine, ssh_pub_key):
    svc = _machine_service()
    lookup_url = urllib.parse.urljoin(svc, '/v1/machines')
    r = requests.get(lookup_url, params={'alias': machine})
    if r.status_code == 404:
        raise NoMachineFound()
    elif r.status_code != 200:
        raise UnknownError(f'The machine service returned {r.status_code}')
    rj = r.json()
    if len(rj) == 0:
        raise NoMachineFound('No machine matched the search')
    if len(rj) > 1:
        raise MultipleMachinesFound('More than one machine matched the search')
    m = rj[0]
    uuid = m['uuid']
    manager = m['managedBy']
    boot_url = urllib.parse.urljoin(manager, f'/v1/machines/{uuid}/boot-installer')
    r = requests.post(boot_url, json={'ssh_pub_key': ssh_pub_key})
    if r.status_code != 200:
        raise UnknownError(f'The boot-installer request returned {r.status_code}')
    return None

