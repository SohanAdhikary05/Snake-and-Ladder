#automated snake and ladder game @SOHAN ADHIKARY
import random
import time
board={0:'start',1: 'go to 38', 2: '2', 3: '3', 4: 'go to 14', 5: '5', 6: '6', 7: '7', 8: 'go to 30', 9: '9', 10: '10', 11: '11', 12: '12', 13: '13', 14: '14', 15: '15', 16: '16', 17: '17', 18: '18', 19: '19', 20: '20', 21: 'go to 42', 22: '22', 23: '23', 24: '24', 25: '25', 26: '26', 27: '27', 28: 'go to 76', 29: '29', 30: '30', 31: '31', 32: 'down to 10', 33: '33', 34: '34', 35: '35', 36: 'down to 6', 37: '37', 38: '38', 39: '39', 40: '40', 41: '41', 42: '42', 43: '43', 44: '44', 45: '45', 46: '46', 47: '47', 48: 'down to 26', 49: '49', 50: 'go to 67', 51: '51', 52: '52', 53: '53', 54: '54', 55: '55', 56: '56', 57: '57', 58: '58', 59: '59', 60: '60', 61: '61', 62: 'down to 18', 63: '63', 64: '64', 65: '65', 66: '66', 67: '67', 68: '68', 69: '69', 70: '70', 71: 'go to 92', 72: '72', 73: '73', 74: '74', 75: '75', 76: '76', 77: '77', 78: '78', 79: '79', 80: 'go to 99', 81: '81', 82: '82', 83: '83', 84: '84', 85: '85', 86: '86', 87: '87', 88: 'down to 24', 89: '89', 90: '90', 91: '91', 92: '92', 93: '93', 94: '94', 95: 'down to 56', 96: '96', 97: 'down to 78', 98: '98', 99: '99', 100: 'WON'}
def poscheck(a):
    v=board[a]
    if len(v)>3:
        if v[0]=='g':
            print("YESS LADDER")
        else:
            print("OH NO SNAKE")
        p=v[-2:]
        if p[0]==' ':
            return v[-1]
        else:
            return p
    return v
tct=0
pnt=0
actpos=0
ch="no"
while ch=="no":
    ch=input("Ready player one ? ").lower()
while 1>0:
    n=int(input("How many times do you want to shake the dice? "))
    time.sleep(1)
    for i in range(n):
        pnt=random.randint(1,6)
    print("Points earned ",pnt)
    tct+=1
    actpos=actpos+pnt
    if actpos>100:
        actpos-=pnt
        continue
    if actpos==100:
        print("WON")
        break
    actpos=int(poscheck(actpos))
    print("Now at : ",actpos)
print("MOVES REQUIRED TO WIN : ",tct)    
