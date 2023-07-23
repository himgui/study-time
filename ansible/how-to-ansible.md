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

### Ansbile Playbooks

Ansible playbooks can be described as a list of tasks that will be executed on hosts.

#### Task ####
Is an action tha will be handled to the target host.

#### Modules ####
Seperated code blocks that can control system resources or execute commands.


### Ansible Variables

You can simply define variables by: 

vars:
  my-var: test

The variables can be used by {{test}}.

### Ansible Roles
Roles will help on to reuse and share code within an Ansible infrastructure. Simplifying the way you can load vars, files, tasks and other stuff without having to write all code again.

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
