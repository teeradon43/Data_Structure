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
        # self.words.append('One')
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
    # print(item,item.__contains__(' '))
    if game.chk(item) == 0:
        print("'"+item+"' is Invalid Input !!!")
        break
    elif item[0] == 'X':
        game.X()
        quit()
    else:
        game.solve(item)

# print(words)