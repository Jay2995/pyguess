import art
import random
def play_game():
  print(art.logo);
  easy_mode_attempts = 5;
  hard_mode_attempts = 10;
  list_of_numbers = [];
  random_number = 0;
  
  
  ############
  for n in range(1,101):
    list_of_numbers.append(n);
  #functions
  def random_number_picker():
    number = random.choice(list_of_numbers);
    return number;
    
  random_number = random_number_picker()
  
  def check():
      if easy_mode_attempts <= 0 or hard_mode_attempts <= 0:
          return True
      return False
    
  print("Welcome to the number guessing name.");
  print(f"Im thinking of a number between 1 and {n}");
  print(f"psst , the correct answer is {random_number}");
  
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ");
  is_playing = True;
  
  
  while is_playing:
    
    if difficulty == 'easy':
      print(f"You have {easy_mode_attempts} remaining to guess the number.");
    elif difficulty == "hard":
      print(f"You have {hard_mode_attempts} remaining to guess the number.");
    else:
      print("Invalid difficulty, please choose easy or hard");
      break
      
    guess = int(input("Make a guess: "));
  
    if guess == random_number:
      print(f"You got it the answer was {guess}");
      is_playing = False;
    elif guess < random_number:
      print("Too low");
      if difficulty == "easy":
        easy_mode_attempts -= 1; 
      elif difficulty == "hard":
        hard_mode_attempts -= 1;
    elif guess > random_number:
      print("Too big")
      if difficulty == "easy":
        easy_mode_attempts -= 1; 
      elif difficulty == "hard":
        hard_mode_attempts -= 1;
  
    if check():
      print("Out of attempts, game over.");
      is_playing = False;
      
  play_again = input("Do you want to play again?: ").lower();
  if play_again == "yes":
    play_game();
  
play_game();
