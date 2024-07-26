def LemonadeChallange(bills:list[int])->bool:
    # res
    if bills[0]!=5:
        return False
    
    tens,fives=0,0
    k=0
    for i in bills:
        if i==5:
            fives+=1
            print("true1")
        elif i==10:
            if fives<1:
                print("false1")
                return False
            fives-=1
            tens+=1
            print("true2")
        elif i==20:
            if tens==0 or fives<1:
                if fives<3:
                    print("false2")
                    return False
                fives-=3
            else:
                tens-=1
                fives-=1
                print("true3")
        k+=1
    return True
print(LemonadeChallange([5,5,10,10,20]))

# TC: O(n)
# SC: 0