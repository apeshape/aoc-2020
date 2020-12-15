data = '12,1,16,3,11,0'
# data = '1,3,2'
# data = '0,3,6'
input_list = data.split(',')

numbers = [int(num) for num in input_list]

print('testing for ', numbers)
spoken = {}
for idx, num in enumerate(numbers):
  spoken[num] = [idx]

turns = len(spoken.keys())
all_spoken = numbers.copy()
while turns < 30000000:
  last_spoken = all_spoken[-1]
  current = numbers[turns % len(numbers)]

  # print('{:2}:'.format(turns), 'last spoken', last_spoken)

  if last_spoken in spoken.keys():
    if len(spoken[last_spoken]) > 0:
      #number has been said before, at least once
      if len(spoken[last_spoken]) > 1:
        current_tail = spoken[last_spoken][-2:]
        diff = current_tail[1] - current_tail[0]
        
        # print('said before, twice', spoken[last_spoken][:2], diff)
        all_spoken.append(diff)
        if diff in spoken.keys():
          spoken[diff].append(turns)
        else:
          spoken[diff] = [turns]
      else:
        if 0 in spoken.keys():
          spoken[0].append(turns)
          all_spoken.append(0)
        else:
          spoken[0] = [turns]
          all_spoken.append(0)

  else:
    #first time number was said
    all_spoken.append(current)
    spoken[current] = [turns]

  turns += 1

print('DONE', all_spoken[-1])