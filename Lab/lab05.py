'''
    Week 2 Lab 5 by Lieutenant Sadder
    Making MatchingGame : เกมต่อคำ
    There are 3 function P R and X
    P(item) use to chk if last 2 characters of previous word == first 2 characters of next words
        then add the word to the list
        if not the game will be over
    R() use to Restart game
    X() use to Exit the game 

    Test Cases:
    (1) *** TorKham HanSaa ***
        Enter Input : P Apple,P LEMON,R,P onion,X
        'Apple' -> ['Apple']
        'LEMON' -> ['Apple', 'LEMON']
        game restarted
        'onion' -> ['onion']

    (2) *** TorKham HanSaa ***
        Enter Input : P apple,p lemon,P onion,X
        'apple' -> ['apple']
        'p lemon' is Invalid Input !!!

    (3) *** TorKham HanSaa ***
        Enter Input : P apPLE,P leMON,R,P Durian,P ant,P pineapple,X
        'apPLE' -> ['apPLE']
        'leMON' -> ['apPLE', 'leMON']
        game restarted
        'Durian' -> ['Durian']
        'ant' -> ['Durian', 'ant']
        'pineapple' -> game over

    (4) *** TorKham HanSaa ***
        Enter Input : R,R,P KK,R,P apple,R,P Lemon,R,X
        game restarted
        game restarted
        'KK' -> ['KK']
        game restarted
        'apple' -> ['apple']
        game restarted
        'Lemon' -> ['Lemon']
        game restarted

    (5) *** TorKham HanSaa ***
        Enter Input : P apple,P lemon,P nectarine,X
        'apple' -> ['apple']
        'lemon' -> ['apple', 'lemon']
        'nectarine' -> game over
'''
class matchGame:

    def __init__(self):
        self.words = []
        self.count = 0

    def chk(self,lst):
        if (lst[0] == 'P') or (lst[0] == 'R') or (lst[0] == 'X'):
            return 1
        else:
            return 0

    def P(self,item):
        if self.count > 0:
            if item[2:] in self.words: #Same Word
                print("'"+item+"' is Invalid Input !!!")
                self.X()
            elif self.words[self.count-1][-2:].lower() == item[2:4].lower() : #Matching
                self.words.append(item[2:])
                print("'"+self.words[self.count]+"' ->",self.words)
                self.count = self.count + 1
            else: #Not Match
                print("'"+item[2:]+"' -> game over")
                self.X()
        else:
            self.words.append(item[2:])
            print("'"+self.words[self.count]+"' ->",self.words)
            self.count = self.count + 1

    def R(self):
        self.words = []
        self.count = 0
        print('game restarted')

    def X(self):
        quit()

    def solve(self, iTem):
        if iTem[0] == 'P':
            self.P(iTem)
        elif iTem[0] == 'R':
            self.R()

print('*** TorKham HanSaa ***')
game = matchGame()
words = [c.strip() for c in (input('Enter Input : ').split(','))]
for item in words:
    if game.chk(item) == 0:
        print("'"+item+"' is Invalid Input !!!")
        break
    elif item[0] == 'X':
        game.X()
        quit()
    else:
        game.solve(item)