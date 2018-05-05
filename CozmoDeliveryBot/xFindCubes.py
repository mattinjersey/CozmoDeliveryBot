#!/usr/bin/env python3

# Copyright (c) 2016 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Tell Cozmo to find a cube, and then drive up to it

This is a test / example usage of the robot.go_to_object call which creates a
GoToObject action, that can be used to drive within a given distance of an
object (e.g. a LightCube).
'''

import asyncio
import cozmo
from cozmo.util import degrees, distance_mm
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
import time


def FindCubes(robot: cozmo.robot.Robot,sCube1,sCube2,aColor,bColor):
    '''The core of the go to object test program'''
    robot.say_text("Find cubes").wait_for_completed()
    look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    FoundCubes = robot.world.wait_until_observe_num_objects(num=3, object_type=cozmo.objects.LightCube, timeout=5)
    look_around.stop()
    NumCubes=len(FoundCubes)
    robot.say_text("Found ").wait_for_completed()
    robot.say_text(str(NumCubes)).wait_for_completed()
    robot.say_text("Cubes").wait_for_completed()
    print('Found NumCubes:%s' %(NumCubes) )
    ID=[0]*3
    for count in range(NumCubes):
        ThisID=FoundCubes[count].cube_id
        
        ID[count]=ThisID
        print('Cube :%s  ID:%s' %(count,ThisID) )
    redFound=False
    blueFound=False
    redIndex=0
    blueIndex=0
    for count in range(NumCubes):
        if ID[count]==sCube1.cube_id:
            redFound=True
            redIndex=count
        elif ID[count]==sCube2.cube_id:
            blueFound=True
            blueIndex=count
    goodFind=redFound and blueFound
    if goodFind:
        aString="found " + aColor+ " and "+bColor
        robot.say_text(aString).wait_for_completed()
    else:
        aString="didn't find both " + aColor+ " and "+bColor
        robot.say_text("didnt find both red and blue").wait_for_completed()
    return NumCubes,FoundCubes,goodFind,redIndex,blueIndex
