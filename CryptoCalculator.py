import logging
logging.basicConfig(level=logging.DEBUG)


def run():
    cryptoSelect()

def cryptoSelect():
    print("Please enter: 1 for Bitcoin")
    print("Please enter: 2 for ETH")
    print("Please enter: 3 for LTC")
    userInput = int(input())

    while userInput < 1 or userInput > 3:
        garbage = userInput

        print(str(garbage) + " is not a valid option;\n"
        "Please enter: 1 for Bitcoin \n"
        "Please enter: 2 for ETH \n"
        "Please enter: 3 for LTC ")

        userInput = int(input())

    cryptoOptions = [(1, "BTC"), (2, "ETH"), (3, "LTC")]
    def selectCrypto(userChoice):
        return [choice for (option, choice) in cryptoOptions if userChoice == option]

    print("You have selected " + str(selectCrypto(userInput)) + " as your Crypto Currency.")
    calculateV2(str(selectCrypto(userInput)))


def calculateV2(userInput):
    # user input a number
    print("Enter number of investments you made for " + userInput)
    numOfInvestments = int(input())
    count = 1

    # Make an empty List
    cryptoPriceList = []
    #Commenting out test code; print("cryptoPriceList: " + str(cryptoPriceList))
    investmentList = []
    #Commenting out test code; print("Investment List: " + str(investmentList))


    # while loop from 1 to = number
    while (count <= numOfInvestments):
        print("What was the price of " + userInput +" at investment number " + str(int(count)))
        cryptoPrice = float(input())
        #print("cryptoPrice:" + str(cryptoPrice)) #NOT SURE IF YOU WANTED TO KEEP THIS IN FINAL PRODUCT OR NOT
        cryptoPriceList.append(cryptoPrice)
        #Commenting out test code; print("PriceList Append:" + str(cryptoPriceList.append(cryptoPrice)))
        print("How much did you invest at investment number " + str(int(count)))
        userInvestment = float(input())
        #print("User Investment: " + str(userInvestment)) #(NOT SURE IF YOU WANTED TO KEEP THIS IN FINAL PRODUCT OR NOT)
        investmentList.append(userInvestment)
        #Commenting out test code; print("Investment List Append: " + str(investmentList.append(userInvestment)))
        count += 1

    print()

    #get the average from the lists
    print(userInput + " PRICES")
    aveCryptoPrice = getAverage(cryptoPriceList)
    print("Average " + userInput + " Price: " + str(aveCryptoPrice))
    print()

    print("YOUR INVESTMENTS")
    aveUserInvestments = getAverage(investmentList)
    print("Average User Investments: " + str(aveUserInvestments))
    print()

    print(
        "What is the current price of " + userInput)  # Later on we'll implement a scraper to grab the current price of bitcoin or whichever crypto!
    finalPrice = float(input())
    print()
    print("Final Price: ${:,.2f}".format(finalPrice))
    percentage = findPercentage(aveCryptoPrice, finalPrice)
    print("Percentage Growth: {:.2f}%".format(percentage*100))
    currValue = ((percentage) * aveUserInvestments) + aveUserInvestments
    
    results(currValue, aveUserInvestments,userInput)

def results(x, y, typeOf):
    if (x > y):
        print("Your current "+ typeOf + " is worth: ${:,.2f}. Currently a net profit!".format(float(x)))
    elif (x == y):
        print("Your current "+ typeOf + " is worth: ${:,.2f}. You broke even.".format(float(x)))
    else:
        print("Your current "+ typeOf + " is worth: ${:,.2f}. Currently a net loss.".format(float(x)))

def calculate():
    print("Hello! How much money did you invest into Bitcoin?")
    investment = int(input())
    print("At what price?")
    initialPrice = int(input())
    print(
        "What is the current price of Bitcoin?")  # Later on we'll implement a scraper to grab the current price of bitcoin or whichever crypto!
    finalPrice = int(input())

    percentage = findPercentage(initialPrice, finalPrice)
    currValue = ((percentage) * investment) + investment

    if (currValue > investment):
        print("Your current bitcoin is worth: ${:,.2f}. Currently a net profit!".format(float(currValue)))
    elif (currValue == investment):

        print("Your current bitcoin is worth: ${:,.2f}. You broke even.".format(float(currValue)))
    else:
        print("Your current bitcoin is worth: ${:,.2f}. Currently a net loss.".format(float(currValue)))

def findPercentage(iPrice, fPrice):
    decrease = float(fPrice) - float(iPrice)
    perc = float(decrease) / float(iPrice)  # I have to fix the math here, I assume!
    return perc

def getAverage(*list):
    ave = sum(*list)/len(*list)
    print(*list)
    return ave

run()
#calculateV2()
