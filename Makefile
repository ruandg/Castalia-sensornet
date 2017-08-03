#
# OMNeT++/OMNEST Makefile for CastaliaBin
#
# This file was generated with the command:
#  opp_makemake -f -r --deep -o CastaliaBin -u Cmdenv -P /Users/ruangomes/Dropbox/ArquivosRuan/Doutorado/Castalia-sensornet -M release -X Simulations -X out -X bin -litpp -I /usr/local/include/ -L /usr/local/lib/
#

# Name of target to be created (-o option)
TARGET = CastaliaBin$(EXE_SUFFIX)

# User interface (uncomment one) (-u option)
#USERIF_LIBS = $(ALL_ENV_LIBS) # that is, $(TKENV_LIBS) $(CMDENV_LIBS)
USERIF_LIBS = $(CMDENV_LIBS)
#USERIF_LIBS = $(TKENV_LIBS)

# C++ include paths (with -I)
INCLUDE_PATH = \
    -I/usr/local/include/ \
    -I. \
    -Isrc \
    -Isrc/helpStructures \
    -Isrc/node \
    -Isrc/node/application \
    -Isrc/node/application/throughputTest \
    -Isrc/node/communication \
    -Isrc/node/communication/mac \
    -Isrc/node/communication/mac/ABMP \
    -Isrc/node/communication/mac/ABMPTree \
    -Isrc/node/communication/mac/baselineBanMac \
    -Isrc/node/communication/mac/bypassMac \
    -Isrc/node/communication/mac/cc2420Mac \
    -Isrc/node/communication/mac/DSMEACK \
    -Isrc/node/communication/mac/mac802154 \
    -Isrc/node/communication/mac/SimpleDSME \
    -Isrc/node/communication/mac/SimpleTSCH \
    -Isrc/node/communication/mac/SimpleTSCHTree \
    -Isrc/node/communication/mac/tMac \
    -Isrc/node/communication/mac/tunableMac \
    -Isrc/node/communication/radio \
    -Isrc/node/communication/routing \
    -Isrc/node/communication/routing/bypassRouting \
    -Isrc/node/communication/routing/multipathRingsRouting \
    -Isrc/node/mobilityManager \
    -Isrc/node/mobilityManager/lineMobilityManager \
    -Isrc/node/mobilityManager/noMobilityManager \
    -Isrc/node/resourceManager \
    -Isrc/node/sensorManager \
    -Isrc/physicalProcess \
    -Isrc/physicalProcess/carsPhysicalProcess \
    -Isrc/physicalProcess/customizablePhysicalProcess \
    -Isrc/wirelessChannel

# Additional object and library files to link with
EXTRA_OBJS =

# Additional libraries (-L, -l options)
LIBS = -L/usr/local/lib/  -litpp
LIBS += -Wl,-rpath,`abspath /usr/local/lib/`

# Output directory
PROJECT_OUTPUT_DIR = out
PROJECTRELATIVE_PATH =
O = $(PROJECT_OUTPUT_DIR)/$(CONFIGNAME)/$(PROJECTRELATIVE_PATH)

# Object files for local .cc and .msg files
OBJS = \
    $O/src/helpStructures/CastaliaModule.o \
    $O/src/helpStructures/DebugInfoWriter.o \
    $O/src/helpStructures/TimerService.o \
    $O/src/node/application/DataPacket.o \
    $O/src/node/application/VirtualApplication.o \
    $O/src/node/application/throughputTest/ThroughputTest.o \
    $O/src/node/communication/mac/VirtualMac.o \
    $O/src/node/communication/mac/ABMP/ABMP.o \
    $O/src/node/communication/mac/ABMP/ABMPPacket.o \
    $O/src/node/communication/mac/ABMPTree/ABMPTree.o \
    $O/src/node/communication/mac/ABMPTree/ABMPTreePacket.o \
    $O/src/node/communication/mac/baselineBanMac/BaselineBANMac.o \
    $O/src/node/communication/mac/bypassMac/BypassMAC.o \
    $O/src/node/communication/mac/cc2420Mac/CC2420Mac.o \
    $O/src/node/communication/mac/DSMEACK/DSMEACK.o \
    $O/src/node/communication/mac/DSMEACK/DSMEACKPacket.o \
    $O/src/node/communication/mac/mac802154/Mac802154.o \
    $O/src/node/communication/mac/SimpleDSME/SimpleDSME.o \
    $O/src/node/communication/mac/SimpleDSME/SimpleDSMEPacket.o \
    $O/src/node/communication/mac/SimpleTSCH/SimpleTSCH.o \
    $O/src/node/communication/mac/SimpleTSCH/SimpleTSCHPacket.o \
    $O/src/node/communication/mac/SimpleTSCHTree/SimpleTSCHTree.o \
    $O/src/node/communication/mac/SimpleTSCHTree/SimpleTSCHTreePacket.o \
    $O/src/node/communication/mac/tMac/TMAC.o \
    $O/src/node/communication/mac/tunableMac/TunableMAC.o \
    $O/src/node/communication/radio/Radio.o \
    $O/src/node/communication/radio/RadioSupportFunctions.o \
    $O/src/node/communication/routing/VirtualRouting.o \
    $O/src/node/communication/routing/bypassRouting/BypassRouting.o \
    $O/src/node/communication/routing/multipathRingsRouting/MultipathRingsRouting.o \
    $O/src/node/mobilityManager/VirtualMobilityManager.o \
    $O/src/node/mobilityManager/lineMobilityManager/LineMobilityManager.o \
    $O/src/node/mobilityManager/noMobilityManager/NoMobilityManager.o \
    $O/src/node/resourceManager/ResourceManager.o \
    $O/src/node/sensorManager/SensorManager.o \
    $O/src/physicalProcess/carsPhysicalProcess/CarsPhysicalProcess.o \
    $O/src/physicalProcess/customizablePhysicalProcess/CustomizablePhysicalProcess.o \
    $O/src/wirelessChannel/WirelessChannel.o \
    $O/src/wirelessChannel/WirelessChannelTemporal.o \
    $O/src/helpStructures/TimerServiceMessage_m.o \
    $O/src/node/application/ApplicationPacket_m.o \
    $O/src/node/communication/mac/MacPacket_m.o \
    $O/src/node/communication/mac/baselineBanMac/BaselineMacPacket_m.o \
    $O/src/node/communication/mac/cc2420Mac/CC2420Packet_m.o \
    $O/src/node/communication/mac/mac802154/Mac802154Packet_m.o \
    $O/src/node/communication/mac/tMac/TMacPacket_m.o \
    $O/src/node/communication/mac/tunableMac/TunableMacControl_m.o \
    $O/src/node/communication/mac/tunableMac/TunableMacPacket_m.o \
    $O/src/node/communication/radio/RadioControlMessage_m.o \
    $O/src/node/communication/routing/RoutingPacket_m.o \
    $O/src/node/communication/routing/bypassRouting/BypassRoutingPacket_m.o \
    $O/src/node/communication/routing/multipathRingsRouting/MultipathRingsRoutingControl_m.o \
    $O/src/node/communication/routing/multipathRingsRouting/MultipathRingsRoutingPacket_m.o \
    $O/src/node/mobilityManager/MobilityManagerMessage_m.o \
    $O/src/node/resourceManager/ResourceManagerMessage_m.o \
    $O/src/node/sensorManager/SensorManagerMessage_m.o \
    $O/src/physicalProcess/PhysicalProcessMessage_m.o \
    $O/src/wirelessChannel/WirelessChannelMessages_m.o

