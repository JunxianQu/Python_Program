import json
from difflib import get_close_matches
from difflib import SequenceMatcher

data = json.load(open("data.json"))


# Translate function
def translate(word):
  w = word.lower()
  if w in data:    # find the word and output its definition
    return data[w]
  elif w.upper() in data: #in case user enters words like USA or NATO
    return data[w.upper()]
  closew = get_close_matches(w, data.keys())  # otherwise, find the closest word
  if len(closew) > 0:
    print( "Do you mean this word: %s? Y:yes   N: no" %closew[0] ) # confirmation by inputer
    while True:
      coninput = input()
      if coninput == 'Y':
        return data[closew[0]]
      elif coninput == 'N':
        return "Cannot find the word."
      else:
        "illegal input. Y:yes   N: no"
  else:
    return "Cannot find the word."

# output function
def output(word):
  if type(word) == list:  # to eliminate the square bracket
    for i in word:
      print(i)
  else:
    print(word)

while True:
  word = input("Enter the word: (type \"end\" to quit) ")
  if word == "end":
    break
  output(translate(word))