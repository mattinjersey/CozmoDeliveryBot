# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 11:08:11 2018

@author: matt
"""


import asyncio
import cozmo
from cozmo.util import degrees, distance_mm
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
import time

def DeliveryStep(robot: cozmo.robot.Robot,cubeA,startColor,cubeB,endColor):
    pickupTry=0
    goodPickup=False
    while goodPickup==False:
        pickupTry+=1
        robot.say_text("Going to "+startColor+" cube").wait_for_completed()
        action=robot.pickup_object(cubeA)
        action.wait_for_completed()
        if action.has_failed:
           code, reason = action.failure_reason
           result= action.result
           print("pickup cube failed. code=%s  reason=%s result=%s" % (code,reason,result))
           robot.say_text("Picked up cube Failed").wait_for_completed()
        else:
           goodPickup=True
        if pickupTry>=3:
            return False
    robot.say_text("Picked up "+startColor+" cube").wait_for_completed()
    robot.say_text("Going to "+endColor+" Cube").wait_for_completed()
    action=robot.place_on_object(cubeB, num_retries=3)
    action.wait_for_completed()
#    if action.has_failed:
#       code, reason = action.failure_reason
#       result= action.result
#       print("place cube failed. code=%s  reason=%s result=%s" % (code,reason,result))
#       robot.say_text("Deliver cube Failed").wait_for_completed()
#       return False
    robot.say_text("Dropped "+startColor+" cube at "+endColor+" cube").wait_for_completed()
    return True
