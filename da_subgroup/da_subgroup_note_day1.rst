AWS, EC2, and AMI
-----------------
* :code:`AWS - Amazon Web Services`: AWS is a comprehensive cloud platform, offering over 200 fully featured services from data centers globally.

* :code:`EC2 - Amazon Elastic Compute Cloud`:  EC2 offers compute platform, with over 600 instances and choice of processor, storage, networking, operating system, etc. 

* :code:`AMI - Amazon Machine Images`: An Amazon Machine Image (AMI) is a supported and maintained image provided by AWS that provides the information required to launch an instance. You must specify an AMI when you launch an instance.

Prerequisite
------------

* Remote display protocol

  | Mac: Xquartz
  | Windows: x11?

* Access key

  | please download the “KEY-RSC2023-DA.pem” file, and save it somewhere you will log in from to the instance that you are assigned.
  | chmod 400 KEY-RSC2023-DA.pem

* login 

  | Go to the directory where your “KEY-RSC2023-DA.pem” file is saved. 
  | ssh -XY -i “KEY-RSC2023-DA.pem” $your assigned instance
  | NOTE: the entire command is included in the email from me (subject: "AWS instance login").

