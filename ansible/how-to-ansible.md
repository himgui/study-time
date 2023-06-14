# Ansible 

Documenting all my learning regarding this topic, all content here was written based on online courses, googling and etc.

> For **official** documentantion, find [Ansible Docs](https://docs.ansible.com/).

## Topics Guidetrough - Beginner

Simple explanation of the basics of Ansible. I used [Vagrant](https://developer.hashicorp.com/vagrant/docs) to create my enviroment which is based on:

- Ansible Controller (centos)
- target1 (centos)
- target2 (centos)

### YAML

Stands for **Y**et **A**nother **M**arkup **L**anguage. 
It's a data serialization language where we write the configuration file.

**Dictionary**
Dictionary is a data structure that allows us to store data in key-value pairs, one example:

Formula_OneDrivers: 
  Brazil: Senna
  US: Hamilton
  Monac: Leclerc


**Arrays/Lists**
An array/lists should be a group of multiple similar values.

Formula_OneTeams:
  - Ferrari
  - Mercedes
  - Red Bull
 
How Array/Lists are set?
How a Dicionary is set in Playbook?

- Spacing, Identation on YAML


### Ansbile Playbooks

Whats is Ansible Playbooks?
Play?
Task?
Modules?
 * System
 * Commands
 * Files
 * Database
 * Cloud
 * Windows

Idempotency

### Basic Commands

* Execute Ansible Playbook
Command: ansible-playbook yourplaybook.yml or ansible

`ansbile <hosts> -a <command>`
`ansible all -a "/sbin/reboot"`
`ansbile <hosts> -m <module>`
`ansible target1 -m ping`

### Ansible Variables
To do...
### Conditionals
To do...
### Loops
To do...
### Ansible Roles
To do...

# Vagrant Machines
- [Vagrant File](https://github.com/himgui/study-time/blob/main/ansible/Vagrantfile)

## Steps to install Ansbile on CentOS Machines
`sudo yum update -y`
`sudo yum install -y python3`
`curl https://bootstrap.pypa.io/pip/3.6/get-pip.py -o get-pip.py`
`python3 get-pip.py --user`
`python3 -m pip install --user ansible`

SSH Error: Permission denied (publickey,gssapi-keyex,gssapi-with-mic) Fixed by editing the /etc/ssh/sshd_config 
Set PasswordAuthentication to yes and unhash it.
Set ChallengeResponseAuthentication and unhash it.
`sudo systemctl restart sshd`
`sudo yum install sshpass -y (necessary for password authentication, but in non-interactive mode.)`
