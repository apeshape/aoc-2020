import re
data = open("data", "r").read().splitlines()

bagtypes = {}
for line in data:
  bagtype, contains = line.split(' contain ')
  bagtype = bagtype.replace(' bags', '')

  rules = []
  contents = contains.split(', ')
  for possible_contents in contents:
    if possible_contents != 'no other bags.':
      bt = re.search(r"(\w*. \w*.)", possible_contents[1:])
      rule = {
        "amount": int(possible_contents[:1]),
        "bagtype": bt.group(0).strip()
      }
      rules.append(rule)

  bagtypes[bagtype] = rules

result = []
def bag_contains(bt, total):
  for rule in bt:
    for res in range(0, rule["amount"]):
      result.append('f')
      bag_contains(bagtypes[rule['bagtype']], total + 1)

bag_contains(bagtypes['shiny gold'], 0)
print(len(result))