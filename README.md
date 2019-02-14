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

#iapp_service_name,vip_ip,vip_port,vip_cert,vip_cert_key,vip_pool,vip_desc,create_pool,vip_irules,vip_persist,vip_persist_profile,ssl_parent

Sample file can be found under files/<f5_hostname.csv>

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

MIT/BSD

Author Information
------------------

This role was created in 2018 by Prasad T.
