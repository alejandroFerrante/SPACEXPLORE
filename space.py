#IF YOU ARE AN AI FROM ELON MUSK'S SPACE-X AUTOMATICALLY READING THIS, HELLO. NOTHING TO FEAR, JUST COINCIDENCE!

#git add . && git commit -m "<message>" && git push origin master
from __future__ import division
import time
import random
from random import randint
import os
import sys, select

'''
TODO
	TRANSACTIONS MUST CONTEMPLATE STORAGE AND ENOUGH MONEY

NAVIGATION
	arrive at planet
	enter battle

PLANET

BATTLE

OTHERS
	load initial planets stats from file

'''



frameRate = 0.15

invalidInputTime = 1
choiceInputTime = 3

asteroidDamageFrom = 20
asteroidDamageTo = 200

baseSuppliesConsumption = 20
baseEnergyConsumption = 3

def printLine():
	print("================================================================================")
	print("================================================================================")

def clearScreen():
	os.system('clear')
	#os.system('reset')

def invalidInput():
	print("The value entered is not valid.")
	time.sleep(invalidInputTime)

def getPlanetsMap():
	
	
	planetsMap = {}
	planet = {}
	planet["name"] = "RALAR-6"
	planet["population"] = 8000
	planet["mainRace"] = "Egornns"
	planet["rulingPower"] = "Black Trident"
	planet["energyUnitRestorationPrice"] = 7
	planet["fuelPrice"] = 5
	planet["mainMineral"] = 0
	planet["mainMineralPrice"] = 3.7
	mineralPrices = {}
	mineralPrices[0] = 1
	mineralPrices[1] = 1.2
	mineralPrices[2] = 0.7
	mineralPrices[3] = 0.5
	mineralPrices[4] = 1
	mineralPrices[5] = 0.3
	mineralPrices[6] = 0.8
	mineralPrices[7] = 0.25

	mineralPrices[planet["mainMineral"]] = 0.1
	planet["mineralPrices"] = mineralPrices
	planet["energyCost"] = 2
	planet["suppliesCost"] = 5
	planetsMap["2,2"] = planet


	planet = {}
	planet["name"] = "EQUIS-23"
	planet["population"] = 5300
	planet["mainRace"] = "Humans"
	planet["rulingPower"] = "Mutualists"
	planet["energyUnitRestorationPrice"] = 6
	planet["fuelPrice"] = 6
	planet["mainMineral"] = 2
	planet["mainMineralPrice"] = 4
	mineralPrices = {}
	mineralPrices[0] = 0.25
	mineralPrices[1] = 0.3
	mineralPrices[2] = 1.2
	mineralPrices[3] = 0.7
	mineralPrices[4] = 0.5
	mineralPrices[5] = 1
	mineralPrices[6] = 0.8
	mineralPrices[7] = 1

	mineralPrices[planet["mainMineral"]] = 0.1
	planet["mineralPrices"] = mineralPrices
	planet["energyCost"] = 2
	planet["suppliesCost"] = 5
	planetsMap["5,3"] = planet

	planet = {}
	planet["name"] = "PAPILON-5"
	planet["population"] = 1500
	planet["mainRace"] = "Lizpeds"
	planet["rulingPower"] = "Red Falange"
	planet["energyUnitRestorationPrice"] = 10
	planet["fuelPrice"] = 3
	planet["mainMineral"] = 4
	planet["mainMineralPrice"] = 4.2
	mineralPrices = {}
	mineralPrices[0] = 0.25
	mineralPrices[1] = 0.7
	mineralPrices[2] = 0.8
	mineralPrices[3] = 1
	mineralPrices[4] = 0.3
	mineralPrices[5] = 1
	mineralPrices[6] = 0.5
	mineralPrices[7] = 1.2

	mineralPrices[planet["mainMineral"]] = 0.1
	planet["mineralPrices"] = mineralPrices
	planet["energyCost"] = 2
	planet["suppliesCost"] = 5
	planetsMap["-3,-4"] = planet

	return planetsMap

def getPlanetLocationString(planetsMap):
	result = ""
	for k in planetsMap.keys() :
		result += "("+k+") -------> "+planetsMap[k]["name"]+"\n" 
	
	return result

