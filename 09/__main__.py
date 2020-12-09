from time import sleep
data = open("data", "r").read().splitlines()

def get_checksum_and_data(start, datalist):
  datalist = list(map(int, datalist))
  preamble = datalist[:start]
  rest = datalist[start:]
  checksums = []
  for chknum in preamble:
    for chknum2 in preamble:
      if chknum != chknum2:
        checksums.append(chknum + chknum2)
  return [checksums, rest]

def get_corrupt_number(startIdx):
  all_numbers = data.copy()
  i = 0
  while i < len(data):
    checksums, rest = get_checksum_and_data(startIdx, all_numbers)
    all_numbers = all_numbers[1:]

    testnum = rest[0]
    if testnum not in checksums:
      return testnum

    i += 1


def find_corrupt_set(corrupt):
  all_numbers = list(map(int, data))
  possible_numbers = [number for number in all_numbers if int(number) <= corrupt]

  startIdx = 0
  while startIdx < len(possible_numbers):
    continousSet = []
    for num in all_numbers[startIdx:]:
      continousSet.append(num)
      set_sum = sum(continousSet)
      if set_sum == corrupt:
        return continousSet
      if set_sum > corrupt:
        break
    startIdx += 1

  return []

corrupt = get_corrupt_number(25)
corrupt_set = find_corrupt_set(corrupt)

part1 = corrupt
part2 = min(corrupt_set) + max(corrupt_set)

print('part1', part1, '\npart2', part2)