import logging
logging.basicConfig(level = logging.DEBUG)




def percentage(initalPrice,finalPrice):
    decrease = float(finalPrice) - float(initalPrice)
    percentage = (decrease/initalPrice) * 100.0
    return percentage

logging.debug(percentage(9784,10094))
