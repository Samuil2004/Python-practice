# import random

# def game():
#   hiddenNum = random.randint(0,100)

#   while True:
#     guessedNum = int(input("What is your next guess?: "))
#     if guessedNum == hiddenNum:
#       print("Congratulations you won!")
#       play_again = input("If you want to play again type Y")
#       if play_again == "Y":
#         game()
#       else:
#         break;
#     elif guessedNum > hiddenNum:
#       print("Your guess is too high")
#     else:
#       print("Your guess is too low")

# game()








# companyName = input("What is the company name")
# # while True:
# numOfAdultTickets = int(input("What is the number of adult tickets"))
#   # if numOfAdultTickets >= 1 and numOfAdultTickets <= 400:
#   #   break;

# # while True:
# numOfChildTickets = int(input("What is the number of child tickets"))
#   # if numOfChildTickets >= 25 and numOfChildTickets <= 120:
#   #   break;

# # while True:
# priceOfAnAdultTicket = float(input("What is the price of an adult ticket"))
#   # if priceOfAnAdultTicket >= 100.00 and priceOfAnAdultTicket <= 1600.00:
#   #   break;

# # while True:
# priceOfService = float(input("What is the service price"))
#   # if priceOfService >= 10.00 and priceOfService <= 50.00:
#   #   break;

# totalPrice = (numOfAdultTickets * (priceOfAnAdultTicket +priceOfService) + numOfChildTickets * ((priceOfAnAdultTicket * 0.3)+priceOfService)) * 0.8

# print(f"The profit of your agency from {companyName} tickets is {totalPrice: .2f} lv.")


# while True:
#   minutesOfWalkS = input()
#   if minutesOfWalkS:
#     minutesOfWalkI = int(minutesOfWalkS)
#     if minutesOfWalkI >=1 and minutesOfWalkI <= 50:
#       break;

# while True:
#   numOfWalksPerDay = int(input())
#   if numOfWalksPerDay >=1 and numOfWalksPerDay <= 10:
#     break;

# while True:
#   consumedCalories = int(input())
#   if consumedCalories >=100 and consumedCalories <= 4000:
#     break;

# if (minutesOfWalk * 5)*numOfWalksPerDay >= consumedCalories*0.5:
#   print(f"Yes, the walk for your cat is enough. Burned calories per day: {(minutesOfWalk * 5)*numOfWalksPerDay}.")
# else:
#   print(f"No, the walk for your cat is not enough. Burned calories per day: {(minutesOfWalk * 5)*numOfWalksPerDay}.")




# while True:
#   typeOfDrink = input()
#   if typeOfDrink == "Espresso" or typeOfDrink == "Cappuccino" or typeOfDrink == "Tea":
#     break;

# while True:
#   sugar = input()
#   if sugar == "Without" or sugar == "Normal" or sugar == "Extra":
#     break;

# while True:
#   numOfDrinks = int(input())
#   if numOfDrinks >= 1 and numOfDrinks <= 50:
#     break;


# if typeOfDrink == "Espresso":
#   match sugar:
#     case "Without":
#       totalPrice = (numOfDrinks * 0.9) * 0.65
#     case "Normal":
#       totalPrice = numOfDrinks
#     case "Extra":
#       totalPrice = numOfDrinks * 1.2
#   if numOfDrinks >= 5:
#     totalPrice = totalPrice * 0.75


# if typeOfDrink == "Cappuccino":
#   match sugar:
#     case "Without":
#       totalPrice = numOfDrinks * 0.65
#     case "Normal":
#       totalPrice = numOfDrinks * 1.2
#     case "Extra":
#       totalPrice = numOfDrinks * 1.6

# if typeOfDrink == "Tea":
#   match sugar:
#     case "Without":
#       totalPrice = (numOfDrinks * 0.5) * 0.65
#     case "Normal":
#       totalPrice = numOfDrinks * 0.6
#     case "Extra":
#       totalPrice = numOfDrinks * 0.7

# totalPrice = 0

# if typeOfDrink == "Espresso":
#     if sugar == "Without":
#         totalPrice = (numOfDrinks * 0.9) * 0.65
#     elif sugar == "Normal":
#         totalPrice = numOfDrinks * 1.0
#     elif sugar == "Extra":
#         totalPrice = numOfDrinks * 1.2
#     if numOfDrinks >= 5:
#         totalPrice *= 0.75

# elif typeOfDrink == "Cappuccino":
#     if sugar == "Without":
#         totalPrice = numOfDrinks * 0.65
#     elif sugar == "Normal":
#         totalPrice = numOfDrinks * 1.2
#     elif sugar == "Extra":
#         totalPrice = numOfDrinks * 1.6

# elif typeOfDrink == "Tea":
#     if sugar == "Without":
#         totalPrice = (numOfDrinks * 0.5) * 0.65
#     elif sugar == "Normal":
#         totalPrice = numOfDrinks * 0.6
#     elif sugar == "Extra":
#         totalPrice = numOfDrinks * 0.7

# if totalPrice >= 15:
#   totalPrice = totalPrice * 0.8

# print(f"You bought {numOfDrinks} cups of {typeOfDrink} for{totalPrice : .2f} lv.")




# while True:
#   numOfGroups = int(input())
#   if numOfGroups >=1 and numOfGroups <=1000:
#     break

# totalNumOfPeople = 0;
# musala = 0;
# monblan = 0;
# kilimandjaro = 0;
# k2 = 0;
# everest = 0;

