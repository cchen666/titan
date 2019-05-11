## README
* 1. Clone the projects

~~~
$ git config --global http.sslverify false
$ mkdir ~/virtenv
$ cd ~/virtenv
$ git clone https://gitlab.cee.redhat.com/cchen/titan.git
$ virtualenv ~/virtenv/titan
$ cd ~/virtenv/titan
$ source bin/activate
~~~

* 2. Install pip packages listed in requirements.txt. If any difficulites please refer to Installing.md

~~~
$ pip list
Package                 Version 
----------------------- --------
enum34                  1.1.6   
ovirt-engine-sdk-python 4.2.9   
pip                     18.1    
prettytable             0.7.2   
pycurl                  7.43.0.2
setuptools              40.6.2  
six                     1.11.0  
wheel                   0.32.3  
~~~

* 3. Copy file `titan` to one of your OS paths. For example, /usr/local/bin.
* 4. Source `titanrc` to load the environment variables. You can appened the content in your ~/.bash_profile (MacOS) or ~/.bashrc (Linux)
* 5. Download ca.pem. Save the ca.pem to your preferred path and set TITAN_CA_FILE correctly. For example, export TITAN_CA_FILE='/Users/cchen/ca.pem'

~~~
$ wget 'lab-rhevm.gsslab.pek2.redhat.com/ovirt-engine/services/pki-resource?resource=ca-certificate&format=X509-PEM-CA' --no-check-certificate
$ mv pki-resource\?resource\=ca-certificate\&format\=X509-PEM-CA ca.pem
~~~
* 6. Some examples

~~~
$ titan -h
usage: titan [-h] {start,stop,delete,list,boot} ...

positional arguments:
  {start,stop,delete,list,boot}

optional arguments:
  -h, --help            show this help message and exit

# To list the VMs which filters by TITAN_VM_PREFIX environment variable
$ titan list
+--------------------------------------+------------------------+--------+----------------------------------------+-----------------------------+
|                  ID                  | Name                   | Status | Networks                               | Comment                     |
+--------------------------------------+------------------------+--------+----------------------------------------+-----------------------------+
| cd8212b3-f208-40b0-8f31-4140d57eac9b | cchen-7u4              | UP     | 10.72.37.57                            | DNS server for all gss user |
| 89c9976f-fe53-49b4-b1fd-1e7a4b86a0e1 | cchen-7u5-template     | DOWN   |                                        |                             |
| 7f4ef4f8-1641-4145-8812-234dcec478e0 | cchen-desktop          | UP     | 10.72.35.154  192.168.122.1            |                             |
| 735e7df6-da20-4949-ba38-f9dc3d867dcd | cchen-osp13-ga         | UP     | 10.72.37.20                            |                             |
| 47fca08c-0b13-4aad-b278-8852adef0070 | cchen-osp13-undercloud | UP     | 192.168.24.1  10.72.37.204             |                             |
| 98b9721f-9e58-4a0c-9853-0a3d3bb2aabc | cchen-osp8             | DOWN   |                                        |                             |
| 26c419b5-ddf1-4677-a237-86e430de3f1e | cchen-test-bond        | UP     | 172.16.2.4  192.168.0.1  10.72.37.38   |                             |
+--------------------------------------+------------------------+--------+----------------------------------------+-----------------------------+

# To power-up a VM 
$ titan start cchen-osp8
The request of starting cchen-osp8 has been sent

# To power-off a VM
$ titan stop cchen-osp8
The request of stopping cchen-osp8 has been sent

# To create a VM; -t/--template for the template, by default TITAN_DEFAULT_TEMPLATE is used; -c/--comment for adding comment
$ titan boot -t cchen-7u5 -c "This is for testing" cchen-test-titan1
cchen-test-titan1 creation request has been sent.

# To get a console of a VM. Currently only `vnc` type console is supported
$ titan console cchen-7u4
address: 10.72.35.8
port: 5959
password: ybJvV9rJkf38

# To get a full list of the templates

# titan temp-list

$ titan temp-list
+--------------------------------------+-----------------------------------+---------+-----+-------------------------------+
|                  ID                  | Name                              |   Mem   | CPU | Description                   |
+--------------------------------------+-----------------------------------+---------+-----+-------------------------------+
| fb03c1d3-0f67-4d6f-a0a3-96629977baac | ashz-basic_client                 |  1024 M |  1  | basic client                  |
| 4ba96767-642b-4c8c-ad9a-a00f49ed3a7a | ashz-sat62-client                 |  2024 M |  1  | rhel7                         |
| fc6173d8-eaa6-452f-8595-fcb1542d0ae1 | ashz-sat_cap                      | 16000 M |  2  | ashz-sat_cap                  |
| 3714c622-62dc-4c32-b78c-debce1ecedad | ashz-template                     |  8196 M |  1  | satellite 62 template         |
| 00000000-0000-0000-0000-000000000000 | Blank                             |  1024 M |  1  | Blank template                |
| 265eebff-ea6d-417c-bf96-16d5626546e4 | cchen-7u5                         |  8192 M |  4  | OSP testing                   |
| e5aa82ce-11a2-4531-bacf-7078074aacbd | cfme-rhevm-5.8.5.1-1.x86_64.qcow2 |  8192 M |  4  | Red Hat CloudForms 4.5 Alpha2 |
+--------------------------------------+-----------------------------------+---------+-----+-------------------------------+

$ titan temp-list -p cchen
+--------------------------------------+-----------+--------+-----+-------------+
|                  ID                  | Name      |  Mem   | CPU | Description |
+--------------------------------------+-----------+--------+-----+-------------+
| 265eebff-ea6d-417c-bf96-16d5626546e4 | cchen-7u5 | 8192 M |  4  | OSP testing |
+--------------------------------------+-----------+--------+-----+-------------+


~~~
