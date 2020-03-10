from parse import *
from matrix import *
from graphics import *
import random

points = newMatrix(4,0)
transform = identity(newMatrix())
color = [150, 0, 255]
createPixels(600, 600, 255)
# Uncomment if you want to make the image
parseFile("script", points, transform, pixels, color)
