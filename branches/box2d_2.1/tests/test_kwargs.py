import unittest
from Box2D import *

class cl (b2ContactListener):
    pass

class test_kwargs (unittest.TestCase):
    def setUp(self):
        pass

    def test_body(self):
        self.cont_list=cl()
        world = b2World(gravity=(0,-10), doSleep=True, contactListener=self.cont_list)
        groundBody = world.CreateBody(b2BodyDef(position=(0,-10)))

        groundBody.CreateFixture(b2PolygonShape(box=(50,10)))

        body = world.CreateBody(b2BodyDef(type=b2_dynamicBody, position=(0,4),
                        fixtures=[]))
        try:
            body = world.CreateBody(b2BodyDef(type=b2_dynamicBody, position=(0,4),
                            fixtures=[b2PolygonShape(box=(5,1))]))
        except ValueError:
            pass # good
        
        body = world.CreateBody(b2BodyDef(type=b2_dynamicBody, position=(0,4),
                        fixtures=[ (b2PolygonShape(box=(2,1)), 1.0) ]))

        body = world.CreateBody(b2BodyDef(type=b2_dynamicBody, position=(0,4),
                        fixtures=[ (b2PolygonShape(box=(2,1)), 1.0),
                                   (b2PolygonShape(box=(2,1)), 1.0) 
                            ]))
         
        body = world.CreateBody(b2BodyDef(type=b2_dynamicBody, position=(0,4),
                        fixtures=[ b2FixtureDef( shape=b2CircleShape(radius=1), density=1, friction=0.3),
                                    (b2PolygonShape(box=(2,1)), 1.0),
                                    (b2PolygonShape(box=(2,1)), 1.0) 
                            ]))
         
        body.CreateFixture(b2FixtureDef( shape=b2CircleShape(radius=1), density=1, friction=0.3))
         
        timeStep = 1.0 / 60
        vel_iters, pos_iters = 6, 2

        for i in range(60):
            world.Step(timeStep, vel_iters, pos_iters)
            world.ClearForces()

if __name__ == '__main__':
    unittest.main()
