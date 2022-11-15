from random import randint

def get_shot():

    ok = "n"
    while ok == "n":
        try:
            shot = input("please enter your guess")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("incorrect number, please try again")
            else:
                ok = "y"
                break
        except:
            print("incorrect entry - please try again")    

    return shot        

def show_board(hit,miss,comp):
    print("  Welcome to our Battleship Game     ")
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ " 
            if place in miss:
                ch = " x "
            elif place in hit:
                ch = " o "
            elif place in comp:
                ch = " 0 "

            row = row + ch 
            place = place + 1
        print (x," ", row)   

def check_shot(shot,boat1,boat2,hit,miss,comp):

    if shot in boat1:
        boat1.remove(shot)     
        if len(boat1) > 0:
            hit.append(shot)
        else:
            comp.append(shot)     

    elif shot in boat2:
        boat1.remove(shot)     
        if len(boat2) > 0:
            hit.append(shot)
        else:
            comp.append(shot)    
    else:
        miss.append(shot)        

    return boat1,boat2,hit,miss,comp


boat1 = [36,46,47]
boat2 = [5,15,25]
hit = []
miss = []
comp = []

for i in range(15):
     guesses = hit + miss + comp
     shot = get_shot()
     boat1,boat2,hit,miss,comp = check_shot(shot,boat1,boat2,hit,miss,comp)
     show_board(hit,miss,comp)  

     if len(boat1) < 1 and len(boat2) < 1:
        print("you've won")     
        break
print ("finished")    
