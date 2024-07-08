HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
import random
lives=7
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
chosen_word=random.choice(word_list)
chosen_word_list=list(chosen_word)
emptlist=[]+["_"]*len(chosen_word_list)
condidntion=True
print("""                                              
  _
 | |                                            
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                                                                                     
""")
while condidntion:
    letter=input("write letter: ")
    if letter in emptlist:
        print("You already guessed it")
    for a in range(len(chosen_word_list)):
      if chosen_word_list[a]==letter:
        emptlist[a]=letter
      if emptlist.count("_")<1:
        condidntion=False
    if emptlist.count("_")>0:
        display = ' '.join(str(item) for item in emptlist)
        print(display)
    if emptlist.count("_")<1:
      display = ' '.join(str(item) for item in emptlist)
      print(f"{display}\nYou Win")  
    if chosen_word_list.count(letter)<1:
      print(f"{letter} not in the word")
      lives=lives-1
      if lives !=1:
        print(HANGMANPICS[-lives])
    if lives==1:
      print(f"{HANGMANPICS[6]}\nYou lose")
      condidntion=False


