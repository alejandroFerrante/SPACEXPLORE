import time
import random
from random import randint
import os
import sys, select


'''
TODO

NAVIGATION
	add damage
	Inspect Stats (ENTRY R)
	asteroids

PLANET

BATTLE

OTHERS
	load planets stats from file

'''

##time.sleep(1)
##possibleValues = ["1","2","3","4","5","6","7","8","9","0"]
##cmd = raw_input("Type a number betweeen 0 and 9: ")
##if cmd in possibleValues :

#i, o, e = select.select( [sys.stdin], [], [], 10 )
#
#	if (i):
#  		print("You said"+str(sys.stdin.readline().strip()))
#	else:
#  		print("You said nothing!")

finished = False
frameRate = 2

invalidInputTime = 1
choiceInputTime = 3

def printLine():
	print("================================================================================")
	print("================================================================================")

def clearScreen():
	os.system('clear')

def invalidInput():
	print("The value entered is not valid.")
	time.sleep(invalidInputTime)

def getPlanetsMap():
	planetsMap = {}
	planet = {}
	planet["name"] = "RALAR-6"
	planetsMap["8,20"] = planet

	planet = {}
	planet["name"] = "EQUIS-23"
	planetsMap["30,0"] = planet

	planet = {}
	planet["name"] = "PAPILON-5"
	planetsMap["30,45"] = planet

	return planetsMap


def getPlanetLocationString(planetsMap):
	result = ""
	for k in planetsMap.keys() :
		result += "("+k+") -------> "+planetsMap[k]["name"]+"\n" 
	
	return result

def doStart(variables):
	printLine()
	print("You finally depart from a planet called H.O.M.E. Unexpected adventures await you as you launch yourself to the ultimate adventure!\n")
	printLine()
	time.sleep(4)
	variables["currentState"] = 1 #LAUNCH
	return variables

def doLaunch(variables):
	possibleValues = ["N","NE","E","SE","S","SW","W","NW"]
	printLine()
	cmd = input("Ready to depart! Select initial direction N, NE, E, SE, S, SW, W, NW :\n")
	printLine()
	if cmd in possibleValues :
		print(">>>> "+cmd)
		variables["currentDirection"] = cmd
		variables["currentState"] = 2#TRAVELING

		print("Take off in t- ")
		time.sleep(1)
		print("5 ...")
		time.sleep(1)

		print("4 ...")
		time.sleep(1)

		print("3 ...")
		time.sleep(1)

		print("2 ...")
		time.sleep(1)

		print("1 ...")
		time.sleep(1)

		print("LAUNCH!")
		printLine()
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

	variables["fuel"] -= variables["fuelConsuption"]

	#CHECK IF FUEL RUN OUT
	#CHECK FOR ASTEROIDS, BATTLE OR PLANET
	printLine()
	print("QUADRANT: ("+str(variables["quadrantX"])+","+str(variables["quadrantY"])+")")
	print("FUEL: "+str(variables["fuel"])+" cosmogallons")
	print("SPEED: "+str(variables["currentSpeed"])+" galactic knots ")
	print("DIRECTION: "+str(variables["currentDirection"]))
	print("\nEnter D to modify direction , S to modify speed, P to list planets or R for a general report \n")
	printLine()
	possibleValues = ["S","D","P","R"]
	i, o, e = select.select( [sys.stdin], [], [], choiceInputTime )
	if (i):
		cmd = str(sys.stdin.readline().strip())
		if cmd in possibleValues :

			if cmd == "S" :
				variables["currentState"] = 21#SET SPEED

			if cmd == "D" :
				variables["currentState"] = 22#SET DIRECTION

			if cmd == "P" :
				print("KNOWN PLANETS \n")
				print(getPlanetLocationString(variables["planetsMap"]))
				time.sleep(5)	

			#if cmd == "R" :
				

		else:
			invalidInput()	
  		
	else:
  		print("")

	return variables

def doSetSpeed(variables):
	printLine()
	cmd = input("Select new speed from "+str(variables["speedMin"])+" to "+str(variables["speedMax"])+"\n")
	printLine()
	try:
		cmd = int(cmd)
		if cmd >= variables["speedMin"] and cmd <= variables["speedMax"]:
			variables["currentSpeed"] = cmd
			variables["currentState"] = 2#TRAVELING
		else:
			invalidInput()

	except:
		invalidInput()

	return variables	

def doSetDirection(variables):
	possibleValues = ["N","NE","E","SE","S","SW","W","NW"]
	printLine()
	cmd = input("Select new direction N, NE, E, SE, S, SW, W, NW :\n")
	printLine()
	if cmd in possibleValues :
		variables["currentDirection"] = cmd
		variables["currentState"] = 2#TRAVELING
	else:
		invalidInput()
	
	return variables	




def doLoop(variables):
	#print(">>>>> "+str(variables["currentState"]))
	if variables["currentState"] == 0:
		return doStart(variables)

	if variables["currentState"] == 1:
		return doLaunch(variables)
	
	if variables["currentState"] == 2:
		return doTravel(variables)
	
	if variables["currentState"] == 21:
		return doSetSpeed(variables)

	if variables["currentState"] == 22:
		return doSetDirection(variables)

	
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
	
	''
	calls = 0
	variables = {}
	variables["planetsMap"] = getPlanetsMap()
	variables["currentState"] = 0
	variables["quadrantX"] = 0
	variables["quadrantY"] = 0
	variables["currentDirection"] = "N"
	variables["currentSpeed"] = 1
	variables["speedMin"] = 1
	variables["speedMax"] = 2
	variables["fuel"] = 2000
	variables["fuelMax"] = 3000
	variables["fuelConsuption"] = 15


	while not finished :
		clearScreen()
		variables = doLoop(variables)
		calls += 1
		time.sleep(frameRate/variables["currentSpeed"])

	
	

if __name__== "__main__":
  main()


'''
	0.START

	1.LAUNCH

	2.NAVIGATING
		21.SET NEW DIRECTION
		22.SET NEW SPEED
		23.METEOR ENCOUNTER
		

	3.BATTLE
		

	4.PLANET MAIN MENU
		41.MARKET
			411.BUY MINERAL
			412.SELL MINERAL
		42.SUPPLIES
			421.BUY SUPPLIES
			422.CHARGE ENERGY
		43.GARAGE
			431.REPAIR SHIP
			432.UPGRADE CANNONS
			433.UPGRADE SHIP ARMOR
			434.UPGRADE EVASION CONTROLS
			435.UPGRADE PROPULSORS
		44.BARRACS
			441.UPGRADE TROOPS
			442.HIRE TROOPS
		45.CAPITOL
			451.FUND PARTY
			452.START RAISING
		46.EXPLORATORY
		47.ECONOMY?
		48.LEAVE

'''

#https://abinbevlatam--fulllatam.cs52.my.salesforce.com/packaging/installPackage.apexp?p0=04t2M000002QBgY