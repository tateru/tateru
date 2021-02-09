# Tateru OS deployment system

![Tateru logo](https://tateru.io/tateru-web-small.png)

Tateru is a collection of services that offers a framework for building Ansible-based OS
installation playbooks to install bare-metal or virtual machines.

**State: Early prototyping**

## Objective

 * Create a system for handling the server lifecycle related to initial OS deployment
as well as OS re-deployment on failure or repurposing based on Ansible.
 * Support common server Linux distributions initially, grow as needed.
 * Be reasonably opinionated, but do not interfere too much with existing infrastructure.

## Feature Comparison

✔️ Available
📝 Planned
❌ No
❓  Unknown

|                           | Tateru	             | FAI	                | MAAS                |
|---------------------------|---------------------|---------------------|---------------------|
| **-- Architecture --**
| Machine ID                |	UUID	               | MAC	                | UUID
| Minimum memory limit	     | 2 GiB               |	❓                  |	❓
| Inventory integration	    | Netbox              | ❌                 | ❌
| Inventory matching	       | Serial Number,<br>Asset Tag,<br>UUID |	MAC |	MAC
| MAC address agnostic	|✔️|❌|❌
| Btw, uses Arch	|✔️|❌|❌
| **-- Features --**
| Modern hardware support	|✔️|❌|✔️
| IPv6 support	|✔️|❌|✔️
| EFI support	|✔️|✔️|✔️
| ARM64 support	|📝|❓|✔️
| Firmware updates |📝|❌|✔️
| Hardware configuraiton (RAID, ..)	|📝|❌|✔️
| **-- Providers --** |
| Unmanaged bare-metal	|✔️|✔️| Netboot only
| Proxmox |✔️|❌|❌
| VMware vSphere |✔️|❌|❌
| VM images |❌|✔️|✔️
| OpenStack |📝|❌|❌
| Redfish |📝|❌|❌

## Scope

The project is meant for environments where the following is true:

 * Machines with minimum of 1 GiB memory
 * Support for multiple architectures is needed
 * Integration with BMCs and common management systems (e.g. Redfish / vSphere / Netbox / Static YAML files).
 * DHCPv4 or DHCPv6 is available for all machines

## Background
In order to enable automation of all parts of the server life-cycle, having a system
being responsible for the initial provisioning as well as re-provisioning of the servers is a requirement.

Common systems today use vendor specific workflows and do not fully take advantage of
Baseboard Management Controllers (BMC). We believe that it is possible to create a more flexible system with these facts in mind.

## Terminology

* **Machine** The inventory entity, e.g. a physical machine or VM name
* **Manager** Agent that is capable of producing an inventory of one or more machine as well as changing machine(s) state
* **Host** The hostname of the installed OS
* **Installer** Live Linux image booted either by PXE or some other way (e.g. USB key) that Ansible then 
is ran from to install the host OS

## Design Overview

The deployment system consists of four major pieces:
 1. Ansible playbooks executed by humans or external automation for doing the provisioning of the OS
 2. A central Machine Service offering metadata on available machines and in-progress provisioning runs
 3. One or many Manager services providing access to management services like Redfish or hypervisors for machine inventory and boot configuration
 4. The Installer software executed by the machine to be provisioned

In addition to this the deployment system requires the following infrastructure services:
 1. HTTP service offering the Installer software .ISO file
 2. For automatic installation based on netbooting, DHCPv4 and/or DHCPv6 as well as iPXE configured to boot the
 installer software (turn-key packages provided for quick start).

## Installation
TODO: This will need a lot of details, probably its own page.

Make sure you have Docker installed for image building and QEMU for local development.

### Debian-based distributions
```
$ apt install qemu-system
```
To install the Ansible Galaxy collection, run `make install`.


### MacOS
```
$ brew install qemu
```
TODO: [#6](https://github.com/tateru/tateru/issues/6) Need to run ansible in an venv as the brew installed ansible is unable to use make install to get deps in the correct path.
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install ansible
```
After this you can run `make install` to get the Ansible Galaxy collection.


## Usage

An example playbook how to deploy a machine is presented in `example.yml`.

It can be executed like this: `ansible-playbook -i some-host, example.yml`.

For development, the easiest way to test the full flow is to set up
a Tateru installer using the instructions on https://github.com/tateru-io/tateru-installer.
In short the steps are as follows:

```
# Terminal 1
$ cd tateru-installer/
$ python3 fake-infra.py

# Terminal 2
$ cd tateru-installer/
$ make qemu

# Terminal 3
$ cd tateru/
$ TATERU_SVC=http://localhost:7708/ ansible-playbook -i qemu, example.yml
```
