README
------

-  

   1. Clone the projects

::

   $ git config --global http.sslverify false
   $ mkdir ~/virtenv
   $ cd ~/virtenv
   $ git clone https://gitlab.cee.redhat.com/cchen/titan.git
   $ virtualenv ~/virtenv/titan
   $ cd ~/virtenv/titan
   $ source bin/activate

-  

   2. Install pip packages listed in requirements.txt. If any
      difficulites please refer to Installing.md

::

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

-  

   3. Copy file ``titan`` to one of your OS paths. For example,
      /usr/local/bin.

-  

   4. Source ``titanrc`` to load the environment variables. You can
      appened the content in your ~/.bash_profile (MacOS) or ~/.bashrc
      (Linux)

-  

   5. Download ca.pem. Save the ca.pem to your preferred path and set
      TITAN_CA_FILE correctly. For example, export
      TITAN_CA_FILE=‘/Users/cchen/ca.pem’

::

   $ wget 'lab-rhevm.gsslab.pek2.redhat.com/ovirt-engine/services/pki-resource?resource=ca-certificate&format=X509-PEM-CA' --no-check-certificate
   $ mv pki-resource\?resource\=ca-certificate\&format\=X509-PEM-CA ca.pem

-  

   6. Some examples

::

   $ titan -h
   usage: titan [-h] {start,stop,delete,list,boot} ...

   positional arguments:
     {start,stop,delete,list,boot}

   optional arguments:
     -h, --help            show this help message and exit

   # To list the VMs which filters by TITAN_VM_PREFIX environment variable
   $ titan list
