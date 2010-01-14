#!/usr/bin/python
#
# C++ version Copyright (c) 2006-2007 Erin Catto http://www.gphysics.com
# Python version Copyright (c) 2010 Ken Lauer / sirkne at gmail dot com
# 
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
# 1. The origin of this software must not be misrepresented; you must not
# claim that you wrote the original software. If you use this software
# in a product, an acknowledgment in the product documentation would be
# appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
# misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

from pygame_main import Framework, main
from Box2D.b2 import *

# This test uses the alternative syntax offered by Box2D.b2, so you'll notice
# that all of the classes that normally have 'b2' in front of them no longer
# do. The choice of which to use is mostly stylistic and is left up to the user.

class Chain (Framework):
    name="Chain"
    def __init__(self):
        super(Chain, self).__init__()

        # The ground
        ground = self.world.CreateBody(
                bodyDef(
                    fixtures=[ 
                        polygonShape(edge=[(-40,0),(40,0)]) 
                        ]
                    )
                )

        plank=fixtureDef(
                    shape=polygonShape(box=(0.6,0.125)),
                    density=20,
                    friction=0.2,
                )

        # Create one Chain (Only the left end is fixed)
        prevBody = ground
        y = 25
        numPlanks = 30
        for i in range(numPlanks):
            body = self.world.CreateBody(
                    bodyDef(
                        type=dynamicBody,
                        position=(0.5+i, y), 
                        fixtures=[plank],
                        )
                    )

            self.world.CreateJoint(
                #weldJointDef(  # You can try this, too, for a slightly different effect.
                revoluteJointDef(
                        bodyA=prevBody,
                        bodyB=body,
                        anchor=(i, y),
                    )
                )

            prevBody = body

if __name__=="__main__":
     main(Chain)

