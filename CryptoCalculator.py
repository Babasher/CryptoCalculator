import logging
logging.basicConfig(level = logging.DEBUG)

def calculate():

    print("Hello! How much money did you invest into bitcoin?")
    investment = int(input())
    print("At was price?")
    initialPrice = int(input())
    print("What is the current price of bitcoin")
    finalPrice = int(input())

    percentage = (initialPrice,finalPrice)
    



def percentage(initalPrice,finalPrice):
    decrease = float(finalPrice) - float(initalPrice)
    percentage = (decrease/initalPrice) * 100.0
    return percentage

logging.debug(percentage(9784,10094))
