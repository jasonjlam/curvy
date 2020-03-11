from parse import *
from matrix import *
from graphics import *
import random

points = newMatrix(4,0)
transform = identity(newMatrix())
color = [0, 0, 0]
createPixels(600, 600, 255)
parseFile("script", points, transform, pixels, color)
# Uncomment if you want to make the image
# createPixels(1300, 1300, 255)
# parseFile("kirb", points, transform, pixels, color)
