import random
import time
# import matplotlib.pyplot as plt


def print_game_matrix(game_matrix):
    mapping = {0: ' ', 1: 'X', 2: 'O'}
    print(" {} | {} | {}".format(mapping[game_matrix[0]], mapping[game_matrix[1]], mapping[game_matrix[2]]))
    print("---+---+---")
    print(" {} | {} | {}".format(mapping[game_matrix[3]], mapping[game_matrix[4]], mapping[game_matrix[5]]))
    print("---+---+---")
    print(" {} | {} | {}".format(mapping[game_matrix[6]], mapping[game_matrix[7]], mapping[game_matrix[8]]))

# defining a function to check if the game is over
def game_over(game_matrix):
    # if there is a winner
    if (game_matrix[0]==game_matrix[1]==game_matrix[2] and game_matrix[0] !=0) or (game_matrix[3]==game_matrix[4]==game_matrix[5] and game_matrix[3] !=0) or (game_matrix[6]==game_matrix[7]==game_matrix[8] and game_matrix[6] !=0) or (game_matrix[0]==game_matrix[3]==game_matrix[6] and game_matrix[0] !=0) or (game_matrix[1]==game_matrix[4]==game_matrix[7] and game_matrix[1] !=0) or (game_matrix[2]==game_matrix[5]==game_matrix[8] and game_matrix[2] !=0) or (game_matrix[0]==game_matrix[4]==game_matrix[8] and game_matrix[0] !=0) or (game_matrix[2]==game_matrix[4]==game_matrix[6] and game_matrix[2] !=0):
        return 1
    # if there is a draw
    elif 0 not in game_matrix:
        return 1
    else:
        return 0
# defining a function to check who won
def who_won(game_matrix):
    if (game_matrix[0] == game_matrix[1] == game_matrix[2] == 1) or \
       (game_matrix[3] == game_matrix[4] == game_matrix[5] == 1) or \
       (game_matrix[6] == game_matrix[7] == game_matrix[8] == 1) or \
       (game_matrix[0] == game_matrix[3] == game_matrix[6] == 1) or \
       (game_matrix[1] == game_matrix[4] == game_matrix[7] == 1) or \
       (game_matrix[2] == game_matrix[5] == game_matrix[8] == 1) or \
       (game_matrix[0] == game_matrix[4] == game_matrix[8] == 1) or \
       (game_matrix[2] == game_matrix[4] == game_matrix[6] == 1):
        return 1  # Player 1 wins
    elif (game_matrix[0] == game_matrix[1] == game_matrix[2] == 2) or \
         (game_matrix[3] == game_matrix[4] == game_matrix[5] == 2) or \
         (game_matrix[6] == game_matrix[7] == game_matrix[8] == 2) or \
         (game_matrix[0] == game_matrix[3] == game_matrix[6] == 2) or \
         (game_matrix[1] == game_matrix[4] == game_matrix[7] == 2) or \
         (game_matrix[2] == game_matrix[5] == game_matrix[8] == 2) or \
         (game_matrix[0] == game_matrix[4] == game_matrix[8] == 2) or \
         (game_matrix[2] == game_matrix[4] == game_matrix[6] == 2):
        return 2  # Player 2 wins
    else:
        return -1  # Game is still in progress or it's a draw

# defining a function to check if a move is valid
# def valid_move(game_matrix,move):
#     if move in range(1,10) and game_matrix[move-1]==0:
#         return True
#     else:
#         return False

# defining a function to make a move
def make_move(game_matrix,move,player):
    game_matrix[move-1]=player
    return game_matrix

def init():
    print("Welcome to Tic Tac Toe!")
    print("Instructions:")
    print("1. The board is numbered from 1 to 9 (left to right).")
    print("2. You have to input the position where you want to mark.")
    print("3. The player who succeeds in marking 3 consecutive positions wins.")
    print("4. If no one wins, the game is a draw.")
    print("5. You will be playing against the Menace.")
    print("6. The Menace is a learning AI which learns from its mistakes.")
init()
# making a dictionary (matchboxes) to store the moves

def meance_move(game_matrix,player):
    curr_pos="".join(str(i) for i in game_matrix)
    if curr_pos not in matchboxes:
        matchboxes[curr_pos]={}
        for i in range(9):
            if(curr_pos[i]=='0'):
                new_pos=curr_pos[:i]+str(player)+curr_pos[i+1:]
                matchboxes[curr_pos][new_pos]=10
    # choose a random move from the matchbox with probability with weights as the value for each move
    new_pos=random.choices(list(matchboxes[curr_pos].keys()),weights=matchboxes[curr_pos].values())[0]
    menace_move_list.append([curr_pos,new_pos])
    # print(new_pos)
    # print("menace moves :" ,menace_move_list)
    game_matrix=list(new_pos)
    game_matrix=[int(i) for i in game_matrix]
    # print("Menace's Move:")
    # print(game_matrix)
    # print_game_matrix(game_matrix)
    return game_matrix

