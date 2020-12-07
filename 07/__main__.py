import re
data = open("data", "r").read().splitlines()

bags = []
def check_bagtype(bagtype, lvl):
  for line in data:
    bt, contains = line.split('contain')

    gb_contains = re.search('('+bagtype+')', contains)

    if gb_contains:
      container = bt.replace(' bags', '')
      if container not in bags:
        bags.append(container)

      check_bagtype(container, lvl + 1)

check_bagtype('shiny gold', 1)
print(bags)
print(len(bags))
