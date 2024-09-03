def line_count():
  
  file = open('file.txt', 'r') #opens the file (file.txt) in read mode
  
  number_lines = len(file.readlines()) #states that the number of lines is equal to the length of the resulting list from running the readlines function
  
  file.close() #closes the file
  
  return('number_lines') #returns the number of lines from above