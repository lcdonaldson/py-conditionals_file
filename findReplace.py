# fot single replacements

import os

textToFind = "white"
textToReplace = "#FFF"
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
  
#  -------------------------------------------------------------

# For multiple replacements
import re
import os 

whiteText = 'white'
offWhite = '#D7E1E7'
greyText = '#444'
blackBg = 'black'
sourcePath = os.listdir('/Users/levi/Desktop/CODE/code_practice/Regex/python/static/')
for file in sourcePath:
  inputfile = '/Users/levi/Desktop/CODE/code_practice/Regex/python/static/' + file
  print('converting' + inputfile)
  with open(inputfile, 'r') as inputfile:
    filedata = inputfile.read()

  fileToChange = '/Users/levi/Desktop/CODE/code_practice/Regex/python/static/' + file
  if whiteText == 'white':
    newText = '#FFF'
    filedata = filedata.replace(whiteText, newText)
    print('changed white to #FFF')

  if offWhite == '#D7E1E7':
    newText = '#FFF'
    filedata = filedata.replace(offWhite, newText)
    print('changed offwhite to #FFF')

  if greyText == '#444':
    newText = 'grey'
    filedata = filedata.replace(greyText, newText)
    print('changed #444 to grey')
    
  if blackBg == 'black':
    newText = '#000000'
    filedata = filedata.replace(blackBg, newText)
    print('changed black to #000000')  
    
  with open(fileToChange, 'w') as file:
    file.write(filedata)
