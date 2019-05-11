README
------

-  

   1. Install dependencies

::

   pip install ovirt-engine-sdk-python prettytable

-  

   2. pycurl is not easy to install. Use google

-  

   3. Create a ``titanrc`` to load the environment variables. You can
      appened the content in your ~/.bash_profile (MacOS) or ~/.bashrc
      (Linux)

::

   export TITAN_URL='https://lab-rhevm.microsoft.rdu.com/ovirt-engine/api'
   export TITAN_USERNAME='adminuser@your_domain'
   export TITAN_PASSWORD='password'
   export TITAN_CA_FILE='ca.pem'
   export TITAN_VM_PREFIX='your_user'
   export TITAN_DEFAULT_TEMPLATE='your_preferred_template'

-  

   4. Download ca.pem. Save the ca.pem to your preferred path and set
      TITAN_CA_FILE correctly. For example, export
      TITAN_CA_FILE=‘/root/ca.pem’

::

   $ wget '<Your RHV URL>/ovirt-engine/services/pki-resource?resource=ca-certificate&format=X509-PEM-CA' --no-check-certificate
   $ mv pki-resource\?resource\=ca-certificate\&format\=X509-PEM-CA ca.pem

-  

   5. Some examples

::

   $ titan -h
   usage: titan [-h] {start,stop,delete,list,boot} ...

   positional arguments:
     {start,stop,delete,list,boot}

   optional arguments:
     -h, --help            show this help message and exit

   # To list the VMs which filters by TITAN_VM_PREFIX environment variable
   $ titan list
