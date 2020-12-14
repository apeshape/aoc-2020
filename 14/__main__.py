import re
data = open("data", "r").read().splitlines()

mem = {}

# def get_mask(maskstr):
#   return maskstr.replace('X', '0')

def get_value(mask, value):
  outval = []
  formatted_val = format(int(value), 'b')
  formatted_val = '0' * (36 - len(formatted_val)) + formatted_val

  for idx, masked in enumerate(mask):
    if mask[idx] == 'X':
      outval.append(formatted_val[idx])
    else:
      outval.append(mask[idx])
  
  return int(''.join(outval), 2)

mask = ''
for instr in data:
  instr_type, value = instr.split(' = ')
  # print(instr_type, value)
  if instr_type == 'mask':
    # mask = int(get_mask(value),2)
    mask = value
    print('mask', mask)
  else:
    val = get_value(mask, value)
    address_match = re.match(r"mem\[(\d*)\]", instr_type)
    addr = address_match.groups(0)[0]
    mem[addr] = val
    print(val, addr)

print('sum', sum(mem.values()))