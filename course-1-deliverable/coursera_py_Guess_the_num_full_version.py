import simplegui
import random

def range5():
    global low, high, comp_num, max_num, attem
    low, high, max_num, attem = 0,5,3,0
    comp_num = random.randrange(low,high)
    print ('you are playing in the range 0-5')
    print ('you have 3 attempts')
    return comp_num

def range10():
    global low, high, comp_num, max_num, attem
    low, high, max_num, attem = 0,10,5,0
    comp_num = random.randrange(low,high)
    print ('you are playing in the range 0-10')
    print ('you have 5 attempts left')

def game(num):
    guess_number = int(num)
    global comp_num, max_num, attem
    attem += 1
    if max_num - attem != -1:
        if guess_number > comp_num:
            print ('guess is high')
            print ('attempts left: ' + str(max_num - attem))
        elif guess_number < comp_num:
            print ('guess is low')
            print ('attempts left: ' + str(max_num - attem))
        elif guess_number == comp_num:
            print ('you have won the game!')
            print ('attempts left: ' + str(max_num - attem))
    else:
            print ('you have used all your attempts! time for new game!')


f = simplegui.create_frame("Guess the number Game", 300, 300)
f.add_button("range: 0 - 5", range5, 200)
f.add_button("range: 0 - 10", range10, 200)
f.add_input("enter the number",game,200)


f.start()
