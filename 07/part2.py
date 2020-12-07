import re
data = open("testdata", "r").read().splitlines()

bagtypes = {}
def get_rule(rulestr):
  if(rulestr != "no other bags."):
    bt = re.search(r"(\w*. \w*.)", rulestr[1:])
    return { bt.group(0).strip(): int(rulestr[:1]) }

for line in data:
  bagtype, contents = (lambda x = line.split(" contain "): [x[0].replace(" bags", ""), x[1].split(", ")])()
  rules = [get_rule(rulestr) for rulestr in contents if get_rule(rulestr)]
  bagtypes[bagtype] = rules

def bag_contains(bt, total):
  for rule in bt:
    bagtype = list(rule.keys())[0]

    newtotal = [bag_contains(bagtypes[bagtype], total + 1) for rng in range(0, rule[bagtype])]
    print('newtotal', newtotal)
    for res in range(0, rule[bagtype]):
      total = bag_contains(bagtypes[bagtype], total + 1)
  
  return total

total = bag_contains(bagtypes["shiny gold"], 0)
print(total)