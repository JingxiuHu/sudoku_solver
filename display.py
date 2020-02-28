## Max Roschke -- Project 03, Sudoku display code
## imports
import time

## windows color
try:
   import colorama
   colorama.init()
except ImportError:
   pass

## global for original screen clear
_cleared = False

def display(puzzle, wait=0.1):
   ## if you really want to know what these are, google for the term:
   ##   'VT100 escape codes'
   ## (1) clear the screen on the first call
   global _cleared
   if not _cleared:
      print('\x1B[2J', end='') 
      _cleared = True
   ## (2) move to upper-left corner
   print('\x1B[H', end='')

   ## (3) print the puzzle
   print(puzzle)

   ## (4) wait specified amount of time
   time.sleep(wait)

