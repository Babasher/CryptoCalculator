import logging
logging.basicConfig(level=logging.DEBUG)

def calculateV2():
    # user input a number
    print("Enter number of investments you made")
    numOfInvestments = int(input())
    count = 1

    # Make an empty List
    cryptoPriceList = []
    #Commenting out test code; print("cryptoPriceList: " + str(cryptoPriceList))
    investmentList = []
    #Commenting out test code; print("Investment List: " + str(investmentList))


    # while loop from 1 to = number
    while (count <= numOfInvestments):
        print("What was the price of the Crypto currency at investment number " + str(int(count)))
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
    print("CRYPTO PRICES")
    aveCryptoPrice = getAverage(cryptoPriceList)
    print("Average Crypto Price: " + str(aveCryptoPrice))
    print()

    print("YOUR INVESTMENTS")
    aveUserInvestments = getAverage(investmentList)
    print("Average User Investments: " + str(aveUserInvestments))
    print()

    print(
        "What is the current price of Bitcoin?")  # Later on we'll implement a scraper to grab the current price of bitcoin or whichever crypto!
    finalPrice = float(input())
    print()
    print("Final Price: ${:,.2f}".format(finalPrice))
    percentage = findPercentage(aveCryptoPrice, finalPrice)
    print("Percentage Growth: {:.2f}%".format(percentage*100))
    currValue = ((percentage) * aveUserInvestments) + aveUserInvestments
    
    results(currValue, aveUserInvestments)

def results(x, y):
    if (x > y):
        print("Your current bitcoin is worth: ${:,.2f}. Currently a net profit!".format(float(x)))
    elif (x == y):
        print("Your current bitcoin is worth: ${:,.2f}. You broke even.".format(float(x)))
    else:
        print("Your current bitcoin is worth: ${:,.2f}. Currently a net loss.".format(float(x)))

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

'''
With the below we can ask for an input() to select which crypto they would like to determine the value and growth of:

cryptoOptions = [(1, "BTC"), (2, "ETH"), (3, "LTC")]
def selectCrypto(userChoice):
  return [choice for (option, choice) in cryptoOptions if userChoice == option]
'''

calculateV2()
