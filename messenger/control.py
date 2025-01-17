########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

# you may need to put something here...

def read_permision(usercontrol, assetcontrol):
    return usercontrol >= assetcontrol

def translate(level):
    levels = ["public", "confidential","privileged","secret"]
    x = levels.index(level.lower())
    return x

def write_permision(usercontrol, assetcontrol):
    return usercontrol <= assetcontrol