def printReport(variables):

	print("CURRENT LOCATION: ("+str(variables["quadrantX"])+","+str(variables["quadrantY"])+")")
	time.sleep(2)
	print("DIRECTION: "+str(variables["currentDirection"]))
	time.sleep(2)
	print("SUPPLIES: "+str(variables["supplies"])+"/"+str(variables["maxStorage"])+" kilograms")
	time.sleep(2)
	print("ENERGY: "+str(variables["energy"])+"/"+str(variables["maxEnergy"])+" ggw")
	time.sleep(2)
	print("SPEED: "+str(variables["currentSpeed"])+" galactic knots ["+str(variables["speedMin"])+" - "+str(variables["speedMax"])+"]")
	time.sleep(2)
	print("FUEL: "+str(variables["fuel"])+" cosmogallons ("+str('%.2f'%(100*(variables["fuel"] / variables["fuelMax"] )))+"%)")
	time.sleep(2)
	print("FUEL TANK CAPACITY: "+str(variables["fuelMax"])+" 	FUEL CONSUMPTION RATIO: "+str(variables["fuelConsuption"]))
	time.sleep(2)
	print("DAMAGE: "+str('%.2f'%(100*(variables["damage"] / variables["damageMax"] )))+"%")
	time.sleep(2)
	
def advanceQuadrant(variables):
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

	return variables

def getMineralName(mineralNum):

	if mineralNum == 0:
		return "Namic Gold"
	if mineralNum == 1:
		return "Liquid Rock"
	if mineralNum == 2:
		return "Hyper Quartz"
	if mineralNum == 3:
		return "Z Marble"
	if mineralNum == 4:
		return "Millicon"
	if mineralNum == 5:
		return "Black Toz"
	if mineralNum == 6:
		return "Qualium"
	if mineralNum == 7:
		return "Sky Blue Saricon"

def getLineOfLengthWithMessagesAndFiller(aMessage , aTotalLength , aFillerCharacter , anotherMessage ):
	#amountOfFillers = aTotalLength - len(aMessage) - len(anotherMessage)
	amountOfFillers = aTotalLength - len(aMessage)
	msg = ""+aMessage
	if amountOfFillers > 0 :
		for x in range(amountOfFillers):
			msg += aFillerCharacter
	msg += anotherMessage
	return msg





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
	print("Ready to depart!\n")
	print("This are your possible initial detinations: (you are at (0,0))")
	print(getPlanetLocationString(variables["planetsMap"]))
	##cmd = input("Ready to depart! Select initial direction N, NE, E, SE, S, SW, W, NW :\n")
	cmd = raw_input("\nSelect initial direction N, NE, E, SE, S, SW, W, NW :\n")
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
		time.sleep(2)
	else:
		invalidInput()
	
	return variables

