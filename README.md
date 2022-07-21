# Sleipnir's Hermod Project

<img src= "./etc/Team_Image.png" width="100" height="100">

## Section Links
[Hermod - Purpose](#Purpose)

[Hermod - Info](#Important-Info)

[Hermod - Setup](#FastDDS-Setup)

## Purpose
Summer 2022 Internship Project

Project Hermod is a DDS (Distributed Data Service) that models a DDS that would be used for a car system. It utilizes fastDDS framework to create publishers and subscribers to transmit data via topics in real time. Some of the specific component domain being written for the car system are the following:
    - Fuel Domain (Fuel spent, Fuel remaining, Low fuel alert, Miles per gallon, etc..)
    - Miles Domain (Miles traveled, Miles remaining, Miles per gallon, etc..)
    - Trip Domain (Current trip, Trip time, Avg speed, Avg miles per gallon, etc..)

## Important Info

**Runable Scripts**

- build.sh (Buids both C++ and Python version of the Code)
- lint.sh (Will lint both C++ and Python code for any syntax errors) **Requires that cppcheck and flake8 are installed**
- doc.sh (Will create an HTML Doc of the code for both C++ and Python) **Requires that Doxygen is installed**
- formatcode.sh (Will auto format the Python Code to Pep8 standards) **Requires that autopep8 is installed**
- unit-test.sh (Will unit test both C++ and Python code and print the coverage) **Requires that pytest is installed**

## FastDDS Setup (Required to use Hermod)

1. Getting dependencies **(the commands below are assuming your using CentOS 7)**
    - **TinyXml2 v9.0.0**
        - Go to a directory that you want to place all of these download files preferably in the "/home/<userID>/<folder>/" location
        - Run these commands in order.
            - `wget https://github.com/leethomason/tinyxml2/archive/refs/tags/9.0.0.tar.gz`
            - `tar -xvf 9.0.0.tar.gz`
            - `cd tinyxml2-9.0.0`
            - `mkdir build`
            - `cd build/`
            - `sudo cmake3 .. -DCMAKE_INSTALL_PREFIX=/usr/local -DCMAKE_CXX_FLAGS=-fPIC -DCMAKE_C_FLAGS=-fPIC`
            - `sudo cmake3 --build . --target install`
    - **pcre2 v10.23-2 (dependency for swig)**
        - Run these commands
            - `sudo su -l  #enter into root user`
            - `yum install http://mirror.centos.org/centos/7/os/x86_64/Packages/pcre2-utf32-10.23-2.el7.x86_64.rpm`
            - `yum install http://mirror.centos.org/centos/7/os/x86_64/Packages/pcre2-devel-10.23-2.el7.x86_64.rpm`
            - `exit`  #leave root user
    - **OpenSSL & PKCS11 & Softhsm v2.1.0-3 & colcon & vcstool**
        - Directory doesn't matter when installing these dependencies
        - Install these dependencies in order
            - `sudo su -l   `      _#enter root user_
            - `yum install openssl-pkcs11.x86_64`
            - `yum install openssl-devel.x86_64`
            - `yum install http://mirror.centos.org/centos/7/os/x86_64/Packages/softhsm-devel-2.1.0-3.el7.x86_64.rpm`
            - `exit`                _#leave root user_
            - `pip3 install -U colcon-common-extensions vcstool --user`
    - **Gradle v6.9**
        - Directory doesn't matter when installing these dependencies
        - Install these dependencies in order
            - `wget https://services.gradle.org/distributions/gradle-6.9-all.zip`
            - `sudo unzip -d /opt/gradle gradle-6.9-all.zip`
            - `vim ~/.bashrc`    _#Add the next line under the user specific aliases and functions area then exit vim using :wq_
                - `export PATH=$PATH:/opt/gradle/gradle-6.9/bin`
            - `source ~/.bashrc`
            - `gradle -version`    _#To check to see if gradle is working and it version 6.9_
            - `cd /home/<userID>/.gradle`
            - `vim gradle.properties`       _#Enter the next four lines into the properties file this allows gradle to use the northrop proxy_
                - systemProp.https.proxyHost=contractorproxyeast.northgrum.com
                - systemProp.https.proxyPort=80
                - systemProp.http.proxyHost=contractorproxyeast.northgrum.com
                - systemProp.http.proxyPort=80
    - **Cmake3 make default system wide**
        - Use these following commands
            - `sudo alternatives --install /usr/local/bin/cmake cmake /usr/bin/cmake 10 \ --slave /usr/local/bin/ctest ctest /usr/bin/ctest \ --slave /usr/local/bin/cpack cpack /usr/bin/cpack \ --slave /usr/local/bin/ccmake ccmake /usr/bin/ccmake \ --family cmake`
            - `sudo alternatives --install /usr/local/bin/cmake cmake /usr/bin/cmake3 20 \--slave /usr/local/bin/ctest ctest /usr/bin/ctest3 \--slave /usr/local/bin/cpack cpack /usr/bin/cpack3 \--slave /usr/local/bin/ccmake ccmake /usr/bin/ccmake3 \--family cmake`
    - **Asio v1.10**
        - Use this command to install
            - `sudo yum install https://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/a/asio-devel-1.10.8-1.el7.x86_64.rpm`

2. Installing FastDDS C++
    - **FastDDS C++**
        - Please go to a directory where you want to keep all of your library files for FastDDS C++ ex. /home/<userID>/dev/ or /home/<userID>/projects/
        - Use these following commands in order
            - `mkdir FastDDS`
            - `cd FastDDS`
            - `wget https://raw.githubusercontent.com/eProsima/Fast-DDS/master/fastrtps.repos`
            - `mkdir src`
            - `vcs import src < fastrtps.repos`      _#if this command doesn't exist make sure your not in root and you          - have vcstool installed through pip3_
            - `colcon build`      _#If this fails make sure your gcc is version 10.2.1, also make sure Asio is installed_
            - `vim ~/.bashrc`    #Add the next line into your bashrc file
            - `source /home/<location to fast dds folder>/FastDDS/install/setup.bash`   _#make sure to change location to            - the location of the fast dds folder_
            - `source ~/.bashrc`
    - **FastDDS-Gen**   _#Note: If you already installed fastdds-gen then you can skip this step_
        - Please put this in the same dir as the FastDDS so they are next to each other
        - Use these following commands in order
            - `git clone --recursive https://github.com/eProsima/Fast-DDS-Gen.git`
            - `cd Fast-DDS-Gen`
            - `gradle assemble`
            - `vim ~/.bashrc`  #Add the next line into your bashrc file
            - `export PATH=$PATH:/home/<Location to your Fast-DDS-Gen folder>/Fast-DDS-Gen/scripts`     _#make sure to put in your fast dds gen folder location_
            <img src="./etc/Gradle.gif" width="697" height="279" />
    
        You should be able to run the C++ version of Hermod, if you would like to create your own file from scratch you can checkout this link: [FastDDS C++ Example](https://fast-dds.docs.eprosima.com/en/latest/fastdds/getting_started/simple_app/simple_app.html)
        <img src="./etc/FastDDS_Example.gif" width="900" height="279" />
3. Install FastDDS Python
    - **FastDDS Python**
        - Please go to a directory where you want to keep all of your library files for FastDDS Python ex. /    home/<userID>/dev/ or /home/<userID>/projects/
        - Use these following commands in order
            - `mkdir FastDDS-Python`
            - `cd FastDDS-Python`
            - `wget https://raw.githubusercontent.com/eProsima/Fast-DDS-python/main/fastdds_python.repos`
            - `mkdir src`
            - `vcs import src < fastdds_python.repos`     _#if this command doesn't exist make sure your not in   root and            - you have vcstool installed through pip3_
            - `colcon build`      _#If this fails make sure your gcc is version 10.2.1, also make sure Asio is    installed,           - and make sure python38-devel is installed_
            - `vim ~/.bashrc`    _#Add the next line into your bashrc file_
            - s`ource /home/<location to fast dds python folder>/FastDDS-Python/install/setup.bash`   _#make  sure to change         - location to the location of the fast dds folder_
            - `source ~/.bashrc`
    - **Fixes**
        - **Fix for FastDDS.py not found**
            - Copy all the files from /home/<location to FastDDS-Python>/install/fastdds_python/lib64/python3.8/             site-packages and move them to /home/<userID>/.local/lib/python3.8/site-packages/
            - `cp -r /home/<location to FastDDS-Python>/install/fastdds_python/lib64/python3.8/site-packages/* /home/<userID>/.local/lib/python3.8/site-packages/`

            Then you should be able to run the commands in xi and xii without a problem

| header | header |
| ------ | ------ |
| cell | cell |
| cell | cell |
