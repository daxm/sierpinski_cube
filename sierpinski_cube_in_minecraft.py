#!/usr/bin/python3

from mcpi.minecraft import Minecraft
import datetime

################
# Changeable Variables
serverip = '192.168.11.253'
recursives = 6  # Remember each new recursion is 27 times larger than the previous one!
# Note: There is a "ceiling" on max build height (default of 256).
# Change it in the minecraft server.properties file before using recursives > 3.
x = 0
y = -64
z = 0
#tThe sctblockType = 7    # Bedrock
blockType = 57    #  Diamond Block
# blockType = 103    # TNT

# Do you want to fill the area prior to building on it?
fillBlockType = 0    # AIR
filler = 1

# Do you want to be teleported there when it is done being built?
teleportPlayer = 1
################


def PlaceBlock(x,y,z,blockType):
    mc.setBlock(x,y,z,blockType)


def BuildStructure(level,x0,y0,z0,blockType):
    nextLevel = level - 1
    levelSize = pow(3,level)
    thirds = int(levelSize / 3)
    twoThirds = thirds * 2
    if level == 0:
        rangerX = [x0]
        rangerY = [y0]
        rangerZ = [z0]
    else:
        rangerX = [x0, x0 + thirds, x0 + twoThirds]
        rangerY = [y0, y0 + thirds, y0 + twoThirds]
        rangerZ = [z0, z0 + thirds, z0 + twoThirds]
    block = 1
    for i in rangerX:
        for j in rangerY:
            for k in rangerZ:
                if (block!=5) and (block!=11) and (block!=13) and (block!=14) and (block!=15) and (block!=17) and (block!=23):
                    if(level > 0):
                        BuildStructure(nextLevel,i,j,k,blockType)
                    else:
                        PlaceBlock(i,j,k,blockType)
                block+=1


# Main Program
programStartTime = datetime.datetime.now()

# Connect to server.
mc = Minecraft.create(address=serverip)

#Fill the area with "fillBlockType".
if filler == 1:
    mc.setBlocks(x,y,z,x*3,y*3,z*3,fillBlockType)

# Build the Sierpinski's Cube.
BuildStructure(recursives,x,y,z,blockType)

#Move player to see the creation.  ### Fix Me.  I don't know where to drop the user after we are done. ###
if teleportPlayer == 1:
    #coord = pow(3,recursives) + 3
    #xP = coord
    #yP = coord
    #zP = coord
    xP = x + 3
    yP = y + 3
    zP = z + 3
    mc.player.setPos(xP,yP,zP)

programEndTime = datetime.datetime.now()

# Print info.
print("The program started at ", programStartTime, "\n")
print("The program ended at ", programEndTime, "\n")
diff = programEndTime - programStartTime
print("The program took ", diff, "\n")
print("\n")
print("The program is done.\n")
