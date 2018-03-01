from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

test = make_rotZ(30)
print_matrix(test)

parse_file( 'script', edges, transform, screen, color )
