import re
data = open("data", "r").read().splitlines()

bagtypes = {}

def get_rule(rulestr):
  bt = re.search(r"(\w*. \w*.)", rulestr[1:])
  return {
    "amount": int(rulestr[:1]),
    "bagtype": bt.group(0).strip()
  }


for line in data:
  bagtype, contains = line.split(" contain ")
  bagtype = bagtype.replace(" bags", "")

  contents = contains.split(", ")
  if(contents[0] == "no other bags."):
    rules = []
  else:
    rules = [get_rule(rulestr) for rulestr in contents]

  bagtypes[bagtype] = rules

def bag_contains(bt, total):
  for rule in bt:
    for res in range(0, rule["amount"]):
      total = bag_contains(bagtypes[rule["bagtype"]], total + 1)
  
  return total

total = bag_contains(bagtypes["shiny gold"], 0)
print(total)