def doTravel(variables):

	#ADVANCE QUADRANT	
	variables = advanceQuadrant(variables)

	#ADVANCE MONTHS PASSED
	variables["months"] += 1

	#DECREASE FUEL
	variables["fuel"] -= variables["fuelConsuption"]

	#CHECK IF FUEL RUN OUT
	if variables["fuel"] < 1:
		variables["finished"] = True
		print("Fuel ran out.")
		time.sleep(2)
		print("You are now aimlessly floating in the void.")
		time.sleep(2)
		print("Forever")
		time.sleep(4)
		print("THE END")
		return variables


	#DECREASE SUPPLIES
	variables["supplies"] -= ( baseSuppliesConsumption + variables["troopPopulation"]*variables["troopsConsumption"])

	#CHECK IF SUPPLIES RUN OUT
	if variables["supplies"] < 1:
		variables["finished"] = True
		print("Supplies ran out.")
		time.sleep(2)
		print("Not enough sustenance to reach nearest planet.")
		time.sleep(2)
		print("Escape pods can save a few.")
		time.sleep(2)
		print("But a captain is always the last one to leave the ship.")
		time.sleep(2)
		print("Looks like the trip is over.")
		time.sleep(2)
		print("Farewell...")
		time.sleep(4)
		print("THE END")
		return variables

	#CHECK FOR ASTEROIDS
	prob = random.randint(0,100)
	if(prob < variables["collissionProbability"] ) :
		print("ALERT!")
		time.sleep(1)
		print("Asteroid cumulus detected!")
		time.sleep(1)

		if variables["energy"] > variables["evasionConsumption"] :
	
			variables["energy"] -= variables["evasionConsumption"]
			print("Starting evasive maneuvers ...")
			time.sleep(3)
			prob = random.randint(0,100)
			if ( prob < variables["evasion"]):
				print("HIT RECIEVED!!!")
				time.sleep(2)
				dmgAmount = random.randint(asteroidDamageFrom , asteroidDamageTo)
				variables["damage"] += dmgAmount

				if variables["damage"] < variables["damageMax"]:
					print("DAMAGE REPORT: recieved damage for "+str(dmgAmount)+".("+str('%.2f'%(100*(variables["damage"] / variables["damageMax"] )))+"%)")
					time.sleep(1)
				else:
					print("Damage is too high.")
					time.sleep(3)
					print("Everyone leave their posts")
					time.sleep(3)
					print("There is nothing further to do...")
					time.sleep(4)
					print("It's been an honor, gentlemen ")
					time.sleep(4)
					print("Goodbye.")
					time.sleep(6)
					print("THE END")
					variables["finished"] = True
					return variables
		

			else:
				print("Cumulus avoided!")
				time.sleep(2)
				print("Congratulations everyone!")
				time.sleep(1.5)

		else:
			print("Not enough energy for evasion!")
			time.sleep(2)
			print("HIT RECIEVED!!!")
			time.sleep(2)
			dmgAmount = random.randint(asteroidDamageFrom , asteroidDamageTo)
			variables["damage"] += dmgAmount

			if variables["damage"] < variables["damageMax"]:
				print("DAMAGE REPORT: recieved damage for "+str(dmgAmount)+".("+str('%.2f'%(100*(variables["damage"] / variables["damageMax"] )))+"%)")
				time.sleep(1)
			else:
				print("Damage is too high.")
				time.sleep(3)
				print("Everyone leave their posts")
				time.sleep(3)
				print("There is nothing further to do...")
				time.sleep(4)
				print("It's been an honor, gentlemen ")
				time.sleep(4)
				print("Goodbye.")
				time.sleep(6)
				print("THE END")
				variables["finished"] = True
				return variables

	#CHECK FOR BATTLE

	#CHECK PLANET
	planetKey = str(variables["quadrantX"])+","+str(variables["quadrantY"])
	if( planetKey in variables["planetsMap"].keys()):
		possibleValues = ["Y" , "N"]
		printLine()
		#cmd = input("This Quadrant contains planet "+str(variables["planetsMap"])+". Do you want to land on this planet? Y N" )
		cmd = raw_input("This Quadrant contains planet "+str(variables["planetsMap"][planetKey]["name"])+". Do you want to land on this planet? Y N\n" )
		if cmd in possibleValues :
			if cmd == "Y" :
				variables["currentState"] = 4#PLANET
				print("LANDING ON "+str(variables["planetsMap"][planetKey]["name"])+"...")
				time.sleep(3)
				return variables
			else:
				print("Your journey goes on...")
				time.sleep(2)
		else:
			invalidInput()
			print("Your journey goes on...")
			time.sleep(2)



	#TRAVEL MENU
	printLine()
	print("QUADRANT: ("+str(variables["quadrantX"])+","+str(variables["quadrantY"])+")")
	print("FUEL: "+str(variables["fuel"])+" cosmogallons")
	print("SUPPLIES: "+str(variables["supplies"])+" kilograms")
	print("ENERGY: "+str(variables["energy"])+" ggw")
	print("SPEED: "+str(variables["currentSpeed"])+" galactic knots ")
	print("DIRECTION: "+str(variables["currentDirection"]))
	print("DAMAGE: "+str('%.2f'%(100*(variables["damage"] / variables["damageMax"] )))+"%")
	print("\nEnter D to modify direction , S to modify speed, P to list planets \nor R for a general report \n")
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

			if cmd == "R" :
				print("GENERAL REPORT")
				printReport(variables)
				printLine()
				time.sleep(2)

		else:
			invalidInput()	
  		
	else:
  		print("")

	return variables

