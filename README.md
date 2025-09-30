# trvlib

trv.sign(x: int/float)
  returns 1 if positive, -1 if negative, 0 if neutral

trv.print_lines(n: int)
  print n blank lines, used for separating text easily

trv.print_grid(grid: list, maxlen=0)
  prints out a 2D list (list of lists) in a human-readable way
  works best with numbers or short strings
  maxlen should usually be kept at 0, but can be manually set
  at 0, maxlen will automatically create the correct amount of space between items
