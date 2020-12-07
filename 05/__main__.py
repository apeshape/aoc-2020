data = open("data", "r").read().splitlines()

teststr = "BBFFBBFRLL"

def letterToBin(l):
  if l == "B" or l == "R": 
    return "1"
  if l == "F" or l == "L":
    return "0"
  return ""

def getSeat(positionString):
  positions = list(map(letterToBin, list(positionString)))
  rowstr = "".join(positions[:-3])
  colstr = "".join(positions[-3:])

  rowval = int(rowstr, 2)
  colval = int(colstr, 2)
  return [rowval, colval]

def getSeatId(row, col):
  return row * 8 + col

ids = []
highest = 0
for line in data:
  row, col = getSeat(line)
  sid = getSeatId(row, col)
  ids.append(sid)
  if sid > highest:
    highest = sid

startTest = 53
for sid in sorted(ids):
  if sid != startTest:
    print('sid', sid - 1)
    break
  startTest += 1
