
def main():
  print(greet(input("Greeting: ")))


def greet(sentence):
  sentence=sentence.lower()
  if sentence.startswith("hello"):
     return 0
  elif sentence.startswith("h"):
     return 20
  else:
     return 100        
  
main()






