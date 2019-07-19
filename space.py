import time
import random
from random import randint
import os
import sys, select

##time.sleep(1)
##possibleValues = ["1","2","3","4","5","6","7","8","9","0"]
##cmd = raw_input("Type a number betweeen 0 and 9: ")
##if cmd in possibleValues :

finished = False
frameRate = 2

invalidInputTime = 1






def clearScreen():
	os.system('clear')

def invalidInput():
	print("The value entered is not valid.")
	time.sleep(invalidInputTime)




def doStart(variables):
	print("You finally depart from a planet called H.O.M.E. Unexpected adventures await you as you launch yourself to the ultimate adventure!\n")
	time.sleep(4)
	variables["currentState"] = 1 #LAUNCH
	return variables


def doLaunch(variables):
	possibleValues = ["N","NE","E","SE","S","SW","W","NW"]
	cmd = input("Ready to depart! Select initial direction N, NE, E, SE, S, SW, W, NW :\n")
	if cmd in possibleValues :
		variables["currentDirection"] = cmd
		variables["currentState"] = 2#TRAVELING
	else:
		invalidInput()
	
	return variables

def doTravel(variables):
	
	if variables["currentDirection"] == "N"  :
		variables["quadrantY"] += 1 

	if variables["currentDirection"] == "NE" :
		variables["quadrantX"] += 1
		variables["quadrantY"] += 1

	if variables["currentDirection"] == "E"  :
		variables["quadrantX"] += 1

	if variables["currentDirection"] == "SE" :
		variables["quadrantX"] += 1
		variables["quadrantY"] -= 1 

	if variables["currentDirection"] == "S"  :
		variables["quadrantY"] -= 1 

	if variables["currentDirection"] == "SW" :
		variables["quadrantX"] -= 1
		variables["quadrantY"] -= 1 

	if variables["currentDirection"] == "W"  :
		variables["quadrantX"] -= 1

	if variables["currentDirection"] == "NW" :
		variables["quadrantX"] -= 1
		variables["quadrantY"] += 1


	print("You are now on quadrant ("+str(variables["quadrantX"])+","+str(variables["quadrantY"])+"). Press C to continue, D to set direction and S to set speed: \n")
	
	variables["currentState"] = 2 #LAUNCH
	return variables


def doLoop(variables):
	#print(">>>>> "+currentState)
	if variables["currentState"] == 0:
		return doStart(variables)

	if variables["currentState"] == 1:
		return doLaunch(variables)
	
	if variables["currentState"] == 2:
		return doTravel(variables)
	

	
	'''
	if currentState == "21" :
		possibleValues = "N,NE,E,SE,S,SW,W,NW"
		print("You are at quadrant ("+quadrantX+","+quadrantY+").\n")
		cmd = input("Enter")
		if cmd in possibleValues :
			state = newState
			currentDirection = "TRAVELING"
			
			#drawScreen(menuMap)
		else:
			invalidInput()
			#drawScreen(menuMap)

	'''

def main():
	
	'''
	calls = 0
	variables = {}
	variables["currentState"] = 0
	variables["quadrantX"] = 0
	variables["quadrantY"] = 0
	variables["currentDirection"] = "N"

	while not finished :
		clearScreen()
		variables = doLoop(variables)
		calls += 1
		time.sleep(frameRate)

	'''
	print("You have ten seconds to answer!")

	i, o, e = select.select( [sys.stdin], [], [], 10 )

	if (i):
  		print("You said"+str(sys.stdin.readline().strip()))
	else:
  		print("You said nothing!")

if __name__== "__main__":
  main()


'''
	0.START

	1.LAUNCH

	2.NAVIGATING
		21.SET NEW DIRECTION
		21.SET NEW SPEED
		22.METEOR ENCOUNTER
		

	3.BATTLE
		

	4.PLANET MAIN MENU
		41.MINERALS
		42.SUPPLIES
		43.MECHANICS
		44.MERCENARIES
		45.POLITICS
		46.ECONOMY
		47.LEAVE

'''

#https://abinbevlatam--fulllatam.cs52.my.salesforce.com/packaging/installPackage.apexp?p0=04t2M000002QBgY