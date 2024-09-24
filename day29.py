color = input("What is your favorite color? ")
print()
word = input("What is your favorite type of animal? ")
print()
def newprint(color, word):
  if color == "red":
    print("with my new program I can just call the ", "\033[31m","color", "\033[0m", " and the word will appear in the color i called example:" "\033[31m", word, sep = "")
    
  elif color == "blue":
    print("with my new program I can just call the ", "\033[32m","color", "\033[0m", " and the word will appear in the color i called example:" "\033[32m", word, sep="")
    
  elif color == "blue":
    print("with my new program I can just call the ", "\033[34m","color", "\033[0m", " and the word will appear in the color i called example:" "\033[34m", word, sep="")
    
  else:
    print("with my new program I can just call the ", "\033[0m","color", "\033[0m", " and the word will appear in the color i called example:" "\033[0m", word, sep="")

newprint(color, word)