# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 15:28:03 2018

@author: matt
"""

import asyncio
import cozmo
from cozmo.util import degrees, distance_mm
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
import time
from xCubeTapped import aWaiting
from xCubeLights import cozmo_Lights
from xFindCubes import FindCubes
from xDeliveryStep import DeliveryStep
from xSelectCubes import SelectCubes


def Delivery(robot: cozmo.robot.Robot): 
     cube1,cube2,cube3=cozmo_Lights(robot)
     #aWaiting(robot)
     NumCubes=0
     while NumCubes<2:
       robot.say_text("Find cubes").wait_for_completed()
       look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
       FoundCubes = robot.world.wait_until_observe_num_objects(num=3, object_type=cozmo.objects.LightCube, timeout=10)
       look_around.stop()
       NumCubes=len(FoundCubes)
       aText='Found '+str(NumCubes)+ ' Cubes'
       robot.say_text(aText).wait_for_completed()
     # to do: right now the robot recognizes color because it knows what color every cube is.
     sCube1,startColor,sCube2,endColor=SelectCubes(robot,FoundCubes,NumCubes)
     robot.say_text("Deliver "+ startColor+" to "+endColor).wait_for_completed()
     aDeliver=DeliveryStep(robot,sCube1,startColor,sCube2,endColor)
     # to do: robot should drive back to base
     robot.say_text("Mission Complete").wait_for_completed()


cozmo.run_program(Delivery)