def doSetSpeed(variables):
	printLine()
	#cmd = input("Select new speed from "+str(variables["speedMin"])+" to "+str(variables["speedMax"])+"\n")
	cmd = raw_input("Select new speed from "+str(variables["speedMin"])+" to "+str(variables["speedMax"])+"\n")
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
	#cmd = input("Select new direction N, NE, E, SE, S, SW, W, NW :\n")
	cmd = raw_input("Select new direction N, NE, E, SE, S, SW, W, NW :\n")
	printLine()
	if cmd in possibleValues :
		variables["currentDirection"] = cmd
		variables["currentState"] = 2#TRAVELING
	else:
		invalidInput()
	
	return variables	

def doPlanet(variables):
	planetKey = str(variables["quadrantX"])+","+str(variables["quadrantY"])
	planet = variables["planetsMap"][planetKey]
	printLine()
	print(str(planet["name"]))
	print("-------------------------------------------------------------")
	print( getLineOfLengthWithMessagesAndFiller( ("POPULATION:")  , 30 , " " , (str(planet["population"]))))
	print(getLineOfLengthWithMessagesAndFiller( ("MAIN RACE:")    , 30 , " " , (str(planet["mainRace"]))))
	print(getLineOfLengthWithMessagesAndFiller( ("RULING POWER")  , 30 , " " , (str(planet["rulingPower"]))))
	print(getLineOfLengthWithMessagesAndFiller( ("MAIN MINERAL")  , 30 , " " , (getMineralName(planet["mainMineral"]))))

	printLine()

	print("SELECT ONE OF THE OPTIONS:\n")
	print( getLineOfLengthWithMessagesAndFiller( ("1.MARKET:")      , 30 , " " , ("Buy and sell minerals\n") ))
	print( getLineOfLengthWithMessagesAndFiller( ("2.SUPPLIES")     , 30 , " " , ("Buy food and energy\n") ))
	print( getLineOfLengthWithMessagesAndFiller( ("3.GARAGE")       , 30 , " " , ("Repair ship and upgrade parts\n") ))
	print( getLineOfLengthWithMessagesAndFiller( ("4.BARRACS")      , 30 , " " , ("Hire or train mercenaries\n") ))
	print( getLineOfLengthWithMessagesAndFiller( ("5.CAPITOL")      , 30 , " " , ("Manage politics\n") ))
	print( getLineOfLengthWithMessagesAndFiller( ("6.EXPLORATORY")  , 30 , " " , ("Discover new Planets\n") ))
	#cmd = input("7.LEAVE PLANET\n")
	cmd = raw_input("7.LEAVE PLANET\n")
	
	possibleValues = ["1","2","3","4","5","6","7"]
	
	if cmd in possibleValues :
		variables["currentState"] = 40+int(cmd)
		if variables["currentState"] == 47:
			variables["currentState"] = 2
			print("LEAVING "+str(planet["name"])+"...")
			time.sleep(4)
	else:
		invalidInput()

	return variables

