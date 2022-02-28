from math import *

class Sphere:
    '''
    Sphere Class - Sphere 3D object:
    
    Attributes
    ----------
    coord : Vect3
        the center coordinates
    radius : float
        the sphere's radius
    
    '''
    
    def __init__(self, coord, radius, material):
        self.coord = coord
        self.radius = radius
        self.material = material

    # Returns the time traveled by the ray until it hit this sphere object or False if the ray hits nothing
    def Intersect(self, ray, orig):

        # Delta used in the polynomial equation solving
        delta = (2 * ray.dot(orig - self.coord)) ** 2 - 4 * ((orig - self.coord).norm() ** 2 - self.radius ** 2)
        
        # if there is a solution (in other words, if the ray hit something)
        if delta >= 0:
            # Calculates the time traveled before reaching tis intersection point
            t = (-(2 * ray.dot(orig - self.coord)) - sqrt(delta))/2

            # Checks if the object is not behind the camera
            if t >= 0:
                return t

        return False