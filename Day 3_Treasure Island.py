print("Welcome to Treasure Island.\nYour mission is to find the treasure")
a=input("Move left or right?")
if a=='left':
    b=input("swim or wait")
    if b=='wait':
         c=input("Which door? R, B, Y")
         if c=='R':
             print("Burned by fire.\nGame Over.")
         elif c=='B':
             print("Eaten by beasts.\nGame Over.")
         elif c=='Y':
             print("You Win!")
         else:
             print('game over')


    else:
        print("Attacked by trout.\nGame Over.")

else:
    print("Fall into a hole.\nGame Over.")