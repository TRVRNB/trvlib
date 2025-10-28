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

trv.random_name(l: int)
  returns a random name of length l
  for example, if l==2, then it will generate a first and last name

trv.randi(seed: int, min: int, max: int)
  like random.randint(), but with a builtin seed feature

trv.cypher(key: int, text: str)
  cyphers text using this key
  use trv.decypher() with the same key to decode it

trv.decypher(key: int, text: str)
  decyphers cyphered text using the same key as trv.cypher()
  
