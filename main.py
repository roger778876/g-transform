from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

test = make_rotY(30.3)
print_matrix(test)

parse_file( 'script', edges, transform, screen, color )
