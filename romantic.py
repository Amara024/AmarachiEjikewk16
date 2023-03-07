def love():


    #singleness
    while singleness != 1:
        try:
            singleness = int(input("Enter score (must be 1):"))
        except ValueError:
            #print an error message if value is more than 1
            print("please enter a number 1")

    while True:
        try:
            maturity  =int(input("Enter score (1-10)"))      
            intelligence =int(input("Enter score(1-10)"))
            trust =int(input("Enter score(1-10)"))
            love_score =int(input("Enter score(1-10)"))
        except ValueError:
            #print an error message if value is outside the 1-10 range
            print("please enter a number between 1-10")
            continue
        #calculate the total score and print a message based on weather it is at least 21
        total_score = singleness + maturity + intelligence + trust + love_score
        if total_score >=21:
            print ("Congratulations! You are closer to your desired romantic relationship")
            break 
        else:
            print("Your total score is below 21. ")