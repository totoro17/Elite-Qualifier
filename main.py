#C2C Elite Qualifier Assignment, Tori Schulz, Dec. 2020

from termcolor import colored, cprint
import random
import time
import emojis

class chat:
  def __init__(self, bot_name):

    self.bot_name = bot_name   # game persona name
    self.name = None           # user's name
    self.emoji_mode= None           # sets a mode 
    self.color = "grey"        # the initial text color

    self.yeehaw_emoji = [emojis.encode(':cow:' ),emojis.encode(':chicken:'), emojis.encode(':corn:'), emojis.encode(':rooster:'), emojis.encode(':goat:'), emojis.encode(':pig:'), emojis.encode(':pig2:'),emojis.encode(':cactus:'), emojis.encode(':tractor:'), emojis.encode(':us:')]

    self.hippie_emoji = [emojis.encode(':herb:'),emojis.encode(':sunflower:'),emojis.encode(':mushroom:'),emojis.encode(':seedling:'),emojis.encode(':sun_with_face:'), emojis.encode(':snail:'),emojis.encode(':v:'), emojis.encode(':crystal_ball:'), emojis.encode(':earth_americas:')]

    self.surferbro_emoji = [emojis.encode(':tropical_fish:'),emojis.encode(':sunglasses:'),emojis.encode(':v:'),emojis.encode(':ocean:'),emojis.encode(':fish:'), emojis.encode(':shell:'), emojis.encode(':sailboat:'), emojis.encode(':anchor:'), emojis.encode(':surfer:')]

    #questions to ask user
    self.userinformation = {"home" : "Where are you from?", 'mode' : "Would you like surfer dude mode, hippie mode, or yeehaw mode? Please reply with 'bro', 'hippie', or 'yeehaw'.", "fav_color" : "What is your favorite color? \n*If your favorite color happens to be 'blue', 'green', 'cyan', 'yellow', 'red', or 'magenta' then you are in for a treat!*"} 

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

    if self.userinformation["mode"].lower() == 'bro':
      self.emoji_mode = self.surferbro_emoji
    elif self.userinformation["mode"].lower() == 'hippie':
      self.emoji_mode = self.hippie_emoji
    elif self.userinformation["mode"].lower() == 'yeehaw':
      self.emoji_mode = self.yeehaw_emoji
    else:
      cprint("\nI regret to inform you that your mode selection above was not valid. You have automatically been set to yeehaw mode", self.color, "on_white")
      self.emoji_mode = self.yeehaw_emoji
      

    bobquestion = self.getinput(self.emoji_mode[0] + " What a coincidence, I'm from " + self.userinformation["home"] + " too! Do you happen to know Bob? (Reply 'yes' or 'no')", 1)

    if bobquestion == "yes" or bobquestion == "Yes":
      cprint("\n" + self.emoji_mode[1] + " Small world huh? Bob is really a great fella." , self.color, "on_white")

    elif bobquestion == "no" or bobquestion == "No":
      cprint("\n" + self.emoji_mode[1] + " I never cared for Bob too much myself.", self.color, "on_white")

    else:
      cprint("\n" + self.emoji_mode[1] + " Sorry I can't quite comprehend your answer to my question. In the future, please reply in the way I ask. I'm still learning. Anyways, moving on! ", self.color, "on_white")

    self.getinput(self.emoji_mode[2] + " Beep...boop... My systems have finished calibrating and the chat is now catered to you. Anyways, what are your feelings on that big global important economic matter going on? ", 1)

    time.sleep(1)
    print()
    cprint(self.emoji_mode[3] + " You make some really great points " + self.name + ".", self.color, "on_white")
    gameanswer = self.getinput(self.emoji_mode[4] + " Would you like to play a quick little game?" + " Reply 'yes' or 'no'", 1)

    if gameanswer == "yes" or gameanswer == "Yes" or gameanswer == "YES":
      time.sleep(1)
      print()
      cprint(self.emoji_mode[5] + " Awesome! Lets do this thing.", self.color, "on_white")
      self.quickgame()
    else:
      time.sleep(1)
      cprint("\n" + self.emoji_mode[5] + "Well we are going to play anyways.", self.color, "on_white")
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
    weatherquestion = self.getinput(self.emoji_mode[6] + " Impressive guessing skills " + self.name + ". Why don't you go ahead and ask me about the weather? ", 1)

    if "weather" in weatherquestion or "Weather" in weatherquestion:
      time.sleep(1)
      cprint("\n" + self.emoji_mode[7] + " Haha, I have fooled you again " + self.name + "! How can I know the weather? I am nothing but a series of numbers trapped inside this cold metal shell.", self.color, "on_white")
    else:
      time.sleep(1)
      cprint(self.emoji_mode[7] + " I like you, you little rebel. Going against the flow, good for you " + self.name + ".", self.color, "on_white")

    time.sleep(2)
    cprint("\n" + self.emoji_mode[8] + "I'm so sorry to cut our chat short but I'm running late for my software appointment. I've been feeling so strange lately since people just keep on pushing my buttons. Check ya later!", self.color, "on_white")
    exit()


  
if __name__ == '__main__':
  #initializes a new chatbot with chosen name
  chatbot = chat("Chatty McChatface")
  #begins the conversation
  chatbot.introduction()





