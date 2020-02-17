#this program is intended to take in information and spit out who would win in a fight
#copyright Elizabeth Rankin

#import statements
import random

#def statments
def teams():
    team_list = []
    teamAdded = ""
    while teamAdded != "x":
        teamAdded = input("Write the team you want to add to the list here, enter 'x' to end team add: ")
        team_list.append(teamAdded)
    team_list.remove("x")
    print()
    print()
    print("Now on to the Matches!")
    return(team_list)

def roster(teamList):
    global winners
    list_length = len(teamList)
    matchups = []
    winners = []
    while list_length > 0:
        selection = random.randint(0, (list_length - 1))
        team_one = teamList.pop(selection)
        list_length = len(teamList)
        selection = random.randint(0, (list_length - 1))
        team_two = teamList.pop(selection)
        list_length = len(teamList)
        matchups.append(team_one + " vs " + team_two)
        winners.append(isWinner(team_one, team_two))
    return(matchups)

def isWinner(teamOne, teamTwo):
    print("On a scale of 1 to 10, the average age of", teamOne, "is:")
    mod1_1 = int(input())
    print("On a scale of 1 to 10, the average fighting experince of", teamOne, "is:")
    mod1_2 = int(input())
    print("On a scale of 1 to 10, the average age of", teamTwo, "is:")
    mod2_1 = int(input())
    print("On a scale of 1 to 10, the average fighting experince of", teamTwo, "is:")
    mod2_2 = int(input())
    global winner
    winner = ""
    print("This match is", teamOne, "VS", teamTwo + "!")
    scoreOne = (mod1_1 * mod1_2) + random.randint(1,100)
    scoreTwo = (mod2_1 * mod2_2) + random.randint(1,100)
    print(teamOne, "scored ", scoreOne, "points.")
    print(teamTwo, "scored", scoreTwo, "points.")
    if scoreOne > scoreTwo:
        print(teamOne, "wins the fight!")
        winner = teamOne
    else:
        if scoreTwo > scoreOne:
            print(teamTwo, "wins the fight!")
            winner = teamTwo
        else:
            print("it was a tie!")
    print()
    return(winner)


#main

teams_list = teams()
team_matchups = roster(teams_list)

print("The matchups for this round were:")
for x in team_matchups:
    print(x)
print()
print("And the winners were:")
for x in winners:
    print(x)