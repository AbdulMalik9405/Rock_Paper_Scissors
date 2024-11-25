import random
import getpass

UserPoints = 0
CompPoints = 0
P1Points = 0
P2Points = 0

GameType = input("Do you want to play against a computer or another player (computer/player)")
GameType = GameType.lower()

def player_name():
  valid = False
  while valid == False:
    try:
      name = input("Player, what is your name?")
      if name.isalpha() == True:
        valid = True
      else:
        raise ValueError
    except ValueError:
      print("Please enter a valid name")
      valid = False
  return name
  
def player_input(name):
  print(name, "it is your turn")
  choice = getpass.getpass(prompt = 'input rock, paper or scissors.')
  choice = choice.lower()
  return choice

def file_write(name):
  f = open("GameResults.txt", "a")
  if name == "No One":
    f.write("It was a Draw\n")
  else:
    f.write(name  + " won\n")
  f.close()

def winner(a, b):
  if a > b:
    return a
  elif b > a:
    return b
  else:
    print("It was a draw")

if GameType != "player" and GameType !="computer":
  print("invalid input")
  ContinuePlay = False

elif GameType == "player":
  player1 = player_name()
  player2 = player_name()
  f = open("GameResults.txt", "w")
  ContinuePlay = True
  
  while ContinuePlay == True:
    p1 = player_input(player1)
    if p1 != "rock" and p1 != "paper" and p1 != "scissors":
      print("Invalid input. Please choose rock, paper, or scissors.")
      continue
    p2 = player_input(player2)
    if p2 != "rock" and p2 != "paper" and p2 != "scissors":
      print("Invalid input. Please choose rock, paper, or scissors.")
      continue
    elif p1 == p2:
      print("Draw")
      file_write("No One")
    elif (p1 == "rock" and p2 == "scissors") or (p1 == "paper" and p2 == "rock") or (p1 == "scissors" and p2 == "paper"):
      print(player1, "Wins")
      P1Points = P1Points + 1
      file_write(player1)
    else:
      print(player2, "Wins")
      P2Points = P2Points + 1
      file_write(player2)
    
    Continue = input("Do you want to continue?")
    Continue = Continue.lower()
    if Continue == "no":
      ContinuePlay = False
    elif Continue != "yes":
      print("invalid input")

  print(player1, "won", P1Points, "points")
  print(player2, "won", P2Points, "points")
  winner = winner(player1, player2)
  if winner == "a":
    print(player1, "won")
  else:
    print(player2, "won")

else:
  f = open("GameResults.txt", "w")
  ContinuePlay = True
  while ContinuePlay == True:
    UserChoice = input("rock, paper, or scissors? ")
    UserChoice = UserChoice.lower()
    if UserChoice != "rock" and UserChoice != "paper" and UserChoice != "scissors":
      print("Invalid input. Please choose rock, paper, or scissors.")
      continue
  
    CompChoice = random.randint(1,4)
    if CompChoice == 1:
      CompChoiceText = "rock"
    elif CompChoice == 2:
      CompChoiceText = "paper"
    else:
      CompChoiceText = "scissors"
  
    print("Computer chose", CompChoiceText)

    if UserChoice == CompChoiceText:
      print("Draw")
      f = open("GameResults.txt", "a")
      f.write("It was a draw\n")
      f.close()
    elif (UserChoice == "rock" and CompChoiceText == "scissors") or (UserChoice == "paper" and CompChoiceText == "rock") or (UserChoice == "scissors" and CompChoiceText == "paper"):
      print("User Wins")
      UserPoints = UserPoints + 1
      f = open("GameResults.txt", "a")
      f.write("User won\n")
      f.close()
    else:
      print("Computer Wins")
      CompPoints = CompPoints + 1
      f = open("GameResults.txt", "a")
      f.write("Computer won\n")
      f.close()

    Continue = input("Do you want to continue?")
    Continue = Continue.lower()
    if Continue == "no":
      ContinuePlay = False
    elif Continue != "yes":
      print("invalid input")
      
  print("User Points:", UserPoints)
  print("Computer Points:", CompPoints)
  winner = winner(CompPoints, UserPoints)
  if winner == "a":
    print("User won")
  else:
    print("Computer Won")