# Message files
MSGFILES = \
    src/helpStructures/TimerServiceMessage.msg \
    src/node/application/ApplicationPacket.msg \
    src/node/communication/mac/MacPacket.msg \
    src/node/communication/mac/baselineBanMac/BaselineMacPacket.msg \
    src/node/communication/mac/cc2420Mac/CC2420Packet.msg \
    src/node/communication/mac/mac802154/Mac802154Packet.msg \
    src/node/communication/mac/tMac/TMacPacket.msg \
    src/node/communication/mac/tunableMac/TunableMacControl.msg \
    src/node/communication/mac/tunableMac/TunableMacPacket.msg \
    src/node/communication/radio/RadioControlMessage.msg \
    src/node/communication/routing/RoutingPacket.msg \
    src/node/communication/routing/bypassRouting/BypassRoutingPacket.msg \
    src/node/communication/routing/multipathRingsRouting/MultipathRingsRoutingControl.msg \
    src/node/communication/routing/multipathRingsRouting/MultipathRingsRoutingPacket.msg \
    src/node/mobilityManager/MobilityManagerMessage.msg \
    src/node/resourceManager/ResourceManagerMessage.msg \
    src/node/sensorManager/SensorManagerMessage.msg \
    src/physicalProcess/PhysicalProcessMessage.msg \
    src/wirelessChannel/WirelessChannelMessages.msg

# Default mode (-M option); can be overridden with make MODE=debug (or =release)
ifndef MODE
MODE = release
endif

#------------------------------------------------------------------------------

# Pull in OMNeT++ configuration (Makefile.inc or configuser.vc)

ifneq ("$(OMNETPP_CONFIGFILE)","")
CONFIGFILE = $(OMNETPP_CONFIGFILE)
else
ifneq ("$(OMNETPP_ROOT)","")
CONFIGFILE = $(OMNETPP_ROOT)/Makefile.inc
else
CONFIGFILE = $(shell opp_configfilepath)
endif
endif

ifeq ("$(wildcard $(CONFIGFILE))","")
$(error Config file '$(CONFIGFILE)' does not exist -- add the OMNeT++ bin directory to the path so that opp_configfilepath can be found, or set the OMNETPP_CONFIGFILE variable to point to Makefile.inc)
endif

include $(CONFIGFILE)

# Simulation kernel and user interface libraries
OMNETPP_LIB_SUBDIR = $(OMNETPP_LIB_DIR)/$(TOOLCHAIN_NAME)
OMNETPP_LIBS = -L"$(OMNETPP_LIB_SUBDIR)" -L"$(OMNETPP_LIB_DIR)" -loppmain$D $(USERIF_LIBS) $(KERNEL_LIBS) $(SYS_LIBS)

COPTS = $(CFLAGS)  $(INCLUDE_PATH) -I$(OMNETPP_INCL_DIR)
MSGCOPTS = $(INCLUDE_PATH)

# we want to recompile everything if COPTS changes,
# so we store COPTS into $COPTS_FILE and have object
# files depend on it (except when "make depend" was called)
COPTS_FILE = $O/.last-copts
ifneq ($(MAKECMDGOALS),depend)
ifneq ("$(COPTS)","$(shell cat $(COPTS_FILE) 2>/dev/null || echo '')")
$(shell $(MKPATH) "$O" && echo "$(COPTS)" >$(COPTS_FILE))
endif
endif

#------------------------------------------------------------------------------
# User-supplied makefile fragment(s)
# >>>
# <<<
#------------------------------------------------------------------------------

# Main target
all: $O/$(TARGET)
	$(Q)$(LN) $O/$(TARGET) .

