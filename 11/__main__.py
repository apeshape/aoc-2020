from time import sleep
from copy import deepcopy
data = open("data", "r").read().splitlines()
seatmap = [list(line) for line in data]

def in_bounds(x, y, seatmap):
  return x >= 0 and x < len(seatmap[0]) and y >= 0 and y < len(seatmap)

def check_direction(direction, start_pos, seatmap):
  xdir, ydir = direction
  x, y = start_pos
  while in_bounds(x + xdir, y + ydir, seatmap):
    x += xdir
    y += ydir
    space = seatmap[y][x]
    if(space == '#'):
      return True
    if(space == 'L'):
      return False
  return False


def get_neighbours(pos, seatmap):
  directions = [
    [-1,-1],
    [0,-1],
    [1,-1],
    [-1,0],
    [1,0],
    [-1,1],
    [0,1],
    [1,1]
  ]
  count = 0
  for direction in directions:
    count += int(check_direction(direction, pos, seatmap))

  return count

def apply_rules(seatmap):
  new_seatmap = deepcopy(seatmap)
  changed = False
  for idy, seatline in enumerate(seatmap):
    for idx, seat in enumerate(seatline):
      if seat == '.':
        continue
      neighbours = get_neighbours([idx, idy], seatmap)
      if neighbours == 0:
        new_seatmap[idy][idx] = '#'
        changed = True
      elif neighbours >= 5:
        new_seatmap[idy][idx] = 'L'
        changed = True
  return [changed, new_seatmap]

def get_seatstring(seatmap):
  lines = []
  for seatline in seatmap:
    lines.append(''.join(seatline))

  return ''.join(lines)

seatstring = ''
while True:
  [changed, seatmap] = apply_rules(seatmap)
  new_seatstring = get_seatstring(seatmap)
  if new_seatstring == seatstring:
    break
  seatstring = new_seatstring


print('eq', get_seatstring(seatmap).count('#'))