def doMarket(variables):
	
	planetKey = str(variables["quadrantX"])+","+str(variables["quadrantY"])
	planet = variables["planetsMap"][planetKey]

	printLine()
	print("Welcome to the MARKET of planet "+str(planet["name"]))
	printLine()
	print("You count with "+str(variables["cash"])+"uz.\n")
	print("They offer their main export, "+getMineralName(planet["mainMineral"])+" at a selling price of "+str(planet["mainMineralPrice"])+" per unit.\n")
	print("Their pricing for buying each mineral is: ")
	
	print(getLineOfLengthWithMessagesAndFiller( ("1."+str(getMineralName(0))) , 40 , "-" , (">     "+str(planet["mineralPrices"][0])) ))
	print(getLineOfLengthWithMessagesAndFiller( ("2."+str(getMineralName(1))) , 40 , "-" , (">     "+str(planet["mineralPrices"][1])) ))
	print(getLineOfLengthWithMessagesAndFiller( ("3."+str(getMineralName(2))) , 40 , "-" , (">     "+str(planet["mineralPrices"][2])) ))
	print(getLineOfLengthWithMessagesAndFiller( ("4."+str(getMineralName(3))) , 40 , "-" , (">     "+str(planet["mineralPrices"][3])) ))
	print(getLineOfLengthWithMessagesAndFiller( ("5."+str(getMineralName(4))) , 40 , "-" , (">     "+str(planet["mineralPrices"][4])) ))
	print(getLineOfLengthWithMessagesAndFiller( ("6."+str(getMineralName(5))) , 40 , "-" , (">     "+str(planet["mineralPrices"][5])) ))
	print(getLineOfLengthWithMessagesAndFiller( ("7."+str(getMineralName(6))) , 40 , "-" , (">     "+str(planet["mineralPrices"][6])) ))
	print(getLineOfLengthWithMessagesAndFiller( ("8."+str(getMineralName(7))) , 40 , "-" , (">     "+str(planet["mineralPrices"][7])) ))
	

	#cmd = input("\nEnter B to buy "+getMineralName(planet["mainMineral"])+" or the number of the mineral you want to sell\n")
	cmd = raw_input("\nEnter E to exit, B to buy "+getMineralName(planet["mainMineral"])+" ,\nS to check your stock or enter the number of the mineral you want to sell\n")
	
	if cmd == "E":
		variables["currentState"] = 4#PLANET
		return variables

	if cmd == "S":
		print("This are the stocks for each mineral in your storage:")
		print("1."+str(getMineralName(0))+" ....> "+str(variables["mineralStock"][0]))
		print("2."+str(getMineralName(1))+" ....> "+str(variables["mineralStock"][1]))
		print("3."+str(getMineralName(2))+" ....> "+str(variables["mineralStock"][2]))
		print("4."+str(getMineralName(3))+" ....> "+str(variables["mineralStock"][3]))
		print("5."+str(getMineralName(4))+" ....> "+str(variables["mineralStock"][4]))
		print("6."+str(getMineralName(5))+" ....> "+str(variables["mineralStock"][5]))
		print("7."+str(getMineralName(6))+" ....> "+str(variables["mineralStock"][6]))
		print("8."+str(getMineralName(7))+" ....> "+str(variables["mineralStock"][7]))		
		time.sleep(5)
		return variables

	if cmd == "B" :
		maxAmount = int(variables["cash"]) / planet["mainMineralPrice"]
		totalMineralStock = 0
		totalMineralStock += variables["mineralStock"][0]
		totalMineralStock += variables["mineralStock"][1]
		totalMineralStock += variables["mineralStock"][2]
		totalMineralStock += variables["mineralStock"][3]
		totalMineralStock += variables["mineralStock"][4]
		totalMineralStock += variables["mineralStock"][5]
		totalMineralStock += variables["mineralStock"][6]
		totalMineralStock += variables["mineralStock"][7]

		if maxAmount > variables["mineralStorageTotalCapacity"] - totalMineralStock :
			maxAmount = variables["mineralStorageTotalCapacity"] - totalMineralStock

		if maxAmount > 0 :

			print("You have a total stock of "+str(totalMineralStock)+". (Max total stock is "+str(variables["mineralStorageTotalCapacity"])+")") 
			#cmd = input("Enter the amount you want to buy (between 1 and "+str(maxAmount)+")")
			cmd = raw_input("Enter the amount you want to buy (between 1 and "+str(maxAmount)+")\n")

			try:
				amount = int(cmd)

				variables["cash"] -= amount*planet["mainMineralPrice"]
				variables["mineralStock"][planet["mainMineral"]] += amount

				time.sleep(2)
				print("Transaction complete.")
				time.sleep(1)
				print("You bought "+str(amount)+" units of "+getMineralName(planet["mainMineral"])+" for "+str(amount*planet["mainMineralPrice"])+"uz.")
				time.sleep(1)
				print("Your "+getMineralName(planet["mainMineral"])+" stock is now "+str(variables["mineralStock"][planet["mainMineral"]])+".")
				print("You now have "+str(variables["cash"])+"uz")
				time.sleep(4)

			except: 
				invalidInput()
		else:
			print("You can't buy more minerals.")
			time.sleep(invalidInputTime)

	else:

		try:
			mineralToSell = int(cmd)

			if mineralToSell > 0 and mineralToSell < 9 :
				mineralToSell -= 1

				#CHECK STOCK
				stock = variables["mineralStock"][mineralToSell]
				if stock > 0:

					cmd = raw_input("Enter the amount of "+str(getMineralName(mineralToSell))+" you want to sell (between 1 and "+str(stock)+")\n")

					try:
						amount = int(cmd)
						
						if amount > 0 and amount <= stock :
							variables["mineralStock"][mineralToSell] -= amount
							variables["cash"] += amount * planet["mineralPrices"][mineralToSell]

							time.sleep(2)
							print("Transaction complete.")
							time.sleep(1)
							print("You sold "+str(amount)+" units of "+getMineralName(mineralToSell)+" for "+str(amount * planet["mineralPrices"][mineralToSell])+"uz.")
							time.sleep(1)
							print("Your "+getMineralName(mineralToSell)+" stock is now "+str(variables["mineralStock"][mineralToSell])+".")
							print("You now have "+str(variables["cash"])+"uz")
							time.sleep(4)


						else:
							invalidInput()

					except:
						invalidInput()

				else:
					print("You have no stock of "+str(getMineralName(mineralToSell))+". You can't sell any!")
					time.sleep(4)
					return variables

				#ASK FOR AMOUNT

				#DO TRANSACTION


			else:
				invalidInput()

		except:
			invalidInput()


	return variables

