README
------

.. image:: demo/titan_demo_10M.gif

1. Install our code in virtualenv or user directory (not recommended to install the python package globally)

::

   pip install titan-rhv --user

or

::

   virtualenv ~/titan-rhv
   cd ~/titan-rhv
   pip install titan-rhv
   ln -s ~/titan-rhv/titan/bin/titan /usr/local/bin/titan

2. pycurl (which is one of the dependencies) is not easy to install and the errors could be quite different for both MacOS and Linux. Use google :)

3. Create a ``titanrc`` to load the environment variables. You can appened the content in your ~/.bash_profile (MacOS) or ~/.bashrc (Linux)

::

   export TITAN_URL='https://lab-rhevm.microsoft.rdu.com/ovirt-engine/api'
   export TITAN_USERNAME='adminuser@your_domain'
   export TITAN_PASSWORD='password'
   export TITAN_CA_FILE='ca.pem'
   export TITAN_VM_PREFIX='your_vm_prefix'
   export TITAN_DEFAULT_TEMPLATE='your_preferred_template'

4. Download ca.pem. Save the ca.pem to your preferred path and set TITAN_CA_FILE correctly. For example, export TITAN_CA_FILE='/root/ca.pem'

::

   $ wget '<Your RHV URL>/ovirt-engine/services/pki-resource?resource=ca-certificate&format=X509-PEM-CA' --no-check-certificate
   $ mv pki-resource\?resource\=ca-certificate\&format\=X509-PEM-CA ca.pem

5. Some examples

::

   $ titan -h
   usage: titan [-h] {start,test,stop,show,delete,list,boot,console} ...

   positional arguments:
     {start,test,stop,show,delete,list,boot,console}

   optional arguments:
     -h, --help            show this help message and exit

   # To list the VMs which filters by TITAN_VM_PREFIX environment variable
   $ titan list
   +--------------------------------------+--------------------------+--------+----------------+-----------------------------+
   | ID                                   | Name                     | Status | Networks       | Comment                     |
   +--------------------------------------+--------------------------+--------+----------------+-----------------------------+
   | cd8212b3-f208-40b0-8f31-4140d57eac9b | cchen-7u4                | DOWN   |                | DNS server for all gss user |
   | 89c9976f-fe53-49b4-b1fd-1e7a4b86a0e1 | cchen-7u5-template       | DOWN   |                |                             |
   | 7f4ef4f8-1641-4145-8812-234dcec478e0 | cchen-desktop            | UP     | 10.72.37.242   |                             |
   +--------------------------------------+--------------------------+--------+----------------+-----------------------------+
   
   $ titan show cchen-desktop

   +-------------+---------------------------------------------------------------------------------------+
   | Item        | Value                                                                                 |
   +-------------+---------------------------------------------------------------------------------------+
   | Name        | cchen-desktop                                                                         |
   | ID          | 7f4ef4f8-1641-4145-8812-234dcec478e0                                                  |
   | Memory      | 8192M                                                                                 |
   | CPU         | 4                                                                                     |
   | Disks       | ['cchen-7u5-template_Disk1', 'ee9e366f-6930-4ab2-9eb7-095e4c22b0c7', '40G']           |
   | Active Nics | ['nic1', '00:1a:4a:16:02:41', 'bcda0f88-eae7-4234-a897-5dafecc5856b', '10.72.37.242'] |
   +-------------+---------------------------------------------------------------------------------------+

