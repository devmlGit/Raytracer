class Material:
    '''
    Material Class - Represents the light ray:
    
    Attributes
    ----------
    color : Color
        the material's color
        
    '''

    def __init__(self, color, materialType):
        self.color = color
        self.materialType = materialType