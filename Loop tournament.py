#this program is intended to take in information and spit out who would win in a fight
#copyright 2020 Elizabeth Rankin

#import statements
import random

#def statments

#this function will take in the input for team names and create a list with those names on it.
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


#this function takes th list in Teams, and creates matchups at random between two named teams.
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
        winners.append(isWinner(team_one, team_two)) #calls isWinner and appends the result to the global
#														variable winners
    return(matchups)


#takes a matchup and then requests variable information which it then uses to determine the winner of a 
#fight.
def isWinner(teamOne, teamTwo): 
    print("On a scale of 1 to 10, the average age of", teamOne, "is:")
    #the fiction project deals with semi-immortals so the ages can be wildly different and will play a 
	#fairly large role in who wins.
    mod1_1 = int(input())
    print("On a scale of 1 to 10, the average fighting experince of", teamOne, "is:")
    #different semi-immortals have very different day-to-day lives so some will have only some 
	#experience fighting and others will have enormous experience.
    mod1_2 = int(input())
    print("On a scale of 1 to 10, the average age of", teamTwo, "is:")
    mod2_1 = int(input())
    print("On a scale of 1 to 10, the average fighting experince of", teamTwo, "is:")
    mod2_2 = int(input())
    winner = ""
    print("This match is", teamOne, "VS", teamTwo + "!")
    scoreOne = (mod1_1 * mod1_2) + random.randint(1,100) #scores are determined by multiplying the two 
	#variables and then adding the result to the random number rolled.
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

#this function takes the winners of the last round then pits them against each other in order, so that a 
#proper tournament bracket can be done.
def next_round(last_winners):
    roster_length = len(last_winners)
    matchups = []
    winners = []
    while roster_length > 0:
        team_one = last_winners.pop(0)
        roster_length = len(last_winners)
        team_two = last_winners.pop(0)
        roster_length = len(last_winners)
        matchups.append(team_one + " vs " + team_two)
        winners.append(isWinner(team_one, team_two)) #calls isWinner and appends the result to the global 
#		variable winners
    return(winners,matchups)

#main
if __name__ == "__main__":
	teams_list = teams()
	team_matchups = roster(teams_list)
	print("The matchups for this round were:")
	for x in team_matchups:
		print(x)
	print()
	print("And the winners were:")
	for x in winners:
		print(x)
	print()
	print("On to the next round!")
	while len(winners) > 1:
		vs_list = []
		winners, vs_list = next_round(winners)
		print("The Matchups that round were:")
		for x in vs_list:
			print(x)
		print("The winners of that round were:")
		for x in winners:
			print(x)
	print("The champions are Team", winners[0])
