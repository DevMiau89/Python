print "Would you like to play a game:"
question = raw_input("> ")

while question != "quit":   
    if  question == "yes":       
        print "Welcome in the Rock Paper Scissors game"
        print "Player one, please enter the tool:"
        player1 = raw_input("> ")

        print "Player two, please enter the tool:"
        player2 = raw_input("> ")

        rock = "rock"
        paper = "paper"
        scissors = "scissors"

        if player1 == rock and player2 == scissors or player1 == paper and player2 == rock or player1 == scissors and player2 == paper:
            print "Player one won"
        elif player1 == scissors and player2 == rock or player1 == rock and player2 == paper or player1 == paper and player2 == scissors:
            print "Player two won"
        else:
            print "Yor input is worng. please re-enter."

    print "Would you like to play a game:"
    question = raw_input("> ")
    continue
   



               
