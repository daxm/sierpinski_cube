#!/usr/bin/python3

################
# Changeable Variables
serverip = '192.168.11.253'
layers = 3
x = 10
y = 10
z = 10
blockType = 46 #TNT
fillBlockType = 0 #AIR
filler = 1
################

from mcpi.minecraft import Minecraft
mc = Minecraft.create(address=serverip)

def placeblock(x,y,z,blockType):
    mc.setBlock(x,y,z,blockType)

def buildstructure(layers,blockType,x,y,z):
    nextlayer = layers - 1
# There are 27 "blocks" in a structure but only 20 get filled in.
# Starting at the "bottom, front, left" position each is named by its position on that level and the level itself.
# A "position" is numbered 1-9 (like a tic-tac-toe board) starting at bottom left and working left to right then upwards.
# So "11" is the first position on the first level whereas "39" is the last block (3rd level, 9th position).

# Note, "y" is "up" so x,y is the plain/level.

#Position 11
    if nextlayer == 1:
        placeblock(x,y,z,blockType)
    else:
        buildstructure(nextlayer,blockType,x,y,z)
#Position 12
    placeblock(x+1,y,z,blockType)
#Position 13
    placeblock(x+2,y,z,blockType)
#Position 14
    placeblock(x,y,z+1,blockType)
#Position 15 (no block)
#    placeblock(x+1,y,z+1,blockType)
#Position 16
    placeblock(x+2,y,z+1,blockType)
#Position 17
    placeblock(x,y,z+2,blockType)
#Position 18
    placeblock(x+1,y,z+2,blockType)
#Position 19
    placeblock(x+2,y,z+2,blockType)
#Position 21
    placeblock(x,y+1,z,blockType)
#Position 22 (no block)
#    placeblock(x+1,y+1,z,blockType)
#Position 23
    placeblock(x+2,y+1,z,blockType)
#Position 24 (no block)
#    placeblock(x,y+1,z+1,blockType)
#Position 25 (no block)
#    placeblock(x+1,y+1,z+1,blockType)
#Position 26 (no block)
#    placeblock(x+2,y+1,z+1,blockType)
#Position 27
    placeblock(x,y+1,z+2,blockType)
#Position 28 (no block)
#    placeblock(x+1,y+1,z+2,blockType)
#Position 29
    placeblock(x+2,y+1,z+2,blockType)
#Position 31
    placeblock(x,y+2,z,blockType)
#Position 32
    placeblock(x+1,y+2,z,blockType)
#Position 33
    placeblock(x+2,y+2,z,blockType)
#Position 34
    placeblock(x,y+2,z+1,blockType)
#Position 35 (no block)
#    placeblock(x+1,y+2,z+1,blockType)
#Position 36
    placeblock(x+2,y+2,z+1,blockType)
#Position 37
    placeblock(x,y+2,z+2,blockType)
#Position 38
    placeblock(x+1,y+2,z+2,blockType)
#Position 39
    placeblock(x+2,y+2,z+2,blockType)

### Start the program ###

#Move player to see the creation
mc.player.setPos(x-3,y-3,z-3)

#Fill the area with "fillBlockType
if filler == 1:
    mc.setBlocks(x,y,z,x*3,y*3,z*3,fillBlockType)

# Build the Sierpinski's Cube
buildstructure(layers,blockType,x,y,z)

