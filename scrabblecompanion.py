
# Spencer Gaffin
# Python Scrabble Scorekeeper Companion

# Helps to keep score of a physical scrabble game. Checks if a word is playable by asking the Scrabble Merriam dictionary online.
# Use ! for the blank tile.

# In order to run, several additions may need to be installed in the terminal:
# (For Windows:)
# pip install beautifulsoup 4
# pip install requests
# pip install lxml

from bs4 import BeautifulSoup
import requests

game = True
def play():
    # Creates dictionary to hold names and scores
    while True:
        try:
            player_names = str(input("Enter player names"+
             " separated by a comma: "))
            input_dict = player_names.split(',')
            # Name of dictionary is d
            d = {}
            for i in input_dict:
                d[i.strip()] = 0
            dLength = len(d)
            # d has to have between 2 and 4 names
            if dLength >= 2 and dLength <= 4:
                break
            else:
                print("Enter a number of players between 2 and 4")
        except ValueError:
            print("Not accepted!")
            continue
    print(d)

##################################################################
    
    while game == True:
        for j in d:
        # Gets word from user
            while True:
                try:                   
                    user_word = str(input(j+", what's your word? "))                   
                    word_length = len(user_word)
                    if word_length > 0:
                        main_score = score_calc(user_word)
                        d[j] += main_score
                        print(user_word, "is worth", main_score, "points")
                        print(d) 
                        break
                    #elif user_word.lower() == "end game":
                        #print("Good Game!")
                        #game = False
                    else:
                        print("Not accepted")
                        continue
                except KeyError:
                    print("Enter a word!")
                    continue
                        
            # Optional word check to online dictionary
            while True:
                try:
                    dict_check = str(input("Would you like to look up your word in the scrabble dictionary? (y or n) "))
                    if dict_check.lower() == "y":
                        check = word_check(user_word)
                        print("I looked it up in the Merriam-Webster",
                        " Scrabble Dictionary and found that ", 
                        str(check).lower(), ".", sep="")

                        # If the word is not in the dictionary, gives the option to delete
                        if (str(check).lower()[-19:]) == "not a playable word":
                            while True:
                                try:
                                    delete_check = str(input("Would you like to delete the word? Skips your turn as a penalty! (y or n) "))
                                    if delete_check.lower() == "y":
                                        main_score = score_calc(user_word)
                                        d[j] -= main_score
                                        print(d)
                                        break
                                    elif delete_check.lower() == "n":
                                        break
                                    else:
                                        print("Not accepted")
                                        continue
                                except KeyError:
                                    print("Not accepted!")
                                    continue            
                    elif dict_check.lower() == "n":
                        break
                    else:
                        print("Not accepted")
                        continue
                except KeyError:
                    print("Not accepted!")
                    continue
                break
            

            while True:
                try:
                    # Checks if extra points are needed
                    extra_check = str(input(str(j)+
                            ", does your word have a letter"+
                            " score or word score? (y or n) "))
                    if extra_check.lower() == "y":

                        # Letter score
                        let_score_value = 1
                        while True:
                            try:
                                letter_extra = str(input("Do you have a letter"+ 
                                                        " score? (y or n) "))
                                if letter_extra.lower() == "y":
                                    num_of_let_score = int(input("How many letters have a letter score? "))
                                    for k in range(0, num_of_let_score):
                                        letter = str(input("What's the letter? (Enter 1 letter): "))
                                        if len(letter) > 1 or len(letter) < 1:
                                            print("Enter 1 letter!")
                                        try:
                                            let_score_value = int(input("What's the letter score? (2 or 3) "))
                                            if main_score == 0:
                                                let_score_value = 0
                                                
                                            elif let_score_value == 2 or let_score_value == 3:
                                                main_score += let_score_calc(letter, let_score_value)
                                                d[j] = main_score
                                                print(d)
                                                continue
                                                
                                            else:
                                                print("Not accepted!")
                                                continue
                                        except KeyError:
                                           print("Not accepted")
                                           continue
                                    break
                                elif letter_extra.lower() == "n":
                                    break
                                else:
                                    print("Not accepted")
                                    continue
                            except KeyError:
                                print("Not accepted!")
                                continue
                        
                        

                        # Word Score
                        while True:
                            try: 
                                word_extra = str(input("Do you have a word score? (y or n) "))
                                if word_extra.lower() == "y":
                                    while True:
                                        try:
                                            word_score_value = int(input("What's the word score? (2 or 3) "))
                                            if word_score_value == 2 or word_score_value == 3:
                                                #main_score
                                                main_score = main_score*word_score_value
                                                d[j] = main_score
                                                print(d)
                                                break
                                            else:
                                                print("Not accepted!")
                                        except KeyError:
                                            print("Not accepted")                                   
                                elif word_extra.lower() == "n":
                                    break
                                else:
                                    print("Not accepted!")
                                    continue 
                            except KeyError:
                                print("Not accepted!")
                                continue
                            break
                    elif extra_check.lower() == "n":
                        print(d)
                        break
                    else:
                        print("Not accepted!")
                        continue
                except KeyError:
                    print("Enter y or n!")
                    continue   
                break
          

def new_func(user_word):
    main_score = score_calc(user_word)
    return main_score 

def scoreboard(dictionary):
    for i in dictionary:
        print

def let_score_calc(letter, score_value):
    total = 0
    total += score[letter.lower()]
    return (total*score_value) - score[letter.lower()]

def score_calc(word):
    total = 0
    for i in word:
        total += score[i.lower()]  
    return total

# word check uses beautifulsoup to look up word online
def word_check(word):
    url = "http://scrabble.merriam.com/finder/" + word
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    try:
        result = soup.find("div", class_ = "play_area play_yes").text.strip()
    except AttributeError:
        result = soup.find("div", class_ = "play_area play_no").text.strip()      
    return result

# score holds values for letters, ! is used as a blank tile
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10, "!": 2}
    
def main():
    play()


main()