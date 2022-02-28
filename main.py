from Sphere import *
from Camera import *
from Vect3 import *
from Scene import *
from Light import *
from Color import *

def main():
    scene = Scene(np.array([Sphere(Vect3(0,0,5), 10, Material(Color(0,255,250), "diffuse")),
                                Sphere(Vect3(0,0,1000), 940, Material(Color(255,255,255), "diffuse")),
                                Sphere(Vect3(0,0,-1000), 940, Material(Color(255,255,255), "diffuse")),
                                Sphere(Vect3(0,1000,0), 940, Material(Color(255,255,255), "diffuse")),
                                Sphere(Vect3(0,-1000,0), 990, Material(Color(255,255,255), "diffuse")),
                                Sphere(Vect3(-1000,0,0), 940, Material(Color(255,255,255), "diffuse")),
                                Sphere(Vect3(1000,0,0), 940, Material(Color(255,255,255), "diffuse"))]), Light(Vect3(-10,20,40), 750))

    camera = Camera(100, 100, 60, Vect3(0,3,55), scene)
    camera.Render()

main()
