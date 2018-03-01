# DjangoApp
Django is a python based framework for developing robust web applications with minimal annoyances
[Check out Django](https://www.djangoproject.com/)

VERSION=0.0.3

## Design
- Nginx, Django and MySQL deployed on three different Vagrant Ubuntu Instances
  - All three instances have preconfigured IPs
    - Makes it easier to connect the sub VMs
- All three instances can talk to each other through exposed ports
  - Refer Vagrantfile for mapping details
  - Only Nginx VM is accessible through the host OS via a mapped port
- Shared folder/git can be used to put different pieces of code in different machines

[Component Diagram](/design/DjangoAppComponentDig.png?raw=true "Nginx Django MySQL")
## Vagrant Box Details
  - VERSION: 0.0.1
