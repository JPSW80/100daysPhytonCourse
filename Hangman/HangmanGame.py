#Step 1 
import random;
import hangman_art;
import  hangman_words;


#Choose a random world from the list
chosen_word=random.choice(hangman_words.word_list)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

from hangman_art import logo
print(logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display.
display=[]

#For each letter in the chosen_word, add a "_" to 'display'.
word_length=len(chosen_word)
for _ in range(word_length):
  display += "_"
print(display)

#create a while loop
end_of_game = False
while not end_of_game: 
  guess = input("Hello my friend! Guess a letter: ").lower()
  
  if guess in display:
    print(f" You've already guessed {guess}")

  for position in  range(word_length):
    letter = chosen_word[position]
    
    #print(f"Current position: {position}\n Current letter: {letter} \n Guessed letter: {guess}")
    if letter==guess:
      display[position]= letter
  print(display)
  

  #TODO-2: - If guess is not a letter in the chosen_word,
  #Then reduce 'lives' by 1. 
  if guess not in chosen_word:
    lives-= 1
    if lives<0:
      end_of_game=True
      print("You lose")
  #If lives goes down to 0 then the game should stop and it should print "You lose."

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")
  
  if "_" not in display:
    end_of_game=True
    print("You win.")
    
 #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
  print(hangman_art.stages[lives])