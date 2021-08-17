def print_all(names, tests, scores):
  header = 'Name'
  row = ''

  for test in tests:
    header += '\t'+test
    
  print(header)

  for name_index in range(len(names)):
    row = names[name_index]
    for score_index in range(len(scores)):
      row += '\t'+ str(scores[name_index][score_index])
    
    print(row)

def print_student_scores(index, students, tests, scores):
  print("Test results for {0}:".format(students[index]))
  for test_index in range(len(tests)):
    print("{0} = {1}%".format(tests[test_index], scores[index][test_index]))

def print_test_scores(index, test, students, scores):
  print("Class results for {0} test:".format(test))
  for student_index in range(len(students)):
    print("{0} = {1}%".format(students[student_index], scores[student_index][index]))