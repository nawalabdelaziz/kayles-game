print("this game is kayles game --> it's about every player choose 1 or 2 numbers and the one who choose the last number wins")
a =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
print(a)
while a!=['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']:
    print("who will start the game player 1 or player 2")
    the_player=int(input())
    while the_player==1: 
       print("player one's turn")
       print("choose one or two numbers")
       choosen_numbers=int(input())
       if choosen_numbers==1:
           print("choose the number from",a)
           a[(int(input()))]='.'
           print(a)
       elif choosen_numbers==2:
           print("choose the two numbers from",a)
           print("choose the first number")
           a[(int(input()))]='.'
           print("choose the second number")
           a[(int(input()))]='.'
           print(a)
       while choosen_numbers!=1 and choosen_numbers!=2:
              print("you're not allow to choose this number please choose 1 or 2")
              choosen_numbers=int(input())
              if choosen_numbers==1:
                 print("choose the number from",a)
                 a[(int(input()))]='.'
                 print(a)
              elif choosen_numbers==2:
                 print("choose the two numbers from",a)
                 print("choose the first number")
                 a[(int(input()))]='.'
                 print("choose the second number")
                 a[(int(input()))]='.'
                 print(a)
       if a==['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']:
           print("player one is the winner")
           break
       print("player two's turn")
       print("choose one or two numbers")
       choosen_numbers=int(input())
       if choosen_numbers==1:
          print("choose the number from",a)
          a[(int(input()))]='.'
          print(a)
       elif choosen_numbers==2:
          print("choose the two numbers from",a)
          print("choose the first number")
          a[(int(input()))]='.'
          print("choose the second number")
          a[(int(input()))]='.'
          print(a)
       while choosen_numbers!=1 and choosen_numbers!=2:
           print("you're not allow to choose this number please choose 1 or 2 ")
           choosen_numbers=int(input())
           if choosen_numbers==1:
              print("choose the number from",a)
              a[(int(input()))]='.'
              print(a)
           elif choosen_numbers==2:
              print("choose the two numbers from",a)
              print("choose the first number")
              a[(int(input()))]='.'
              print("choose the second number")
              a[(int(input()))]='.'
              print(a)
       if a==['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']:
           print("player two is the winner")
           break
    while the_player==2:
         print("player two's turn")
         print("choose one or two numbers")
         choosen_numbers=int(input())
         if choosen_numbers==1:
             print("choose the number from",a)
             a[(int(input()))]='.'
             print(a)
         elif choosen_numbers==2:
              print("choose the two numbers from",a)
              print("choose the first number")
              a[(int(input()))]='.'
              print("choose the second number")
              a[(int(input()))]='.'
              print(a)
         while choosen_numbers!=1 and choosen_numbers!=2:
              print("you're not allow to choose this number please choose 1 or 2" )
              choosen_numbers=int(input())
              if choosen_numbers==1:
                print("choose the number from",a)
                a[(int(input()))]='.'
                print(a)
              elif choosen_numbers==2:
                print("choose the two numbers from",a)
                print("choose the first number")
                a[(int(input()))]='.'
                print("choose the second number")
                a[(int(input()))]='.'
                print(a)
         if a==['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']:
             print("player two is the winner")
             break
         print("player one's turn")
         print("choose one or two numbers")
         choosen_numbers=int(input())
         if choosen_numbers==1:
             print("choose the number from",a)
             a[(int(input()))]='.'
             print(a)
         elif choosen_numbers==2:
             print("choose the two numbers from",a)
             print("choose the first number")
             a[(int(input()))]='.'
             print("choose the second number")
             a[(int(input()))]='.'
             print (a)
         while choosen_numbers!=1 and choosen_numbers!=2:
             print("you're not allow to choose this number please choose 1 or 2" )
             choosen_numbers=int(input())
             if choosen_numbers==1:
                print("choose the number from",a)
                a[(int(input()))]='.'
                print(a)
             elif choosen_numbers==2:
                print("choose the two numbers from",a)
                print("choose the first number")
                a[(int(input()))]='.'
                print("choose the second number")
                a[(int(input()))]='.'
                print(a)
         if a==['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']:
            print("player one is the winner")
            break


