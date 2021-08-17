def average_for_student(name_index,scores):
  total = 0
  for score in scores[name_index]:
    total += score
  
  average = total/len(scores[name_index])
  return average

def average_for_test(test_index,scores):
  total = sum(scores[test_index])
  average = total/len(scores[0])
  return average
