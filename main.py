#C2C Elite Qualifier Assignment, Tori Schulz, Dec. 2020

from termcolor import colored, cprint
import random
import time

class chat:
  def __init__(self, bot_name):

    self.bot_name = bot_name   # game persona name
    self.name = None           # user's name
    self.mode = None           # sets a mode / add feature later
    self.color = "grey"        # the initial text color
    self.userinformation = {"home" : "Where are you from?", "fav_color" : "What is your favorite color? \n*If your favorite color happens to be 'blue', 'green', 'cyan', 'yellow', 'red', or 'magenta' then you are in for a treat!*"} #questions to ask user
    self.color_options = ["blue", "green", "cyan", "yellow", "red", "grey", "magenta"]  #possible color options to alter text given the users favorite color choice
    
    
  #the introduction function that is called first to begin the chatbot conversation
  #no inputs or outputs
  def introduction(self):
    self.name = self.getinput("Hello, My name is " + self.bot_name + "! What is your name?", 0)

    time.sleep(1)
    cprint("\nIt is nice to meet you " + self.name + "! Remember that if at anytime you wish to end our chat, simply reply 'EXIT' at any time.\n", "grey", "on_white")

    time.sleep(1)
    cprint("To most customize this chat to you in our extremely high tech and advanced systems, I am going to ask you a few questions:", "grey", "on_white")


    for userdata in self.userinformation:
      answer = self.getinput(self.userinformation[userdata], 1)
      self.userinformation[userdata] = answer

    if self.userinformation["fav_color"].lower() in self.color_options:
      self.color = self.userinformation["fav_color"].lower()
    else:
      self.color = "grey"

    bobquestion = self.getinput("What a coincidence, I'm from " + self.userinformation["home"] + " too! Do you happen to know Bob? (Reply 'yes' or 'no')", 1)

    if bobquestion == "yes" or bobquestion == "Yes":
      cprint("\nSmall world huh? Bob is really a great fella.", self.color, "on_white")

    elif bobquestion == "no" or bobquestion == "No":
      cprint("\nI never cared for Bob too much myself.", self.color, "on_white")

    else:
      cprint("\nSorry I can't quite comprehend your answer to my question. In the future, please reply in the way I ask. I'm still learning. Anyways, moving on!", self.color, "on_white")

    self.getinput("Beep...boop... My systems have finished calibrating and the chat is now catered to you. Anyways, what are your feelings on that big global important economic matter going on?", 1)

    time.sleep(1)
    print()
    cprint("You make some really great points " + self.name + ".", self.color, "on_white")
    gameanswer = self.getinput("Would you like to play a quick little game? Reply 'yes' or 'no'", 1)

    if gameanswer == "yes" or gameanswer == "Yes" or gameanswer == "YES":
      time.sleep(1)
      print()
      cprint("Awesome! Lets do this thing.", self.color, "on_white")
      self.quickgame()
    else:
      time.sleep(1)
      cprint("\nWell we are going to play anyways.", self.color, "on_white")
      self.quickgame()


#input: the users input in the conversation
#checks if they input exit and if so, exits game
  def exitcheck(self, input):
    if input == "EXIT" or input == "exit" or input == "Exit":
      cprint("Adios!", "white", "on_red")
      exit(0)


# gets the users input and checks if they want to exit
# input: string with prompt
# output: string of users response
  def getinput(self, message, sleep_time):
    time.sleep(sleep_time)
    cprint("\n" + message, self.color, "on_white")
    response = input()
    self.exitcheck(response)
    return response

#initiates the quick game given the user choice
#no inputs or outputs
  def quickgame(self):
    correctnum = str(random.randrange(1, 10))
    guess = None
    guessednumbers = []
    guess = self.getinput("Guess a number between 1 and 10.", 1)

    while guess != correctnum:
      if guess in guessednumbers:
        print()
        cprint("You may need to get your noggin checked out you have already guessed that.", "red", "on_white")
      if guess.lstrip('-').isdigit() == True:
        if int(guess) <= 0 or int(guess) > 10:
          print()
          cprint("I regret to inform you that number is not between 1 and 10.", "red", "on_white")
          print()     
      else:
        print()
        cprint("That is not an accepted answer type.", "red", "on_white")
      
      guessednumbers.append(guess)
      guess = self.getinput("Try Again.", 0)

    cprint("\nW I N N E R   W I N N E R  C H I C K E N   D I N N E R!!!!!", "grey", "on_green")

    self.continuegame()

#called after the quickgame has been completed to continue conversation
#no inputs or outputs
  def continuegame(self):
    weatherquestion = self.getinput("Impressive guessing skills " + self.name + ". Why don't you go ahead and ask me about the weather?", 1)

    if "weather" in weatherquestion or "Weather" in weatherquestion:
      time.sleep(1)
      cprint("\nHaha, I have fooled you again " + self.name + "! How can I know the weather? I am nothing but a series of numbers trapped inside this cold metal shell.", self.color, "on_white")
    else:
      time.sleep(1)
      cprint("I like you, you little rebel. Going against the flow, good for you " + self.name + ".", self.color, "on_white")

    time.sleep(2)
    cprint("\nI'm so sorry to cut our chat short but I'm running late for my software appointment. I've been feeling so strange lately since people just keep on pushing my buttons. Check ya later!", self.color, "on_white")


  
if __name__ == '__main__':
  #initializes a new chatbot with chosen name
  chatbot = chat("Chatty McChatface")
  #begins the conversation
  chatbot.introduction()





