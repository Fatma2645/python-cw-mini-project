def padel_court_cost(court_type):
    print("ifcoirt_type is indoor return[30]")
    elififcoirt_type is outdoorreturn(20)



def rackets_cost(racket_brand):
    if racket_brand== "Bullpadel":
        return 140
    elif racket_brand=="Bullpadel":
        return 200




def padel_balls_cost(ball_boxes):
 if ball_boxes==1:
    return2
 elif ball_boxes==2:
    return 3.5
 elif ball_boxes==3:
    return 5



def padel_game_cost():
    court_type=input("court type indoor:/outdoor")
    racketts_brand=input("racket_brand:nox/slux/bullpadel")
    ball_boxes=int(input("number of ball boxes:1/2/3"))
    print=padel_court_cost(court_type)+rackets_cost(rackets_brand)+padel_ball_cost(ball_boxes)
    return print

print (padel_game_cost())
    



    


    