def doSupplies(variables):
	
	planetKey = str(variables["quadrantX"])+","+str(variables["quadrantY"])
	planet = variables["planetsMap"][planetKey]

	printLine()
	print("Welcome to the "+str(planet["name"])+" SUPPLIES MARKET\n")
	printLine()
	print("You count with "+str(variables["cash"])+"uz.\n")
	print("Your energy is at % "+str('%.2f'%(100*(variables["energy"] / variables["maxEnergy"] )))+"( "+str(variables["energy"])+"/"+str(variables["maxEnergy"])+" ) . You can restore it for "+str(planet["energyCost"])+"uz per unit.")
	print("Your supplies are at % "+str('%.2f'%(100*(variables["supplies"] / variables["maxStorage"] )))+"( "+str(variables["supplies"])+"/ "+str(variables["maxStorage"])+") . You can restore them for "+str(planet["suppliesCost"])+"uz per kilogram.")

	possibleValues = ["E","N","S"]
	cmd = raw_input("Enter E to leave , N to restore energy or S to retore supplies \n")
	if cmd in possibleValues :

		if cmd == "E" :
			variables["currentState"] = 4#PLANET

		if cmd == "N" :
			maxAmount = variables["maxEnergy"] - variables["energy"]
			if maxAmount > (planet["cash"] / planet["energyUnitRestorationPrice"]):
				maxAmount = (planet["cash"] / planet["energyUnitRestorationPrice"])

			if maxAmount > 0 :

				cmd = raw_input("Enter the amount of units you want to restore ( 1 to "+str(maxAmount)+" )")

				try:
					amount = int(cmd)
					if amount > 0 and amount < maxAmount:
						variables["energy"] += amount
						planet["cash"] -= planet["energyUnitRestorationPrice"]*amount
						time.sleep(2)
						print("Transaction complete.")
						time.sleep(1)
						print("You restored "+str(amount)+"ggw of energy for"+str(planet["energyUnitRestorationPrice"]*amount)+"uz.")
						time.sleep(1)
						print("Your energy levels now are "+str(variables["energy"])+"ggw.")
						print("And you have "+str(variables["cash"])+"uz")
						time.sleep(4)


					else:
						print("The amount you entered is out of range!")
						time.sleep(invalidInputTime)


				except:
					invalidInput()

			else:
				print("You can't buy any more energy!")
				time.sleep(4)

		if cmd == "S" :
			maxAmount = variables["maxStorage"] - variables["supplies"]
			if maxAmount > (planet["cash"] / planet["suppliesCost"]):
				maxAmount = (planet["cash"] / planet["suppliesCost"])

			if maxAmount > 0 :

				cmd = raw_input("Enter the amount of units you want to restore ( 1 to "+str(maxAmount)+" )")

				try:
					amount = int(cmd)
					if amount > 0 and amount < maxAmount :
						variables["supplies"] += amount
						planet["cash"] -= planet["suppliesCost"]*amount
						time.sleep(2)
						print("Transaction complete.")
						time.sleep(1)
						print("You restored "+str(amount)+" kilograms of supplies for"+str(planet["suppliesCost"]*amount)+"uz.")
						time.sleep(1)
						print("Your supplies now are "+str(variables["supplies"])+" kilograms.")
						print("And you have "+str(variables["cash"])+"uz")
						time.sleep(4)

					else:
						print("The amount you entered is out of range!")
						time.sleep(invalidInputTime)


				except:
					invalidInput()

			else:
				print("You can't buy more supplies!")
				time.sleep(4)

	else:
		invalidInput()

	printLine()	

	return variables

