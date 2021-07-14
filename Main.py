import random
from collections import Counter

sched = [[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
         [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
         [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
         [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
         [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]]

em = ["A","B","C","D", "E", "F", "J"]

def reset_list():
    em = ["A","B","C","D", "E", "F", "J"]
    return em

def print_schedule(sched):
    for i in range(len(sched)):
        print(sched[i])
        print(" ")
        
def assign(sched):
    
    find = find_empty(sched)
    if not find:
        return True
    else:
        row, col = find
    
    em = reset_list()
    random.shuffle(em)
    for choice1, choice2 in zip(em[0::2], em[1::2]):
        if condition(sched, [choice1, choice2], row, col):
            if col == 4:
                sched[row][col][0] = choice1
                sched[row][col][1] = choice1
            else:
                sched[row][col][0] = choice1
                sched[row][col][1] = choice2
            
            if assign(sched):
                return True
            
            sched[row][col][0] = 0
            #assign(sched)
        
                
    return False
        
# List of all conditions when assigning to our schedule
def condition(sched, choice, day, shift):
    # condition 1: employee cannot work both early and late shift
    if (shift == 5 and choice[0] in sched[day][0]) or (shift == 5 and choice[1] in sched[day][0]):
        print("Err1")
        return False
    
    # cannot work two shifts back to back
    if (shift > 0 and choice[0] in sched[day][shift-1]) or (shift > 0 and choice[1] in sched[day][shift-1]):
        print("Err2")
        return False
    
    # Irina only works after X Time
    if shift < 4 and choice == "C":
        print("Err3")
        return False
    
    # Can only work 2 shifts a day
    new_list = []
    for i in range(len(sched[day])):
        for j in sched[day][i]:
            new_list.append(j)
            
    choice1 = choice[0] 
    choice2 = choice[1]       
    if (Counter(new_list).get(choice1) == None) or (Counter(new_list).get(choice2) == None):
        return True
    
    elif (Counter(new_list).get(choice1) > 2) or (Counter(new_list).get(choice2) > 2):
        print("Err4")
        return False
    
    
    return True

# find an unassigned shift spot
def find_empty(sched):
    for i in range(len(sched)):
        for j in range(len(sched[0])):
            if sched[i][j][0] == 0:
                return (i,j)    
    return None
        
       

print_schedule(sched)
assign(sched)
print("______________")
print_schedule(sched)