def human_move(game_matrix,player):
    curr_pos="".join(str(i) for i in game_matrix)
    if curr_pos not in matchboxes:
        matchboxes[curr_pos]={}
        for i in range(9):
            if(curr_pos[i]=='0'):
                new_pos=curr_pos[:i]+str(player)+curr_pos[i+1:]
                matchboxes[curr_pos][new_pos]=10
    # choose a random move from the matchbox with probability with weights as the value for each move
    new_pos=random.choices(list(matchboxes[curr_pos].keys()))[0]
    # print(new_pos)
    game_matrix=list(new_pos)
    game_matrix=[int(i) for i in game_matrix]
    # print("Human's Move:")
    # print(game_matrix)
    # print_game_matrix(game_matrix)
    return game_matrix


def random_mover(game_matrix):
    # choose a random move
    move=random.choice([i for i in range(9) if game_matrix[i]==0])
    game_matrix[move]=1
    return game_matrix

num_trials = 1000
before_training_wins = []
before_training_losses = []
after_training_wins = []
after_training_losses = []
matchboxes={}
#play against player 
for i in range(0):
    game_matrix=[0,0,0,0,0,0,0,0,0]
    menace_move_list=[]

    while True:
        move=int(input("Enter your move:"))
        game_matrix=make_move(game_matrix,move,1)
        # game_matrix=human_move(game_matrzix,1)
        print("Your Move:")
        print(game_matrix)
        #print the game matrix
        print_game_matrix(game_matrix)
        #check if the game is over
        game_result=who_won(game_matrix)
        if(game_over(game_matrix)):
            game_result=who_won(game_matrix)
            print("player",game_result,"wins")
            break
        # if game_result==-1:
        #     print("Game is a draw")
            # print(matchboxes)
            # break
        #ask menace to make a move
        game_matrix=meance_move(game_matrix,2)
        print("Menace's Move:")
        print(game_matrix)
        #print the game matrix
        print_game_matrix(game_matrix)
        if(game_over(game_matrix)):
            game_result=who_won(game_matrix)
            print("player",game_result,"wins")
            break
        # if game_result==-1:
        #     break



