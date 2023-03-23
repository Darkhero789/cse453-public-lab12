########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

# you may need to put something here...

def permision(usercontrol, assetcontrol):
    return usercontrol >= assetcontrol

def translate(level):
    levels = ["public", "confidential","privileged","secret"]
    x = levels.index(level)
    return x
