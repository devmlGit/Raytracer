import numpy as np
from Sphere import *
from Vect3 import *
from Material import *
from Color import *

class Scene:
    '''
    Scene Class - stores the scene objects:

    Attributes
    ----------
    sceneObjects : numpy array of Sphere
        list of the scene objects
    lightSources : Light
        scene's lightsource
        
    '''

    def __init__(self, sceneObjects, lightSource):
        self.sceneObjects = sceneObjects
        self.lightSource = lightSource

    # Returns 2d array [ray intersection point, sphere it hit] if ray hits something else False
    def Intersect( self, ray, orig):
        # The time traveled by the ray until it hits something
        t = 0

        # Sphere hit by the ray
        sphereInter = Sphere(Vect3(0,0,0), 1, Material(Color(0,0,0), "diffuse"))

        # Checks which sphere it hit first
        for sphere in self.sceneObjects:
            result = sphere.Intersect(ray, orig)
            if result != False:
                sphereInter = sphere if (result < t or t == 0) else sphereInter
                t = result if t == 0 else min( result, t)

        # Returns t
        if t != 0:
            return np.array([t, sphereInter])
        else:
            return False