for i in range(1):
    
    matchboxes={}

    #   Before training
    #  Playing against the menace
    menace_wins=0
    human_wins=0
    draws=0
    print()
    print()
    print("Playing before training :")
    #   Training the menace
    for i in range(100):
        game_matrix=[0,0,0,0,0,0,0,0,0]
        menace_move_list=[]

        while True:
            game_matrix=human_move(game_matrix,1)
            # print("Your Move:")
            # print(game_matrix)
            # #print the game matrix
            # print_game_matrix(game_matrix)
            #check if the game is over
            if(game_over(game_matrix)):
                game_result=who_won(game_matrix)

                if game_result==1 or game_result==2 :
                    # print(menace_move_list)
                    # print("player",game_result,"won")
                    if(game_result==1):
                        # for i in menace_move_list:
                        #     matchboxes[i[0]][i[1]]-=1
                        human_wins+=1
                    elif(game_result==2):
                        # for i in menace_move_list:
                        #     matchboxes[i[0]][i[1]]+=1
                        menace_wins+=1
                    # print(matchboxes)
                    break
                if game_result==-1:
                    # print("Game is a draw")
                    # print(matchboxes)
                    break
            #ask menace to make a move
            game_matrix=meance_move(game_matrix,2)

            if(game_over(game_matrix)):
                game_result=who_won(game_matrix)

                if game_result==1 or game_result==2 :
                    # print("player",game_result,"won")
                    # print(menace_move_list)
                    #update the matchbox
                    if(game_result==1):
                        # for i in menace_move_list:
                        #     matchboxes[i[0]][i[1]]-=1
                        human_wins+=1
                    elif(game_result==2):
                        # for i in menace_move_list:
                        #     matchboxes[i[0]][i[1]]+=1
                        menace_wins+=1
                    # print(matchboxes)
                    break
                if game_result==-1:
                    draws+=1
                    # print("Game is a draw")
                    # print(matchboxes)
                    break
    before_training_losses.append(human_wins)
    before_training_wins.append(menace_wins)
    print("Menace wins:",menace_wins)
    print("Human wins:",human_wins)
    print("Draws:",draws)

    # wait()
    #   Training the menace
    menace_wins=0
    human_wins=0
    draws=0 
    print()
    print()
    print("Training the menace :")

    for i in range(10000):
        game_matrix=[0,0,0,0,0,0,0,0,0]
        menace_move_list=[]

        while True:
            game_matrix=human_move(game_matrix,1)
            # print("Your Move:")
            # print(game_matrix)
            # #print the game matrix
            # print_game_matrix(game_matrix)
            #check if the game is over
            if(game_over(game_matrix)):
                game_result=who_won(game_matrix)

                if game_result==1 or game_result==2 :
                    # print(menace_move_list)
                    # print("player",game_result,"won")
                    if(game_result==1):
                        for i in menace_move_list:
                            matchboxes[i[0]][i[1]]*=0.1
                        human_wins+=1

                    elif(game_result==2):
                        for i in menace_move_list:
                            matchboxes[i[0]][i[1]]*=10
                        menace_wins+=1

                    # print(matchboxes)
                    break
                if game_result==-1:
                    draws+=1
                    # print("Game is a draw")
                    # print(matchboxes)
                    break
            #ask menace to make a move
            game_matrix=meance_move(game_matrix,2)

            if(game_over(game_matrix)):
                game_result=who_won(game_matrix)

                if game_result==1 or game_result==2 :
                    # print("player",game_result,"won")
                    # print(menace_move_list)
                    #update the matchbox
                    if(game_result==1):
                        for i in menace_move_list:
                            matchboxes[i[0]][i[1]]*=0.1
                        human_wins+=1

                    elif(game_result==2):
                        for i in menace_move_list:
                            matchboxes[i[0]][i[1]]*=10
                        menace_wins+=1

                    # print(matchboxes)
                    break
                if game_result==-1:
                    draws+=1
                    # print("Game is a draw")
                    # print(matchboxes)
                    break

    print("Menace wins:",menace_wins)
    print("Human wins:",human_wins)
    print("Draws:",draws)


    # print(matchboxes)

    #  Playing against the menace
    menace_wins=0
    human_wins=0
    draws=0
    #   Training the menace
    print()
    print()
    print("Playing after training :")
    for i in range(100):
        game_matrix=[0,0,0,0,0,0,0,0,0]
        menace_move_list=[]

        while True:
            game_matrix=human_move(game_matrix,1)
            # print("Your Move:")
            # print(game_matrix)
            # #print the game matrix
            # print_game_matrix(game_matrix)
            #check if the game is over
            if(game_over(game_matrix)):
                game_result=who_won(game_matrix)

                if game_result==1 or game_result==2 :
                    # print(menace_move_list)
                    # print("player",game_result,"won")
                    if(game_result==1):
                        for i in menace_move_list:
                            matchboxes[i[0]][i[1]]*=0.1
                        human_wins+=1
                    elif(game_result==2):
                        for i in menace_move_list:
                            matchboxes[i[0]][i[1]]*=10
                        menace_wins+=1
                    # print(matchboxes)
                    break
                if game_result==-1:
                    # print("Game is a draw")
                    # print(matchboxes)
                    draws+=1
                    break
            #ask menace to make a move
            game_matrix=meance_move(game_matrix,2)

            if(game_over(game_matrix)):
                game_result=who_won(game_matrix)

                if game_result==1 or game_result==2 :
                    # print("player",game_result,"won")
                    # print(menace_move_list)
                    #update the matchbox
                    if(game_result==1):
                        for i in menace_move_list:
                            matchboxes[i[0]][i[1]]*=0.1
                        human_wins+=1
                    elif(game_result==2):
                        for i in menace_move_list:
                            matchboxes[i[0]][i[1]]*=10
                        menace_wins+=1
                    # print(matchboxes)
                    break
                if game_result==-1:
                    draws+=1
                    # print("Game is a draw")
                    # print(matchboxes)
                    break

    print("Menace wins:",menace_wins)
    print("Human wins:",human_wins)
    print("Draws:",draws)
    after_training_losses.append(human_wins)
    after_training_wins.append(menace_wins)
    print(matchboxes)

# #Plot the results
# print(before_training_wins)
# print(before_training_losses)
# print(after_training_wins)
# print(after_training_losses)
# plt.plot(range(10), before_training_wins, label='Wins before training')
# # plt.plot(range(10), before_training_losses, label='Losses before training')
# plt.plot(range(10), after_training_wins, label='Wins after training')
# # plt.plot(range(10), after_training_losses, label='Losses after training')

# plt.xlabel('Trials')
# plt.ylabel('Number of games')
# plt.title('Menace Performance')
# plt.legend()
# plt.show()
#play against player 
for i in range(0):
    game_matrix=[0,0,0,0,0,0,0,0,0]
    menace_move_list=[]

    while True:
        move=int(input("Enter your move:"))
        game_matrix=make_move(game_matrix,move,1)
        # game_matrix=human_move(game_matrix,1)
        print("Your Move:")
        print(game_matrix)
        #print the game matrix
        print_game_matrix(game_matrix)
        #check if the game is over
        game_result=who_won(game_matrix)
        if(game_over(game_matrix)):
            game_result=who_won(game_matrix)
            print("player",game_result,"wins")
            break
        # if game_result==-1:
        #     print("Game is a draw")
            # print(matchboxes)
            # break
        #ask menace to make a move
        game_matrix=meance_move(game_matrix,2)
        print("Menace's Move:")
        print(game_matrix)
        #print the game matrix
        print_game_matrix(game_matrix)
        if(game_over(game_matrix)):
            game_result=who_won(game_matrix)
            print("player",game_result,"wins")
            break
        # if game_result==-1:
        #     break
