data = open("data", "r").read()

groups = data.split("\n\n")

def checkAnswersMatch(testAgainst, answers):
  if len(answers) == 0:
    return testAgainst

  newTestAgainst = []
  for otherAnswer in list(answers[0]):
    if otherAnswer in list(testAgainst) and otherAnswer not in newTestAgainst:
      newTestAgainst.append(otherAnswer)

  return checkAnswersMatch(newTestAgainst, answers[1:])

sum = 0
for group in groups:
  answers = group.split('\n')

  # my crappy recursion
  matches = checkAnswersMatch(answers[0], answers[1:])
  # 
  # matches = set(answers[0]).intersection( *answers[1:] )
  sum += len(matches)

print("SUM::", sum)