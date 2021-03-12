import secrets

user = input("enter x or o : ")

if user == 'x':
    comp = 'o'
elif user == 'o':
    comp = 'x'
else:
    print("wrong input from user")
    exit()
new = ['_','_','_','_','_','_','_','_','_']

def pos(x,n): #function that assigns position chosen to the player
    if x == 1 :
        new[0] = n
    elif x == 2:
        new[1] = n
    elif x == 3:
        new[2] = n
    elif x == 4:
        new[3] = n
    elif x == 5:
        new[4] = n
    elif x == 6:
        new[5] = n
    elif x == 7:
        new[6] = n
    elif x == 8:
        new[7] = n
    elif x == 9:
        new[8] = n
    else:
        exit(0)

def won(): #function to determine if there's a winner or not

    if (new[0] == new[1] == new[2] == user) or\
            (new[0] == new[3] == new[6] == user) or\
            (new[0] == new[4] == new[8] == user) or\
            (new[2] == new[4] == new[6] == user) or\
            (new[3] == new[4] == new[5] == user) or\
            (new[6] == new[7] == new[8] == user) or\
            (new[0] == new[4] == new[8] == user) or\
            (new[2] == new[5] == new[8] == user) or\
            (new[1] == new[4] == new[7] == user):
        print("You Won")
        exit(0)
    elif (new[0] == new[1] == new[2] == comp ) or\
            (new[0] == new[3] == new[6] == comp) or\
            (new[0] == new[4] == new[8] == comp) or\
            (new[2] == new[4] == new[6] == comp) or\
            (new[3] == new[4] == new[5] == comp) or\
            (new[6] == new[7] == new[8] == comp) or\
            (new[0] == new[4] == new[8] == comp) or\
            (new[2] == new[5] == new[8] == comp) or\
            (new[1] == new[4] == new[7] == comp):
        print("You loose, computer Wins")
        exit(0)

    elif len(lst) == 0:
        print("It's a Draw ")
        exit(0)
    else:
        pass




lst = [1,2,3,4,5,6,7,8,9]


for iterate in range(1,10): #both computer and user take turns to play in loop
    user_n = int(input("pick a number : "))
    try:
        lst.remove(user_n)
    except Exception as e:
        print('You picked a number not in list', e)
        exit()
    if len(lst) == 0:
        pos(user_n, user)
        pos(comp_n, comp)
        won()

    comp_n = secrets.choice(lst)
    lst.remove(comp_n)


    pos(user_n,user)
    pos(comp_n, comp)
    print('___' + new[0] + '___|___' + new[1] + '___|___' + new[2] + '___')
    print('       |       |       ')
    print('___' + new[3] + '___|___' + new[4] + '___|___' + new[5] + '___')
    print('       |       |       ')
    print('___' + new[6] + '___|___' + new[7] + '___|___' + new[8] + '___')
    print('       |       |       ')
    won()









