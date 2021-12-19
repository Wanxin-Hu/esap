import random

def print_intro():
	print('''Congrats,  you  are  the  newest  ruler  of  ancient  Samaria,  elected  for  a  ten  year  term of  office.   Your  duties  are  to  distribute  food,  direct  farming,  and  buy  and  sell  land as  needed  to  support  your  people.   Watch  out  for  rat  infestations  and  the  resultant plague!  Grain is the general currency,  measured in bushels.  The following will helpyou in your decisions:\n*  Each person needs at least 20 bushels of grain per year to survive.\n*  Each person can farm at most 10 acres of land.\n*  It takes 2 bushels of grain to farm an acre of land.\n*  The market price for land fluctuates yearly.\nRule wisely and you will be showered with appreciation at the end of your term.\nRulepoorly and you will be kicked out of office!''')

def ask_to_buy_land(bushels, cost):
	#Ask user how many ushels to spend buying land.
	acres = int(input("How many acres will you buy? (Enter 0 if you don't want to buy any.) \n"))
	while (acres * cost > bushels):
		print ("O great Hammurabi, we have but " , bushels, " bushels of grain!")
		acres = int(input("How many acres will you buy? "))
	return acres

def ask_to_sell_land(acres):
	#Ask user how much land they want to sell. 
	#can't ask whe they decide to buy land
	acre = int(input("How many acres will you sell?\n"))
	while (acre > acres):
		print ("O great Hammurabi, we have but " , acres, " acres of land!")
		acre = int(input("How many acres will you sell?\n "))
	return acre

def ask_to_feed(bushels):
	#Ask user how many bushels they want to use for feeding. 
	bushel = int(input("How many bushels will you use for feeding?\n"))
	while bushel > bushels:
		print ("O great Hammurabi, we have but" , bushels, " bushels of grain!\n")
		bushel = int(input("How many bushels will you use for feeding?\n"))
	return bushel

def ask_to_cultivate(acres, population, bushels):
	#Ask user how much land they want to plant seed in.
	acre = int(input("How much land will you plant seed in?\n"))
	while (population * 10 < acre):
		print("O great Hammurabi, we have but ", population, " people who can farm!")
		acre = int(input("How much land will you plant seed in?\n"))
		while ((acre *2) > bushels):
			print("O great Hammurabi, we have but ", bushels, " bushels of grain!")
			acre = int(input("How much land will you plant seed in?\n"))
			while(acre > acres):
				print("O great Hammurabi, we have but ", acres, " acres of land!")
				acre = int(input("How much land will you plant seed in?\n"))
	return acre

def isPlague():
	#15% there is a plague 
	ran = random.randint(1, 100)
	if (ran <= 15):
		return True
	else:
		return False

def numStarving(population, bushels):
	#if more than 45% are starving, game ends
	people_survive = bushels // 20
	if (people_survive < population):
		return population - people_survive
	else:
		return 0

def numImmigrants(land, grainInStorage, population, numStarving):
	#if people are starving, no one comes to this country
	if (numStarving > 0):
		return 0
	else:
		return int((20 * land + grainInStorage) /((100 * population) + 1))

def getHarvest():
	number = random.randint(1, 8)
	return number

def doRatsInfest():
	#return the part
	possibility = random.randint(1, 100)
	if (possibility <= 40):
		return (random.randint(1, 3)) / 10
	else:
		return 0

def priceOfLand():
	#the player need to know
	return random.randint(16, 22)

	
def Hammurabi():

	starved = 0
	immigrants = 5
	population = 100
	harvest = 3000          # total bushels harvested
	bushels_per_acre = 3    # amount harvested for each acre planted
	rats_ate = 200          # bushels destroyed by rats
	bushels_in_storage = 2800
	acres_owned = 1000
	cost_per_acre = 19      # each acre costs this many bushels
	plague_deaths = 0


	print_intro()

	for year in range(1, 11):
		print("O great Hammurabi!\nYou are in year " + str(year) + " of your ten year rule.\nIn the previous year " + str(int(starved)) + " people starved to death.\nIn the previous year " + str(int(immigrants)) + " people entered the kingdom.\nThe population is now " + str(int(population)) + ".\nWe harvested "+str(int(harvest)) + " bushels at " + str(int(bushels_per_acre)) + " bushels per acre.\nRats destroyed " + str(int(rats_ate)) + " bushels, leaving " + str(int(bushels_in_storage)) + " bushels in storage.\nThe city owns " +str(int(acres_owned)) + " acres of land.Land is currently worth " + str(int(cost_per_acre)) + " bushels per acre.\nThere were " + str(int(plague_deaths)) + " deaths from the plague.")

######buy land : land++, bushel--
		land_bought = ask_to_buy_land(bushels_in_storage, cost_per_acre)
		if (land_bought != 0):
			bushels_in_storage -= land_bought * cost_per_acre
			acres_owned += land_bought
		else:
######sell lnad: land--, bushel ++
			land_sold = ask_to_sell_land(acres_owned)
			bushels_in_storage += land_sold * cost_per_acre
			acres_owned -= land_sold

######feed : bushel--
		bushel_to_feed = ask_to_feed(bushels_in_storage)
		bushels_in_storage -= bushel_to_feed

######harvest: bushel++, differ from years to years. 
		bushels_per_acre = getHarvest()
		harvest = ask_to_cultivate(acres_owned, population, bushels_in_storage) *bushels_per_acre
		bushels_in_storage = bushels_in_storage + harvest 

######plague: population -- 
		if(isPlague()):
			plague_deaths = int(population / 2)
			population -= plague_deaths

#######starving: population --
		starved = numStarving(population, bushel_to_feed)
######too many starving: end game at 45%
		if (float(starved) > (population * 0.45)):
			print("YOU SUCK AT THIS!!!\n YOU PEOPLE DIED OUT!!!\n SEE YOU ON THE GUILLOTINE!!")
			break
		else:
			population = population - starved
########immigrant : population ++
		immigrants = numImmigrants(acres_owned, bushels_in_storage, population, starved)
		population += immigrants

######rat: bushel-- 
		rats_ate = bushels_in_storage * doRatsInfest()
		bushels_in_storage -= rats_ate

######price of land changes every years
		cost_per_acre = priceOfLand()

		int(population)
		int(bushels_in_storage)
		int(acres_owned)
		
		if year==10:
			print("O great Hammurabi, YOU MADE IT!")
			print("Your kingdom has " + poopulation + "people, " + bushels_in_storage + " bushels in storage, and " + acres_owned + "acres owned. GOOD JOB!!")

			break


Hammurabi()