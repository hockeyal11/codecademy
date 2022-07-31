import time

class Player_one:
    def __init__(self, name, x_or_o):
        self.name = name
        self.x_or_o = x_or_o
    def __repr__(self):
        return f"{self.name} is Player 1 and is using {self.x_or_o}!"

class Player_two:
    def __init__(self, name, x_or_o):
        self.name = name
        self.x_or_o = x_or_o
    def __repr__(self):
        return f"{self.name} is Player 2 and is using {self.x_or_o}!"

name_1 = input('What is your name?: ')
time.sleep(2.0)
x_or_o_1 = input("Do you want to be X's or O's?: ")
time.sleep(2.0)
p1 = Player_one(name_1, x_or_o_1)
print(repr(p1))
time.sleep(5.0)
name_2 = input('What is your name Player 2?: ')
x_or_o_2 = ''
if x_or_o_1 == 'X':
    x_or_o_2 = 'O'
else:
    x_or_o_2 = 'X'
time.sleep(2.0)
p2 = Player_two(name_2, x_or_o_2)
time.sleep(2.0)
print(repr(p2))
time.sleep(2.0)
print('''This is Tic-Tac-Toe! Here are the rules. Each player alternates turns to get 3 X\'s or 3 \'s in a row to win the game.
The board is set up like this:''')
time.sleep(10.0)
print('''    
             I     I     
           1 I  2  I  3  
        _____I_____I_____
             I     I     
          4  I  5  I  6  
        _____I_____I_____
             I     I     
          7  I  8  I  9  
             I     I     ''')
time.sleep(5.0)
print('Use the numbers in each space to place your X or O in their spot! Good luck and have fun!')
