#this program is intended to take in information and spit out who would win in a fight
#copyright Elizabeth Rankin

#import statements
import random

#def statments
def teams(): #this function will take in the input for team names and create a list with those names on it.
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

def roster(teamList): #this function takes th list in Teams, and creates matchups at random between two named teams.
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
        winners.append(isWinner(team_one, team_two)) #calls isWinner and appends the result to the global variable winners
    return(matchups)

def isWinner(teamOne, teamTwo): #takes a matchup and then requests variable information which it then uses to determine the winner of a fight.
    print("On a scale of 1 to 10, the average age of", teamOne, "is:")
    #the fiction project deals with semi-immortals so the ages can be wildly different and will play a fairly large role in who wins.
    mod1_1 = int(input())
    print("On a scale of 1 to 10, the average fighting experince of", teamOne, "is:")
    #different semi-immortals have very different day-to-day lives so some will have only some experience fighting and others will have enormous experience.
    mod1_2 = int(input())
    print("On a scale of 1 to 10, the average age of", teamTwo, "is:")
    mod2_1 = int(input())
    print("On a scale of 1 to 10, the average fighting experince of", teamTwo, "is:")
    mod2_2 = int(input())
    global winner
    winner = ""
    print("This match is", teamOne, "VS", teamTwo + "!")
    scoreOne = (mod1_1 * mod1_2) + random.randint(1,100) #scores are determined by multiplying the two variables and then adding the result to the random number rolled.
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
