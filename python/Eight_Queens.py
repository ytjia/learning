#Print out a random solution

def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0, nextY-i):
            return True
    return False
    
def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)
    for pos in solution:
        print line(pos)
        
import random
while True:
    number = input('Input the number of your queens:')
    if number == -1:
        break
    try:
        prettyprint(random.choice(list(queens(number))))
    except Exception:
        print 'No possible solution!'
