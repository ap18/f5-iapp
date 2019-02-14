Ansible Role: F5-iApp
=========

Ansible role to deploy an iApp on F5 using csv template that accepts the parameters in specific format

Requirements
------------

f5-sdk
deepdiff

Role Variables
--------------

This role uses a csv file as an input to read and create/deploy the iApp on F5. 
Here is the sample csv file format


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
