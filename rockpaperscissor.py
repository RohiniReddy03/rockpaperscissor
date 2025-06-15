def rock_paper_scissor():
    rock = 1
    paper = 2
    scissor = 3
    p1 = int(input("Enter Player 1 choice (1-Rock, 2-Paper, 3-Scissors): "))
    p2 = int(input("Enter Player 2 choice (1-Rock, 2-Paper, 3-Scissors): "))
    if p1 == p2:
        print("It is a tie!")
    elif (p1 == rock and p2 == scissor) or (p1 == paper and p2 == rock) or (p1 == scissor and p2 == paper):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
rock_paper_scissor()


def rock_paper_scissor(rock, paper, scissor):
    p1 = int(input("enter the p1:"))
    p2 = int(input("enter the p2:"))
    if p1 == p1:
       print("It is  a tie")
    elif (p1 == rock and p2 == scissor):
       print("p1 win")
    elif (p1 == rock and p2 == paper):
        print("p2 win")
    elif (p1 == paper and p2 == rock):
        print("p1 win")
    elif (p1 == paper and p2 == scissor):
        print("p2 win")
    elif (p1 == scissor and p2 == rock):
        print("p2 win")
    elif (p1 == scissor and p2 == paper):
        print("p1 win")
        
rock_paper_scissor()




           
           
           
           
           
           
           
           
           
           
    