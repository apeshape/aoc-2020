import re
data = open("data", "r").read().splitlines()

ids = []
highest = 0
for line in data:
  sid = int(re.sub(r"[B|R]", "1", re.sub(r"[F|L]", "0", line)), 2)
  ids.append(sid)
  if sid > highest:
    highest = sid

for seat in range(sorted(ids)[0], highest):
  if seat not in ids:
    print(highest, seat)