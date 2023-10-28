
# Spencer Gaffin
# Python Scrabble Word Checker

# Checks if a word is playable by asking the Scrabble Merriam dictionary online.
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
    
    while game == True:
        # Gets word from user
            while True:
                try:                   
                    user_word = str(input("What's your word? "))                   
                    word_length = len(user_word)
                    if word_length > 0:
                        main_score = score_calc(user_word)
                        print(user_word, "is worth", main_score, "points")
                        break
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
                    elif dict_check.lower() == "n":
                        break
                    else:
                        print("Not accepted")
                        continue
                except KeyError:
                    print("Not accepted!")
                    continue
                break

def new_func(user_word):
    main_score = score_calc(user_word)
    return main_score 

# Tallies points
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