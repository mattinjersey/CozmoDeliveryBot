#!/usr/bin/env python3

# Copyright (c) 2017 Anki, Inc.
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

'''Demonstrate the use of Object Moving events to detect when the cubes are moved.

This script is a simple example of how to subscribe to Object Moving events to
track when Cozmo detects that a cube is being moved.
'''

import time

import cozmo



def handle_object_tapped(evt, **kw):
    global keepGoing
    # This will be called whenever an EvtObjectMovingStarted event is dispatched -
    # whenever we detect a cube starts moving (via an accelerometer in the cube)
    print("Object %s was tapped: number of taps=%s" %
          (evt.obj.object_id, evt.tap_count))
    keepGoing=False
    #print('KeepGoing:%s' %(keepGoing) )

def aWaiting(robot: cozmo.robot.Robot):
    global keepGoing
    # Add event handlers that will be called for the corresponding event
    robot.add_event_handler(cozmo.objects.EvtObjectTapped, handle_object_tapped)
    robot.say_text("waiting for tapped cube").wait_for_completed()
    keepGoing=True
    # keep the program running until user closes / quits it
    #print("Press CTRL-C to quit")
    while keepGoing:
        time.sleep(0.1)
    robot.say_text("cube Tapped").wait_for_completed()

#cozmo.robot.Robot.drive_off_charger_on_connect = False  # Cozmo can stay on his charger for this example
#cozmo.run_program(aWaiting)
