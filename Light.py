class Light:
    '''
    Light Class - lightsource:

    Attributes
    ----------
    coord : Vect3
        center of the lightsource
    intensity : float
        light's intensity
        
    '''

    def __init__(self, coord, intensity):
        self.coord = coord
        self.intensity = intensity