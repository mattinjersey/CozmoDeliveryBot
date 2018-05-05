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

# to do: right now the robot recognizes cube by pattern not by color.

import asyncio
import cozmo
from cozmo.util import degrees, distance_mm
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
import time
from random import randint

def SelectCubes(robot,FoundCubes,NumCubes):
    print("NumCubes:%s" % NumCubes)
    z0=55
    for count in range(NumCubes):
        print("cube :%s  Height: %s  Object:%s" % ( count,FoundCubes[count].pose.position.z,FoundCubes[count].object_id))
    if NumCubes==2:
        if FoundCubes[0].pose.position.z>z0:
            print("Cube 0 high")
            # cube 0 is HIGH in the air!...move 0 first
            ID1=0
            ID2=1
        elif  FoundCubes[1].pose.position.z>z0:
            # cube 1 is HIGH in the air!...move 1 first
            print("Cube 1 high")
            ID1=1
            ID2=0
        else:
            k=randint(0,1)
            if k==1:
                ID1=0
                ID2=1
                print("sCube1:0")
                print("sCube2:1")
            else:
                ID2=0
                ID1=1
 
    else: # NumCubes=-3
       if FoundCubes[0].pose.position.z>z0:
            # cube 0 is HIGH in the air!...move 0 first
            ID1=0
            if abs( FoundCubes[0].pose.position.x- FoundCubes[1].pose.position.x)<10:
                ID2=2
            else:
                ID2=1
       elif  FoundCubes[1].pose.position.z>z0:
            print("Cube 1 High.")
            # cube 1 is HIGH in the air!...move 1 first
            ID1=1
            if abs( FoundCubes[0].pose.position.x- FoundCubes[1].pose.position.x)<10:
                ID2=2
            else:
                ID2=0
       elif  FoundCubes[2].pose.position.z>z0:
            # cube 2 is HIGH in the air!...move 1 first
            print("Cube 2 High.")
            ID1=2
            if abs( FoundCubes[0].pose.position.x- FoundCubes[2].pose.position.x)<10:
                ID2=1
            else:
                ID2=0
       else:
            print("no cube high, random select.")
            k1=randint(0,2)
            k2=k1
            while (k2==k1):
                k2=randint(0,2)
            ID1=k1
            ID2=k2
    sCube1=FoundCubes[ID1]
    sCube2=FoundCubes[ID2]
    print("sCube1:%s  cubeID:%s" % (ID1,sCube1.object_id))    
    print("sCube2:%s  cubeID:%s" % (ID2,sCube2.object_id)) 
    cube1 = robot.world.get_light_cube(LightCube1Id)  # looks like a paperclip
    cube2 = robot.world.get_light_cube(LightCube2Id)  # looks like a lamp / heart
    cube3 = robot.world.get_light_cube(LightCube3Id)  # looks like the letters 'ab' over 'T'
    if sCube1.object_id==cube1.object_id:
        startColor="red"
    elif sCube1.object_id==cube2.object_id:
        startColor="Green"
    elif sCube1.object_id==cube3.object_id:
        startColor="Blue"
    if sCube2.object_id==cube1.object_id:
        endColor="red"
    elif sCube2.object_id==cube2.object_id:
        endColor="Green"
    elif sCube2.object_id==cube3.object_id:
        endColor="Blue"
    return sCube1,startColor,sCube2,endColor
