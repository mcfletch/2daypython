#! /usr/bin/env python
'''Test of the glVertex function (draws flower)'''
from OpenGLContext import testingcontext
BaseContext = testingcontext.getInteractive()
from OpenGL.GL import *
from OpenGLContext.arrays import array
from OpenGLContext.scenegraph.basenodes import *

vertices = array([
    [-1,0,0,1,0,0],
    [1,0,0,0,1,0],
    [0,1,0,0,0,1],
],dtype='f')


class TestContext( BaseContext ):
    def OnInit(self):
        self.scenegraph = self.sg = sceneGraph(children=[
            Transform( children = [
                Shape(
                    geometry = IndexedFaceSet(
                        coord = Coordinate(
                            point = vertices[:,:3],
                        ),
                        color = Color(
                            color = vertices[:,3:6],
                        ),
                        ccw = True,
                        coordIndex = array([0,1,2]),
                    ),
                ),
                ],
                translation = [0,0,8],
            ),
        ])

if __name__ == "__main__":
    TestContext.ContextMainLoop()
