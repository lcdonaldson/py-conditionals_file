import os
textToFind = "white"
textToReplace = "#fff"
sourcePath = os.listdir('pathToFile')
for file in sourcePath:
  inputfile = 'pathToFile' + file
  print('converting' + inputfile)
  with open(inputfile, 'r') as inputfile:
    filedata = inputfile.read()
    freq = 0
    freq = filedata.count(textToFind)
  fileToChange = 'pathToFile' + file
  filedata = filedata.replace(textToFind, textToReplace)
  with open(fileToChange, 'w') as file:
    file.write(filedata)
  print("total %d replaced" % freq)