# for i in range(0,numOfGroups):
#   while True:
#     numOfPeople = int(input())
#     if numOfPeople >= 1 and numOfPeople <= 1000:
#       break;
#   totalNumOfPeople += numOfPeople;
#   if numOfPeople <= 5:
#     musala += numOfPeople;
#   elif numOfPeople >=6 and numOfPeople <= 12:
#     monblan += numOfPeople;
#   elif numOfPeople >= 13 and numOfPeople <= 25:
#     kilimandjaro += numOfPeople;
#   elif numOfPeople >= 26 and numOfPeople <= 40:
#     k2 += numOfPeople;
#   elif numOfPeople >= 41:
#     everest += numOfPeople;


# print(f"{(musala / totalNumOfPeople) * 100:.2f}%")
# print(f"{(monblan / totalNumOfPeople) * 100:.2f}%")
# print(f"{(kilimandjaro / totalNumOfPeople) * 100:.2f}%")
# print(f"{(k2 / totalNumOfPeople) * 100:.2f}%")
# print(f"{(everest / totalNumOfPeople) * 100:.2f}%")





# budget = float(input())

# while True:
#   name = input()
#   if budget <= 0:
#      break;
#   if name == "ACTION":
#     print(f"We are left with {budget:.2f} leva.")
#     break
#   elif len(name) > 15:
#     budget = budget * 0.8
#   else:
#       salary = float(input())
#       if salary > budget:
#         print(f"We need {salary-budget:.2f} leva for our actors.")
#         break
#       else:
#         budget = budget - salary

# 2000000
# 19
# totalNumOfGames = 0;
# wins = 0;
# lost = 0;

# while True:
#   name = input()
#   if name == "End of tournaments":
#     print(f"{(wins/totalNumOfGames)*100:.2f}% matches win")
#     print(f"{(lost/totalNumOfGames)*100:.2f}% matches lost")
#     break
#   numOfGames = int(input())
#   totalNumOfGames += numOfGames
#   for i in range(1,numOfGames+1):
#     pointsD = int(input())
#     pointsO = int(input())
#     if pointsD > pointsO:
#       print(f"Game {i} of tournament {name}: win with {pointsD - pointsO} points.")
#       wins += 1
#     else:
#       print(f"Game {i} of tournament {name}: lost with {pointsO - pointsD} points.")
#       lost += 1

# import math
# figure = input()

# if figure == "square":
#   a = float(input())
#   print(f"{a*a:.3f}")
# elif figure == "rectangle":
#   a = float(input())
#   b = float(input())
#   print(f"{a*b:.3f}")
# elif figure == "circle":
#   a = float(input())
#   print(f"{a*a*(math.pi):.3f}")
# elif figure == "triangle":
#   a = float(input())
#   b = float(input())
#   print(f"{(a*b)/2:.3f}")



# minutes = int(input())
# walks = int(input())
# calories = int(input())

# if walks * minutes * 5 >= calories*0.5:
#   print(f"Yes, the walk for your cat is enough. Burned calories per day: {walks * minutes * 5}.")
# else:
#   print(f"No, the walk for your cat is not enough. Burned calories per day: {walks * minutes * 5}.")




# import math 

# buckets = int(input())
# rolls = int(input())
# glovesPrice = float(input())
# painterPrice = float(input())

# totalPrice = buckets * 21.50 + rolls*5.20 + math.ceil(rolls*0.35)*glovesPrice + math.floor(buckets*0.48)*painterPrice

# print(f"This delivery will cost {totalPrice/15:.2f} lv.")

# import math 

# planned = int(input())
# employees = int(input())
# days = int(input())

# processors = math.floor((employees * days * 8)/3)

# if planned > processors:
#   print(f"Losses: -> {(planned-processors)*110.10:.2f} BGN")
# elif planned <= processors:
#   print(f"Profit: -> {(processors-planned)*110.10:.2f} BGN")


# month = input()
# hours = int(input())
# people = int(input())
# dayTime = input()

# price = 0;

# if month == "march" or month == "april" or month == "may":
#   if dayTime == "day":
#     price = 10.50
#   else:
#     price = 8.40
# elif month == "june" or month == "july" or month == "august":
#   if dayTime == "day":
#     price = 12.60
#   else:
#     price = 10.20

# if people >= 4:
#   price = price *0.9

# if hours >= 5:
#   price = price * 0.5

# print(f"Price per person for one hour: {price:.2f}")
# print(f"Total cost of the visit: {price*hours*people:.2f}")



# num = int(input())

# group1 = 0;
# group2 = 0;
# group3 = 0;
# totalFood = 0;
# for i in range(0,num):
#   food = float(input())
#   if food >= 100 and food<200:
#     group1 += 1;
#   elif food >= 200 and food < 300:
#     group2 +=1
#   else:
#     group3 +=1
#   totalFood +=food

# print(f"Group 1: {group1} cats.")
# print(f"Group 2: {group2} cats.")
# print(f"Group 3: {group3} cats.")
# print(f"Price for food per day: {(totalFood/1000)*12.45:.2f} lv.")

# adults = 0
# children = 0

# while True:
#   age = input()
#   if age == "Christmas":
#     break
#   if int(age) <= 16:
#     children+=1
#   else:
#     adults +=1

# print(f"Number of adults: {adults}")
# print(f"Number of kids: {children}")
# print(f"Money for toys: {children*5}")
# print(f"Money for sweaters: {adults*15}")



locations = int(input())

for i in range(0,locations):
  expected = float(input())
  days = int(input())
  total = 0
  for j in range(0,days):
    actual = float(input())
    total += actual
  
  if expected <= total/days:
    print(f"Good job! Average gold per day: {total/days:.2f}.")
  else:
    print(f"You need {expected - total/days:.2f} gold.")