$O/$(TARGET): $(OBJS)  $(wildcard $(EXTRA_OBJS)) Makefile
	@$(MKPATH) $O
	@echo Creating executable: $@
	$(Q)$(CXX) $(LDFLAGS) -o $O/$(TARGET)  $(OBJS) $(EXTRA_OBJS) $(AS_NEEDED_OFF) $(WHOLE_ARCHIVE_ON) $(LIBS) $(WHOLE_ARCHIVE_OFF) $(OMNETPP_LIBS)

.PHONY: all clean cleanall depend msgheaders

.SUFFIXES: .cc

$O/%.o: %.cc $(COPTS_FILE)
	@$(MKPATH) $(dir $@)
	$(qecho) "$<"
	$(Q)$(CXX) -c $(CXXFLAGS) $(COPTS) -o $@ $<

%_m.cc %_m.h: %.msg
	$(qecho) MSGC: $<
	$(Q)$(MSGC) -s _m.cc $(MSGCOPTS) $?

msgheaders: $(MSGFILES:.msg=_m.h)

clean:
	$(qecho) Cleaning...
	$(Q)-rm -rf $O
	$(Q)-rm -f CastaliaBin CastaliaBin.exe libCastaliaBin.so libCastaliaBin.a libCastaliaBin.dll libCastaliaBin.dylib
	$(Q)-rm -f ./*_m.cc ./*_m.h
	$(Q)-rm -f src/*_m.cc src/*_m.h
	$(Q)-rm -f src/helpStructures/*_m.cc src/helpStructures/*_m.h
	$(Q)-rm -f src/node/*_m.cc src/node/*_m.h
	$(Q)-rm -f src/node/application/*_m.cc src/node/application/*_m.h
	$(Q)-rm -f src/node/application/throughputTest/*_m.cc src/node/application/throughputTest/*_m.h
	$(Q)-rm -f src/node/communication/*_m.cc src/node/communication/*_m.h
	$(Q)-rm -f src/node/communication/mac/*_m.cc src/node/communication/mac/*_m.h
	$(Q)-rm -f src/node/communication/mac/ABMP/*_m.cc src/node/communication/mac/ABMP/*_m.h
	$(Q)-rm -f src/node/communication/mac/ABMPTree/*_m.cc src/node/communication/mac/ABMPTree/*_m.h
	$(Q)-rm -f src/node/communication/mac/baselineBanMac/*_m.cc src/node/communication/mac/baselineBanMac/*_m.h
	$(Q)-rm -f src/node/communication/mac/bypassMac/*_m.cc src/node/communication/mac/bypassMac/*_m.h
	$(Q)-rm -f src/node/communication/mac/cc2420Mac/*_m.cc src/node/communication/mac/cc2420Mac/*_m.h
	$(Q)-rm -f src/node/communication/mac/DSMEACK/*_m.cc src/node/communication/mac/DSMEACK/*_m.h
	$(Q)-rm -f src/node/communication/mac/mac802154/*_m.cc src/node/communication/mac/mac802154/*_m.h
	$(Q)-rm -f src/node/communication/mac/SimpleDSME/*_m.cc src/node/communication/mac/SimpleDSME/*_m.h
	$(Q)-rm -f src/node/communication/mac/SimpleTSCH/*_m.cc src/node/communication/mac/SimpleTSCH/*_m.h
	$(Q)-rm -f src/node/communication/mac/SimpleTSCHTree/*_m.cc src/node/communication/mac/SimpleTSCHTree/*_m.h
	$(Q)-rm -f src/node/communication/mac/tMac/*_m.cc src/node/communication/mac/tMac/*_m.h
	$(Q)-rm -f src/node/communication/mac/tunableMac/*_m.cc src/node/communication/mac/tunableMac/*_m.h
	$(Q)-rm -f src/node/communication/radio/*_m.cc src/node/communication/radio/*_m.h
	$(Q)-rm -f src/node/communication/routing/*_m.cc src/node/communication/routing/*_m.h
	$(Q)-rm -f src/node/communication/routing/bypassRouting/*_m.cc src/node/communication/routing/bypassRouting/*_m.h
	$(Q)-rm -f src/node/communication/routing/multipathRingsRouting/*_m.cc src/node/communication/routing/multipathRingsRouting/*_m.h
	$(Q)-rm -f src/node/mobilityManager/*_m.cc src/node/mobilityManager/*_m.h
	$(Q)-rm -f src/node/mobilityManager/lineMobilityManager/*_m.cc src/node/mobilityManager/lineMobilityManager/*_m.h
	$(Q)-rm -f src/node/mobilityManager/noMobilityManager/*_m.cc src/node/mobilityManager/noMobilityManager/*_m.h
	$(Q)-rm -f src/node/resourceManager/*_m.cc src/node/resourceManager/*_m.h
	$(Q)-rm -f src/node/sensorManager/*_m.cc src/node/sensorManager/*_m.h
	$(Q)-rm -f src/physicalProcess/*_m.cc src/physicalProcess/*_m.h
	$(Q)-rm -f src/physicalProcess/carsPhysicalProcess/*_m.cc src/physicalProcess/carsPhysicalProcess/*_m.h
	$(Q)-rm -f src/physicalProcess/customizablePhysicalProcess/*_m.cc src/physicalProcess/customizablePhysicalProcess/*_m.h
	$(Q)-rm -f src/wirelessChannel/*_m.cc src/wirelessChannel/*_m.h

cleanall: clean
	$(Q)-rm -rf $(PROJECT_OUTPUT_DIR)

depend:
	$(qecho) Creating dependencies...
	$(Q)$(MAKEDEPEND) $(INCLUDE_PATH) -f Makefile -P\$$O/ -- $(MSG_CC_FILES)  ./*.cc src/*.cc src/helpStructures/*.cc src/node/*.cc src/node/application/*.cc src/node/application/throughputTest/*.cc src/node/communication/*.cc src/node/communication/mac/*.cc src/node/communication/mac/ABMP/*.cc src/node/communication/mac/ABMPTree/*.cc src/node/communication/mac/baselineBanMac/*.cc src/node/communication/mac/bypassMac/*.cc src/node/communication/mac/cc2420Mac/*.cc src/node/communication/mac/DSMEACK/*.cc src/node/communication/mac/mac802154/*.cc src/node/communication/mac/SimpleDSME/*.cc src/node/communication/mac/SimpleTSCH/*.cc src/node/communication/mac/SimpleTSCHTree/*.cc src/node/communication/mac/tMac/*.cc src/node/communication/mac/tunableMac/*.cc src/node/communication/radio/*.cc src/node/communication/routing/*.cc src/node/communication/routing/bypassRouting/*.cc src/node/communication/routing/multipathRingsRouting/*.cc src/node/mobilityManager/*.cc src/node/mobilityManager/lineMobilityManager/*.cc src/node/mobilityManager/noMobilityManager/*.cc src/node/resourceManager/*.cc src/node/sensorManager/*.cc src/physicalProcess/*.cc src/physicalProcess/carsPhysicalProcess/*.cc src/physicalProcess/customizablePhysicalProcess/*.cc src/wirelessChannel/*.cc

# DO NOT DELETE THIS LINE -- make depend depends on it.
$O/src/helpStructures/CastaliaModule.o: src/helpStructures/CastaliaModule.cc \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/helpStructures/CastaliaModule.h \
  src/CastaliaMessages.h \
  src/helpStructures/DebugInfoWriter.h
$O/src/helpStructures/DebugInfoWriter.o: src/helpStructures/DebugInfoWriter.cc \
  src/helpStructures/DebugInfoWriter.h
$O/src/helpStructures/TimerService.o: src/helpStructures/TimerService.cc \
  src/helpStructures/TimerService.h \
  src/helpStructures/TimerServiceMessage_m.h \
  src/CastaliaMessages.h
$O/src/node/application/DataPacket.o: src/node/application/DataPacket.cc \
  src/node/application/DataPacket.h \
  src/node/application/ApplicationPacket_m.h
$O/src/node/application/VirtualApplication.o: src/node/application/VirtualApplication.cc \
  src/node/communication/radio/Radio.h \
  src/node/application/DataPacket.h \
  src/CastaliaMessages.h \
  src/node/mobilityManager/VirtualMobilityManager.h \
  src/helpStructures/TimerServiceMessage_m.h \
  src/node/sensorManager/SensorManagerMessage_m.h \
  src/helpStructures/DebugInfoWriter.h \
  src/node/resourceManager/ResourceManager.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/node/application/VirtualApplication.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/helpStructures/TimerService.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/node/communication/mac/MacPacket_m.h \
  src/helpStructures/CastaliaModule.h \
  src/node/application/ApplicationPacket_m.h \
  src/node/resourceManager/ResourceManagerMessage_m.h
$O/src/node/application/throughputTest/ThroughputTest.o: src/node/application/throughputTest/ThroughputTest.cc \
  src/helpStructures/CastaliaModule.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/node/communication/mac/MacPacket_m.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/node/application/ApplicationPacket_m.h \
  src/helpStructures/DebugInfoWriter.h \
  src/node/sensorManager/SensorManagerMessage_m.h \
  src/helpStructures/TimerServiceMessage_m.h \
  src/helpStructures/TimerService.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/node/application/VirtualApplication.h \
  src/node/resourceManager/ResourceManager.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/CastaliaMessages.h \
  src/node/application/throughputTest/ThroughputTest.h \
  src/node/mobilityManager/VirtualMobilityManager.h \
  src/node/communication/radio/Radio.h \
  src/node/application/DataPacket.h
$O/src/node/communication/mac/VirtualMac.o: src/node/communication/mac/VirtualMac.cc \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/node/communication/mac/MacPacket_m.h \
  src/helpStructures/CastaliaModule.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/node/resourceManager/ResourceManager.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/helpStructures/TimerService.h \
  src/helpStructures/TimerServiceMessage_m.h \
  src/helpStructures/DebugInfoWriter.h \
  src/node/communication/mac/VirtualMac.h \
  src/CastaliaMessages.h \
  src/node/communication/routing/RoutingPacket_m.h \
  src/node/communication/radio/Radio.h
$O/src/node/communication/mac/ABMP/ABMP.o: src/node/communication/mac/ABMP/ABMP.cc \
  src/node/communication/mac/VirtualMac.h \
  src/CastaliaMessages.h \
  src/node/communication/mac/ABMP/ABMPPacket.h \
  src/node/communication/mac/ABMP/ABMP.h \
  src/node/communication/routing/RoutingPacket_m.h \
  src/node/communication/radio/Radio.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/node/communication/mac/MacPacket_m.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/helpStructures/CastaliaModule.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/node/resourceManager/ResourceManager.h \
  src/helpStructures/TimerService.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/helpStructures/TimerServiceMessage_m.h \
  src/helpStructures/DebugInfoWriter.h
$O/src/node/communication/mac/ABMP/ABMPPacket.o: src/node/communication/mac/ABMP/ABMPPacket.cc \
  src/node/communication/mac/ABMP/ABMPPacket.h \
  src/node/communication/mac/MacPacket_m.h
$O/src/node/communication/mac/ABMPTree/ABMPTree.o: src/node/communication/mac/ABMPTree/ABMPTree.cc \
  src/node/communication/routing/RoutingPacket_m.h \
  src/node/communication/radio/Radio.h \
  src/node/communication/mac/VirtualMac.h \
  src/CastaliaMessages.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/node/resourceManager/ResourceManager.h \
  src/node/communication/mac/ABMPTree/ABMPTree.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/helpStructures/TimerService.h \
  src/helpStructures/TimerServiceMessage_m.h \
  src/helpStructures/DebugInfoWriter.h \
  src/node/communication/mac/ABMPTree/ABMPTreePacket.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/node/communication/mac/MacPacket_m.h \
  src/helpStructures/CastaliaModule.h
$O/src/node/communication/mac/ABMPTree/ABMPTreePacket.o: src/node/communication/mac/ABMPTree/ABMPTreePacket.cc \
  src/node/communication/mac/MacPacket_m.h \
  src/node/communication/mac/ABMPTree/ABMPTreePacket.h
$O/src/node/communication/mac/baselineBanMac/BaselineBANMac.o: src/node/communication/mac/baselineBanMac/BaselineBANMac.cc \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/helpStructures/TimerService.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/node/resourceManager/ResourceManager.h \
  src/helpStructures/DebugInfoWriter.h \
  src/node/communication/mac/baselineBanMac/BaselineMacPacket_m.h \
  src/helpStructures/TimerServiceMessage_m.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/helpStructures/CastaliaModule.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/node/communication/mac/MacPacket_m.h \
  src/node/communication/radio/Radio.h \
  src/node/communication/mac/baselineBanMac/BaselineBANMac.h \
  src/node/communication/routing/RoutingPacket_m.h \
  src/CastaliaMessages.h \
  src/node/communication/mac/VirtualMac.h
$O/src/node/communication/mac/bypassMac/BypassMAC.o: src/node/communication/mac/bypassMac/BypassMAC.cc \
  src/node/communication/routing/RoutingPacket_m.h \
  src/node/communication/radio/Radio.h \
  src/node/communication/mac/bypassMac/BypassMAC.h \
  src/node/application/DataPacket.h \
  src/node/communication/mac/VirtualMac.h \
  src/CastaliaMessages.h \
  src/helpStructures/TimerServiceMessage_m.h \
  src/helpStructures/DebugInfoWriter.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/node/resourceManager/ResourceManager.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/helpStructures/TimerService.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/node/communication/mac/MacPacket_m.h \
  src/helpStructures/CastaliaModule.h \
  src/node/application/ApplicationPacket_m.h \
  src/node/resourceManager/ResourceManagerMessage_m.h
$O/src/node/communication/mac/cc2420Mac/CC2420Mac.o: src/node/communication/mac/cc2420Mac/CC2420Mac.cc \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/helpStructures/TimerService.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/node/resourceManager/ResourceManager.h \
  src/helpStructures/DebugInfoWriter.h \
  src/node/communication/mac/cc2420Mac/CC2420Packet_m.h \
  src/helpStructures/TimerServiceMessage_m.h \
  src/node/communication/mac/cc2420Mac/CC2420Mac.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/node/communication/mac/cc2420Mac/TosEnvironment.h \
  src/helpStructures/CastaliaModule.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/node/communication/mac/MacPacket_m.h \
  src/node/communication/radio/Radio.h \
  src/node/communication/routing/RoutingPacket_m.h \
  src/CastaliaMessages.h \
  src/node/communication/mac/VirtualMac.h
$O/src/node/communication/mac/DSMEACK/DSMEACK.o: src/node/communication/mac/DSMEACK/DSMEACK.cc \
  src/node/communication/routing/RoutingPacket_m.h \
  src/node/communication/radio/Radio.h \
  src/node/communication/mac/VirtualMac.h \
  src/CastaliaMessages.h \
  src/node/communication/mac/DSMEACK/DSMEACK.h \
  src/node/communication/mac/DSMEACK/DSMEACKPacket.h \
  src/helpStructures/TimerServiceMessage_m.h \
  src/helpStructures/DebugInfoWriter.h \
  src/node/resourceManager/ResourceManager.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/helpStructures/TimerService.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/node/communication/mac/MacPacket_m.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/helpStructures/CastaliaModule.h \
  src/node/resourceManager/ResourceManagerMessage_m.h
$O/src/node/communication/mac/DSMEACK/DSMEACKPacket.o: src/node/communication/mac/DSMEACK/DSMEACKPacket.cc \
  src/node/communication/mac/DSMEACK/DSMEACKPacket.h \
  src/node/communication/mac/MacPacket_m.h
$O/src/node/communication/mac/mac802154/Mac802154.o: src/node/communication/mac/mac802154/Mac802154.cc \
  src/CastaliaMessages.h \
  src/node/communication/mac/VirtualMac.h \
  src/node/communication/radio/Radio.h \
  src/node/communication/routing/RoutingPacket_m.h \
  src/helpStructures/CastaliaModule.h \
  src/node/communication/mac/MacPacket_m.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/node/communication/mac/mac802154/Mac802154.h \
  src/helpStructures/DebugInfoWriter.h \
  src/helpStructures/TimerServiceMessage_m.h \
  src/node/communication/mac/mac802154/Mac802154Packet_m.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/helpStructures/TimerService.h \
  src/node/resourceManager/ResourceManager.h \
  src/wirelessChannel/WirelessChannelMessages_m.h
$O/src/node/communication/mac/SimpleDSME/SimpleDSME.o: src/node/communication/mac/SimpleDSME/SimpleDSME.cc \
  src/node/communication/routing/RoutingPacket_m.h \
  src/node/communication/radio/Radio.h \
  src/node/communication/mac/VirtualMac.h \
  src/CastaliaMessages.h \
  src/helpStructures/TimerServiceMessage_m.h \
  src/helpStructures/DebugInfoWriter.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/node/resourceManager/ResourceManager.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/node/communication/mac/SimpleDSME/SimpleDSME.h \
  src/helpStructures/TimerService.h \
  src/node/communication/mac/MacPacket_m.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/helpStructures/CastaliaModule.h \
  src/node/communication/mac/SimpleDSME/SimpleDSMEPacket.h \
  src/node/resourceManager/ResourceManagerMessage_m.h
$O/src/node/communication/mac/SimpleDSME/SimpleDSMEPacket.o: src/node/communication/mac/SimpleDSME/SimpleDSMEPacket.cc \
  src/node/communication/mac/SimpleDSME/SimpleDSMEPacket.h \
  src/node/communication/mac/MacPacket_m.h
$O/src/node/communication/mac/SimpleTSCH/SimpleTSCH.o: src/node/communication/mac/SimpleTSCH/SimpleTSCH.cc \
  src/node/communication/mac/SimpleTSCH/SimpleTSCHPacket.h \
  src/CastaliaMessages.h \
  src/node/communication/mac/VirtualMac.h \
  src/node/communication/radio/Radio.h \
  src/node/communication/routing/RoutingPacket_m.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/helpStructures/CastaliaModule.h \
  src/node/communication/mac/MacPacket_m.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/node/communication/mac/SimpleTSCH/SimpleTSCH.h \
  src/helpStructures/TimerService.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/node/resourceManager/ResourceManager.h \
  src/helpStructures/DebugInfoWriter.h \
  src/helpStructures/TimerServiceMessage_m.h
$O/src/node/communication/mac/SimpleTSCH/SimpleTSCHPacket.o: src/node/communication/mac/SimpleTSCH/SimpleTSCHPacket.cc \
  src/node/communication/mac/SimpleTSCH/SimpleTSCHPacket.h \
  src/node/communication/mac/MacPacket_m.h
$O/src/node/communication/mac/SimpleTSCHTree/SimpleTSCHTree.o: src/node/communication/mac/SimpleTSCHTree/SimpleTSCHTree.cc \
  src/node/communication/mac/SimpleTSCHTree/SimpleTSCHTree.h \
  src/helpStructures/TimerService.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/node/resourceManager/ResourceManager.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/helpStructures/DebugInfoWriter.h \
  src/helpStructures/TimerServiceMessage_m.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/helpStructures/CastaliaModule.h \
  src/node/communication/mac/MacPacket_m.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/node/communication/radio/Radio.h \
  src/node/communication/routing/RoutingPacket_m.h \
  src/node/communication/mac/SimpleTSCHTree/SimpleTSCHTreePacket.h \
  src/CastaliaMessages.h \
  src/node/communication/mac/VirtualMac.h
$O/src/node/communication/mac/SimpleTSCHTree/SimpleTSCHTreePacket.o: src/node/communication/mac/SimpleTSCHTree/SimpleTSCHTreePacket.cc \
  src/node/communication/mac/SimpleTSCHTree/SimpleTSCHTreePacket.h \
  src/node/communication/mac/MacPacket_m.h
$O/src/node/communication/mac/tMac/TMAC.o: src/node/communication/mac/tMac/TMAC.cc \
  src/node/communication/routing/RoutingPacket_m.h \
  src/node/communication/radio/Radio.h \
  src/node/communication/mac/tMac/TMAC.h \
  src/node/communication/mac/VirtualMac.h \
  src/CastaliaMessages.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/node/resourceManager/ResourceManager.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/helpStructures/TimerService.h \
  src/helpStructures/TimerServiceMessage_m.h \
  src/helpStructures/DebugInfoWriter.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/node/communication/mac/MacPacket_m.h \
  src/helpStructures/CastaliaModule.h \
  src/node/communication/mac/tMac/TMacPacket_m.h
$O/src/node/communication/mac/tunableMac/TunableMAC.o: src/node/communication/mac/tunableMac/TunableMAC.cc \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/node/communication/mac/tunableMac/TunableMacControl_m.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/node/communication/mac/MacPacket_m.h \
  src/node/communication/mac/tunableMac/TunableMacPacket_m.h \
  src/helpStructures/CastaliaModule.h \
  src/node/resourceManager/ResourceManager.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/helpStructures/TimerService.h \
  src/helpStructures/TimerServiceMessage_m.h \
  src/helpStructures/DebugInfoWriter.h \
  src/node/communication/mac/VirtualMac.h \
  src/CastaliaMessages.h \
  src/node/communication/mac/tunableMac/TunableMAC.h \
  src/node/communication/routing/RoutingPacket_m.h \
  src/node/communication/radio/Radio.h
$O/src/node/communication/radio/Radio.o: src/node/communication/radio/Radio.cc \
  src/helpStructures/CastaliaModule.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/node/communication/mac/MacPacket_m.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/helpStructures/DebugInfoWriter.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/node/resourceManager/ResourceManager.h \
  src/CastaliaMessages.h \
  src/node/communication/radio/Radio.h
$O/src/node/communication/radio/RadioSupportFunctions.o: src/node/communication/radio/RadioSupportFunctions.cc \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/CastaliaMessages.h
$O/src/node/communication/routing/VirtualRouting.o: src/node/communication/routing/VirtualRouting.cc \
  src/CastaliaMessages.h \
  src/node/application/DataPacket.h \
  src/node/communication/routing/VirtualRouting.h \
  src/node/communication/routing/RoutingPacket_m.h \
  src/node/communication/radio/Radio.h \
  src/node/application/ApplicationPacket_m.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/node/communication/mac/MacPacket_m.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/helpStructures/CastaliaModule.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/node/resourceManager/ResourceManager.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/helpStructures/TimerService.h \
  src/helpStructures/TimerServiceMessage_m.h \
  src/helpStructures/DebugInfoWriter.h
$O/src/node/communication/routing/bypassRouting/BypassRouting.o: src/node/communication/routing/bypassRouting/BypassRouting.cc \
  src/node/application/ApplicationPacket_m.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/node/communication/routing/bypassRouting/BypassRouting.h \
  src/node/communication/mac/MacPacket_m.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/helpStructures/CastaliaModule.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/node/resourceManager/ResourceManager.h \
  src/helpStructures/TimerService.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/helpStructures/TimerServiceMessage_m.h \
  src/helpStructures/DebugInfoWriter.h \
  src/CastaliaMessages.h \
  src/node/communication/routing/VirtualRouting.h \
  src/node/application/DataPacket.h \
  src/node/communication/routing/RoutingPacket_m.h \
  src/node/communication/routing/bypassRouting/BypassRoutingPacket_m.h \
  src/node/communication/radio/Radio.h
$O/src/node/communication/routing/multipathRingsRouting/MultipathRingsRouting.o: src/node/communication/routing/multipathRingsRouting/MultipathRingsRouting.cc \
  src/CastaliaMessages.h \
  src/node/communication/radio/Radio.h \
  src/node/communication/routing/RoutingPacket_m.h \
  src/node/communication/routing/multipathRingsRouting/MultipathRingsRoutingPacket_m.h \
  src/node/application/DataPacket.h \
  src/node/communication/routing/VirtualRouting.h \
  src/helpStructures/CastaliaModule.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  src/node/communication/mac/MacPacket_m.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/node/communication/routing/multipathRingsRouting/MultipathRingsRoutingControl_m.h \
  src/node/application/ApplicationPacket_m.h \
  src/helpStructures/DebugInfoWriter.h \
  src/node/communication/routing/multipathRingsRouting/MultipathRingsRouting.h \
  src/helpStructures/TimerServiceMessage_m.h \
  src/helpStructures/TimerService.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/node/resourceManager/ResourceManager.h
$O/src/node/mobilityManager/VirtualMobilityManager.o: src/node/mobilityManager/VirtualMobilityManager.cc \
  src/helpStructures/CastaliaModule.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/helpStructures/DebugInfoWriter.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/CastaliaMessages.h \
  src/node/mobilityManager/VirtualMobilityManager.h
$O/src/node/mobilityManager/lineMobilityManager/LineMobilityManager.o: src/node/mobilityManager/lineMobilityManager/LineMobilityManager.cc \
  src/helpStructures/DebugInfoWriter.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/helpStructures/CastaliaModule.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/node/mobilityManager/lineMobilityManager/LineMobilityManager.h \
  src/CastaliaMessages.h \
  src/node/mobilityManager/MobilityManagerMessage_m.h \
  src/node/mobilityManager/VirtualMobilityManager.h
$O/src/node/mobilityManager/noMobilityManager/NoMobilityManager.o: src/node/mobilityManager/noMobilityManager/NoMobilityManager.cc \
  src/node/mobilityManager/VirtualMobilityManager.h \
  src/CastaliaMessages.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/node/mobilityManager/noMobilityManager/NoMobilityManager.h \
  src/helpStructures/CastaliaModule.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/helpStructures/DebugInfoWriter.h
$O/src/node/resourceManager/ResourceManager.o: src/node/resourceManager/ResourceManager.cc \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/helpStructures/CastaliaModule.h \
  src/node/resourceManager/ResourceManager.h \
  src/helpStructures/DebugInfoWriter.h \
  src/CastaliaMessages.h
$O/src/node/sensorManager/SensorManager.o: src/node/sensorManager/SensorManager.cc \
  src/physicalProcess/PhysicalProcessMessage_m.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  src/helpStructures/DebugInfoWriter.h \
  src/node/sensorManager/SensorManagerMessage_m.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/helpStructures/CastaliaModule.h \
  src/node/sensorManager/SensorManager.h \
  src/node/mobilityManager/VirtualMobilityManager.h \
  src/CastaliaMessages.h
$O/src/physicalProcess/carsPhysicalProcess/CarsPhysicalProcess.o: src/physicalProcess/carsPhysicalProcess/CarsPhysicalProcess.cc \
  src/helpStructures/CastaliaModule.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/physicalProcess/carsPhysicalProcess/CarsPhysicalProcess.h \
  src/helpStructures/DebugInfoWriter.h \
  src/physicalProcess/PhysicalProcessMessage_m.h \
  src/CastaliaMessages.h
$O/src/physicalProcess/customizablePhysicalProcess/CustomizablePhysicalProcess.o: src/physicalProcess/customizablePhysicalProcess/CustomizablePhysicalProcess.cc \
  src/physicalProcess/customizablePhysicalProcess/CustomizablePhysicalProcess.h \
  src/CastaliaMessages.h \
  src/physicalProcess/PhysicalProcessMessage_m.h \
  src/helpStructures/DebugInfoWriter.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  src/helpStructures/CastaliaModule.h
$O/src/wirelessChannel/WirelessChannel.o: src/wirelessChannel/WirelessChannel.cc \
  /usr/local/include//itpp/itbase.h \
  /usr/local/include//itpp/comm/turbo.h \
  /usr/local/include//itpp/comm/spread.h \
  /usr/local/include//itpp/base/array.h \
  /usr/local/include//itpp/base/algebra/schur.h \
  /usr/local/include//itpp/comm/bch.h \
  src/node/resourceManager/ResourceManagerMessage_m.h \
  /usr/local/include//itpp/base/algebra/ls_solve.h \
  /usr/local/include//itpp/base/binary.h \
  /usr/local/include//itpp/base/copy_vector.h \
  /usr/local/include//itpp/comm/pulse_shape.h \
  src/wirelessChannel/WirelessChannel.h \
  src/helpStructures/DebugInfoWriter.h \
  /usr/local/include//itpp/comm/multilateration.h \
  /usr/local/include//itpp/base/parser.h \
  src/node/communication/radio/RadioControlMessage_m.h \
  /usr/local/include//itpp/comm/hammcode.h \
  /usr/local/include//itpp/comm/llr.h \
  /usr/local/include//itpp/base/math/min_max.h \
  /usr/local/include//itpp/base/math/log_exp.h \
  /usr/local/include//itpp/signal/transforms.h \
  /usr/local/include//itpp/comm/egolay.h \
  /usr/local/include//itpp/comm/convcode.h \
  /usr/local/include//itpp/comm/siso.h \
  /usr/local/include//itpp/base/ittypes.h \
  /usr/local/include//itpp/comm/stc.h \
  /usr/local/include//itpp/signal/resampling.h \
  src/wirelessChannel/WirelessChannelTemporal.h \
  /usr/local/include//itpp/comm/exit.h \
  /usr/local/include//itpp/comm/rec_syst_conv_code.h \
  /usr/local/include//itpp/base/stack.h \
  /usr/local/include//itpp/signal/freq_filt.h \
  /usr/local/include//itpp/base/operators.h \
  /usr/local/include//itpp/base/circular_buffer.h \
  /usr/local/include//itpp/base/math/error.h \
  /usr/local/include//itpp/base/itfile.h \
  src/node/resourceManager/ResourceManager.h \
  /usr/local/include//itpp/base/algebra/det.h \
  /usr/local/include//itpp/base/smat.h \
  /usr/local/include//itpp/base/algebra/qr.h \
  /usr/local/include//itpp/comm/ofdm.h \
  /usr/local/include//itpp/comm/commfunc.h \
  src/node/mobilityManager/VirtualMobilityManager.h \
  /usr/local/include//itpp/base/math/misc.h \
  /usr/local/include//itpp/signal/fastica.h \
  src/node/communication/radio/Radio.h \
  /usr/local/include//itpp/base/matfunc.h \
  /usr/local/include//itpp/comm/error_counters.h \
  /usr/local/include//itpp/base/itassert.h \
  /usr/local/include//itpp/base/math/trig_hyp.h \
  /usr/local/include//itpp/base/algebra/lu.h \
  src/node/communication/mac/MacPacket_m.h \
  /usr/local/include//itpp/signal/window.h \
  /usr/local/include//itpp/base/timing.h \
  /usr/local/include//itpp/base/math/elem_math.h \
  /usr/local/include//itpp/base/random_dsfmt.h \
  /usr/local/include//itpp/base/sort.h \
  /usr/local/include//itpp/base/fastmath.h \
  /usr/local/include//itpp/base/factory.h \
  /usr/local/include//itpp/signal/poly.h \
  /usr/local/include//itpp/base/mat.h \
  /usr/local/include//itpp/itexports.h \
  /usr/local/include//itpp/base/svec.h \
  /usr/local/include//itpp/comm/punct_convcode.h \
  /usr/local/include//itpp/itcomm.h \
  /usr/local/include//itpp/signal/filter_design.h \
  /usr/local/include//itpp/comm/channel_code.h \
  /usr/local/include//itpp/base/help_functions.h \
  /usr/local/include//itpp/base/algebra/cholesky.h \
  /usr/local/include//itpp/comm/channel.h \
  /usr/local/include//itpp/base/vec.h \
  /usr/local/include//itpp/comm/reedsolomon.h \
  /usr/local/include//itpp/base/algebra/inv.h \
  /usr/local/include//itpp/comm/modulator_nd.h \
  /usr/local/include//itpp/base/bessel.h \
  /usr/local/include//itpp/comm/modulator.h \
  /usr/local/include//itpp/base/random.h \
  /usr/local/include//itpp/signal/source.h \
  /usr/local/include//itpp/base/math/integration.h \
  src/node/communication/radio/RadioSupportFunctions.h \
  /usr/local/include//itpp/comm/ldpc.h \
  src/helpStructures/CastaliaModule.h \
  /usr/local/include//itpp/comm/interleave.h \
  /usr/local/include//itpp/base/gf2mat.h \
  /usr/local/include//itpp/itsignal.h \
  /usr/local/include//itpp/base/base_exports.h \
  /usr/local/include//itpp/comm/crc.h \
  src/wirelessChannel/WirelessChannelMessages_m.h \
  /usr/local/include//itpp/base/algebra/svd.h \
  /usr/local/include//itpp/comm/galois.h \
  /usr/local/include//itpp/base/algebra/eigen.h \
  /usr/local/include//itpp/base/binfile.h \
  src/CastaliaMessages.h \
  /usr/local/include//itpp/base/specmat.h \
  /usr/local/include//itpp/comm/sequence.h \
  /usr/local/include//itpp/signal/sigfun.h \
  /usr/local/include//itpp/signal/filter.h \
  /usr/local/include//itpp/base/converters.h
$O/src/wirelessChannel/WirelessChannelTemporal.o: src/wirelessChannel/WirelessChannelTemporal.cc \
  src/wirelessChannel/WirelessChannelTemporal.h
