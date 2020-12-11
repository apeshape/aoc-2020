from copy import deepcopy
data = open("data", "r").read().splitlines()
seatmap = [list(line) for line in data]

def neighbour_count(neighbours):
  count = 0
  for neighbour in neighbours:
    if neighbour: count += 1
  return count

def in_bounds(x, y, seatmap):
  bounds_right = len(seatmap[0])
  bounds_bottom = len(seatmap)
  return x >= 0 and x < bounds_right and y >= 0 and y < bounds_bottom

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



def get_neighbours(pos, seatmap):

  neighbour_tl = check_direction([-1,-1], pos, seatmap) #ty and lx and seatmap[y-1][x-1] == '#'
  neighbour_t = check_direction([0,-1], pos, seatmap) #ty and seatmap[y-1][x] == '#'
  neighbour_tr = check_direction([1,-1], pos, seatmap) #ty and rx and seatmap[y-1][x+1] == '#'

  neighbour_l = check_direction([-1,0], pos, seatmap) #lx and seatmap[y][x-1] == '#'
  neighbour_r = check_direction([1,0], pos, seatmap) #rx and seatmap[y][x+1] == '#'

  neighbour_dl = check_direction([-1,1], pos, seatmap) #by and lx and seatmap[y+1][x-1] == '#'
  neighbour_d = check_direction([0,1], pos, seatmap) #by and seatmap[y+1][x] == '#'
  neighbour_dr = check_direction([1,1], pos, seatmap) #by and rx and seatmap[y+1][x+1] == '#'

  # print('has neighbours', neighbour_tl, x, y)
  # return neighbour_tl or neighbour_t or neighbour_tr or neighbour_l or neighbour_r or neighbour_dl or neighbour_d or neighbour_dr
  return neighbour_count([neighbour_tl, neighbour_t, neighbour_tr, neighbour_l, neighbour_r, neighbour_dl, neighbour_d, neighbour_dr])


def apply_rules(seatmap):
  new_seatmap = deepcopy(seatmap)
  for idy, seatline in enumerate(seatmap):
    for idx, seat in enumerate(seatline):
      if seatmap[idy][idx] == '.':
        continue
      neighbours = get_neighbours([idx, idy], seatmap)
      if neighbours == 0:
        new_seatmap[idy][idx] = '#'
      elif neighbours >= 5:
        new_seatmap[idy][idx] = 'L'        
  return new_seatmap

def get_seatstring(seatmap):
  lines = []
  for seatline in seatmap:
    lines.append(''.join(seatline))

  return ''.join(lines)

applied = apply_rules(seatmap)
seatstring = get_seatstring(applied)

iterations = 0
test = True
while test:
  applied = apply_rules(applied)
  new_seatstring = get_seatstring(applied)
  if new_seatstring == seatstring:
    test = False
  seatstring = new_seatstring

print('eq', seatstring.count('#'))
