import time
from mcpi import minecraft

mc = minecraft.Minecraft.create()

redstonePositions = []

plateActive = 247
wireInactive = 10
wireActive = 12

while True:

    x, y, z = mc.player.getTilePos()

    if mc.getBlock(x, y-1, z) == wireInactive:
        redstonePositions = [redstonePositions, (x, y-1, z)]
        mc.postToChat("New redstone wire position ( X : " + str(x) + " Y :" + str(y) + " Z :" + str(z) + ") added.")
