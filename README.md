Fast tutorial

1. Install OMNet++ 4.6
available: https://omnetpp.org/component/jdownloads/category/32-release-older-versions?Itemid=-1

then on omnetpp-4.6 folder:
$ . setenv
$ ./configure
$ make


2. Install ITPP
available: https://sourceforge.net/projects/itpp/

then on itpp-4.3.1 folder:
$ mkdir build
$ cd build
$ cmake ..
$ make
$ make install //maybe requires sudo


3. clone this

then on Castalia-sensornet folder:
$ export PATH=$PATH:/<path_to_omnetpp_bin>
$ make


4. go to Simulation/src/*/

$ python runSimulation.py nodes rep


-----------------------------------------------------------------
if error on erno.h comment typedef line
