from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single word that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
  with open(fname, "r") as file:
    commands = file.readlines()
  commands = [command.strip() for command in commands]
  numCommands = len(commands)
  i = 0

  while (i < numCommands):
    if (commands[i] == "line"):
      newedge = commands[i + 1].split()
      newedge = [int(x) for x in newedge]
      add_edge(points, newedge[0], newedge[1], newedge[2], newedge[3], newedge[4], newedge[5])
      i += 2

    elif (commands[i] == "ident"):
      ident(transform)
      i += 1

    elif (commands[i] == "scale"):
      scales = commands[i + 1].split()
      scales = [int(x) for x in scales]
      m = make_scale(scales[0], scales[1], scales[2])
      matrix_mult(m, transform)
      i += 2

    elif (commands[i] == "move"):
      moves = commands[i + 1].split()
      moves = [int(x) for x in moves]
      m = make_translate(moves[0], moves[1], moves[2])
      matrix_mult(m, transform)
      i += 2

    elif (commands[i] == "rotate"):
      rotates = commands[i + 1].split()
      if (rotates[0] == "x"):
        m = make_rotX(int(rotates[1]))
      elif (rotates[0] == "y"):
        m = make_rotY(int(rotates[1]))
      else:
        m = make_rotZ(int(rotates[1]))
      matrix_mult(m, transform)
      i += 2

    elif (commands[i] == "apply"):
      matrix_mult(transform, points)
      i += 1

    elif (commands[i] == "display"):
      draw_lines(points, screen, color)
      display(screen)
      i += 1

    elif (commands[i] == "save"):
      newfile = commands[i + 1].split()
      draw_lines(points, screen, color)
      save_extension(screen, newfile[0])
      i += 2

    elif (commands[i] == "quit"):
      return

    else:
      raise Exception("invalid command in script")
