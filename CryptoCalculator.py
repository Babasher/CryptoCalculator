import logging
logging.basicConfig(level = logging.DEBUG)

def calculate():

    print("Hello! How much money did you invest into bitcoin?")
    investment = int(input())
    print("At was price?")
    initialPrice = int(input())
    print("What is the current price of bitcoin") #Later on we'll implement a scraper to grab the current price of bitcoin or whichever crypto!
    finalPrice = int(input())

    percentage = (initialPrice,finalPrice)




    currValue = percentage * investment


    logging.debug(initialPrice)
    logging.debug(finalPrice)
    logging.debug(percentage) #Returns a tuple, which we don't want!
    logging.debug(currValue)

    #if(currValue > investment):
       # print("You're current bitcoin is worth: " + currValue + " currently a net profit")
    #elif(currValue == investment):
      #  print("You're current bitcoin is worth: " + currValue + " You broke even!")
    #else:
     #   print("You're current bitcoin is worth: " + currValue + "currently a net loss")





def percentage(initalPrice,finalPrice):
    decrease = float(finalPrice) - float(initalPrice)
    percentage = (decrease/initalPrice) * 100.0 # I have to fix the math here, i assume!
    return percentage


logging.debug(calculate())