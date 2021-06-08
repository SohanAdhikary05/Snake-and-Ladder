import random
import time
board={0:'start',1: 'L to 38', 2: '2', 3: '3', 4: 'L to 14', 5: '5', 6: '6', 7: '7', 8: 'L to 30', 9: '9', 10: '10', 11: '11', 12: '12', 13: '13', 14: '14', 15: '15', 16: '16', 17: '17', 18: '18', 19: '19', 20: '20', 21: 'L to 42', 22: '22', 23: '23', 24: '24', 25: '25', 26: '26', 27: '27', 28: 'L to 76', 29: '29', 30: '30', 31: '31', 32: 'S to 10', 33: '33', 34: '34', 35: '35', 36: 'S to 6', 37: '37', 38: '38', 39: '39', 40: '40', 41: '41', 42: '42', 43: '43', 44: '44', 45: '45', 46: '46', 47: '47', 48: 'S to 26', 49: '49', 50: 'L to 67', 51: '51', 52: '52', 53: '53', 54: '54', 55: '55', 56: '56', 57: '57', 58: '58', 59: '59', 60: '60', 61: '61', 62: 'S to 18', 63: '63', 64: '64', 65: '65', 66: '66', 67: '67', 68: '68', 69: '69', 70: '70', 71: 'L to 92', 72: '72', 73: '73', 74: '74', 75: '75', 76: '76', 77: '77', 78: '78', 79: '79', 80: 'L to 99', 81: '81', 82: '82', 83: '83', 84: '84', 85: '85', 86: '86', 87: '87', 88: 'S to 24', 89: '89', 90: '90', 91: '91', 92: '92', 93: '93', 94: '94', 95: 'S to 56', 96: '96', 97: 'S to 78', 98: '98', 99: '99', 100: '100'}
def poscheck(a):
    v=board[a]
    if len(v)>3:
        p=v[-2:]
        if p[0]==' ':
            return v[-1]
        else:
            return p
    return v
print("WELCOME TO THE SNAKES AND LADDERS")
print("-----------THE BOARD-------------")
ct=100
for i in range(10):
    if ((i+1)%2==1):
        for j in range(ct,ct-10,-1):
            print(board[j],end="\t")   
    else:
        for j in range(ct-9,ct+1):
            print(board[j],end="\t") 
    ct-=10
    print("")
while(1>0):
    n=int(input("Enter the number of players (max 6) : "))
    if n>6:
        print("MAXIMUM 6 allowed!")
        continue
    else:
        break
    
tct=[]
pnt=[]
actpos=[]
for i in range(n):
    tct.append(0)

    pnt.append(0)
    actpos.append(0)
for i in range(1,n+1):
    print("Player ",i,end="\t")
while not(100 in actpos):
    print("")
    for i in range(n):
        pnt[i]=random.randint(1,6)
        tct[i]=tct[i]+1
        actpos[i]=actpos[i]+pnt[i]
        if actpos[i]>100:
            actpos[i]-=pnt[i]
        actpos[i]=int(poscheck(actpos[i]))
    for i in range(n):
        print("Points : ",pnt[i],end="\t")
        time.sleep(0.5)
    print("")
    for i in range(n):    
        print("Now at : ",actpos[i],end="\t")
print("")
for i in range(n):
    if actpos[i]==100:
        print("WINNER Player ",i+1)
        print("Number of moves required ",tct[i])