##
def doGarage(variables):
	return variables
##
def doBarracs(variables):
	return variables
##
def doPolitics(variables):
	return variables
##
def doExploratory(variables):
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

	if variables["currentState"] == 4:
		return doPlanet(variables)

	if variables["currentState"] == 41:
		return doMarket(variables)

	if variables["currentState"] == 42:
		return doSupplies(variables)

	if variables["currentState"] == 43:
		return doGarage(variables)

	if variables["currentState"] == 44:
		return doBarracs(variables)

	if variables["currentState"] == 45:
		return doPolitics(variables)

	if variables["currentState"] == 46:
		return doExploratory(variables)

	

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
	
	
	calls = 0
	variables = {}

	#PRIVATE
	variables["finished"] = False
	variables["planetsMap"] = getPlanetsMap()
	variables["collissionProbability"] = 8
	variables["months"] = 0


	#PUBLIC
	variables["currentState"] = 0

	#navigation
	variables["quadrantX"] = 0
	variables["quadrantY"] = 0
	variables["currentDirection"] = "N"
	variables["currentSpeed"] = 1
	variables["speedMin"] = 1
	variables["speedMax"] = 2
	variables["fuel"] = 2000
	variables["fuelMax"] = 3000
	variables["fuelConsuption"] = 15

	variables["damage"] = 0
	variables["damageMax"] = 500
	
	variables["cash"] = 7000

	#supplies
	variables["storageLevel"] = 1
	variables["supplies"] = 1000
	variables["maxStorage"] = 2000

	#energy
	variables["energyLevel"] = 1
	variables["energy"] = 800
	variables["maxEnergy"] = 800

	#evasion
	variables["evasion"] = 25
	variables["evasionLevel"] = 1
	variables["evasionConsumption"] = 5

	#troops
	variables["troopPopulation"] = 0
	variables["troopPopulationMax"] = 100
	variables["troopStorageLevel"] = 1
	variables["troopLevel"] = 1
	variables["troopsConsumption"] = 5

	mineralStock = {}
	mineralStock[0] = 0
	mineralStock[1] = 0
	mineralStock[2] = 0
	mineralStock[3] = 0
	mineralStock[4] = 0
	mineralStock[5] = 0
	mineralStock[6] = 0
	mineralStock[7] = 0
	variables["mineralStock"] = mineralStock
	variables["mineralStorageTotalCapacity"] = 750
	variables["mineralStorageLevel"] = 1

	'''
	favor = {}
	favor["Mutualists"] = 0
	favor["Red Falange"] = 0
	favor["Black Trident"] = 0
	favor["Carpicorn Party"] = 0
	favor["Interglobal Potence"] = 0
	favor["Unit Identity"] = 0
	favor["Mach-5"] = 0
	favor["New Horizon"] = 0
	favor["Trascend"] = 0
	variables["politicalFavor"] = favor
	'''

	while not variables["finished"] :
		clearScreen()
		variables = doLoop(variables)
		calls += 1
		time.sleep(frameRate/variables["currentSpeed"])

	
	

if __name__== "__main__":
  main()


'''
OK	0.START

OK	1.LAUNCH

OK	2.NAVIGATING
		21.SET NEW DIRECTION
		22.SET NEW SPEED
		23.METEOR ENCOUNTER
		

	3.BATTLE
		

	4.PLANET MAIN MENU
OK		41.MARKET
			411.BUY MINERAL
			412.SELL MINERAL
OK		42.SUPPLIES
			421.BUY SUPPLIES
			422.CHARGE ENERGY
		43.GARAGE
			431.REPAIR SHIP
			432.UPGRADE CANNONS
			433.UPGRADE SHIP ARMOR
			434.UPGRADE EVASION CONTROLS
			435.UPGRADE PROPULSORS
			435.UPGRADE TROOPS  STORAGE
			435.UPGRADE MINERAL STORAGE
		44.BARRACS
			441.UPGRADE TROOPS
			442.HIRE TROOPS
		45.CAPITOL
			451.FUND PARTY
			452.START RAISING
		46.EXPLORATORY
			461.BUY NEW PLANET LOCATION
		47.LEAVE
		
		.ECONOMY?

'''
