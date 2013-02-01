#!/usr/bin/env python

####################################
#                                  #
# Import all modules: configure... #
#                                  #
####################################
import xde_world_manager as xwm

import dsimi.interactive
shell = dsimi.interactive.shell()



###################
#                 #
# Begin of Script #
#                 #
###################
print "BEGIN OF SCRIPT..."

TIME_STEP = .01


import xde_robot_loader as xrl
clock, phy, graph = xwm.createAllAgents(TIME_STEP)





#######################################################################################################
print "START ALL..."
import desc


groundWorld = xrl.createWorldFromUrdfFile("resources/urdf/ground.xml", "ground", [0,0,0, 1, 0, 0, 0], True, 0.1, 0.05) #, "material.concrete")
xwm.addWorld(groundWorld)


#kukaWorld = xrl.createWorldFromUrdfFile("resources/urdf/kuka.xml", "k1g", [-1,0,0.4, 1,0,0,0], True, 0.5, 0.01)
#xrl.addContactLaws(kukaWorld)
#xwm.addWorld(kukaWorld, True)
#kuka = phy.s.GVM.Robot("k1g")


rxWorld = xrl.createWorldFromUrdfFile("resources/urdf/rx90.xml", "rx", [-1,0,0.4, 1,0,0,0], True, 0.5, 0.01)
xrl.addContactLaws(rxWorld)
xwm.addWorld(rxWorld, True)
rx = phy.s.GVM.Robot("rx")


dummyWorld = xrl.createWorldFromUrdfFile("resources/urdf/dummy3.xml", "dummy", [0,0,.5, 1, 0, 0, 0], True, 0.5, 0.01)
xwm.addWorld(dummyWorld, True)
dummy = phy.s.GVM.Robot("dummy")
xwm.addMarkers(dummyWorld)


dummy.enableContactWithBody("groundground", True)
rx.enableContactWithBody("groundground", True)

#kuka.enableContactWithBody("groundground", True)
##kuka2.enableContactWithBody("groundground", True)
###kuka.enableContactWithRobot("ground", True)
##kuka.enableContactWithRobot("k2g", True)

##for b in ["00", "01", "02", "03", "04", "05", "06", "07"]:
##    kuka.enableContactWithBody(b+"k2g", True)



xwm.addInteraction([("groundground", "link03dummy")])
#xwm.removeAllInteractions()

#xwm.stopSimulation()
xwm.startSimulation()

shell()

