import random
words = ["python","hello","easy","superb","good","ice","lava"]
def display():
  print("#"*30)
  print("Welcome to spoken word guesser")
  print("#"*30,"\n\n\n")
def word_select():
  word_choice = random.choice(words)
  return word_choice

def inp():
  display()
  ori_user_word = word_select()
  user_word = list(ori_user_word)
  lent = len(ori_user_word)
  print("Your word is of",lent,"letters")
  i=0
  counter = 0
  while(i<=lent+1):
    try:
      letter = input("Enter the letter you think is in the word       : ")
      print(user_word)
      for j in range(len(user_word)):
        if letter == user_word[j]:
          print("Letter",letter,"is at index",j)
          counter+=1
          del user_word[j]
      if counter == lent:
        print("Nice !!!! you guessed the letters ")
        print("Word was : ",ori_user_word)
        exit()
    except Exception:
      print(" ")
    finally:
      i+=1
      
  print("You only guessed ",counter,"out of",lent,"letters")
  print("Actual word was ; ",ori_user_word)

inp()
  
