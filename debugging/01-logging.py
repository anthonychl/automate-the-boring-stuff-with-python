import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') # this is the basic setup
# logging.disable(logging.CRITICAL) # disable all messages at critical level or lower, and since critical is the highest, means to disable all messages


logging.debug('Start of program')
def factorial(n):
    logging.debug('factorial of :'+str(n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('incrementing total to :'+str(total))
    return total

print( factorial(5) )
logging.debug('End of program')

'''
2019-08-25 22:06:51,817 - DEBUG - Start of program
2019-08-25 22:06:51,822 - DEBUG - factorial of :5
2019-08-25 22:06:51,824 - DEBUG - incrementing total to :1
2019-08-25 22:06:51,827 - DEBUG - incrementing total to :2
2019-08-25 22:06:51,864 - DEBUG - incrementing total to :6
2019-08-25 22:06:51,868 - DEBUG - incrementing total to :24
2019-08-25 22:06:51,870 - DEBUG - incrementing total to :120
2019-08-25 22:06:51,874 - DEBUG - End of program
120

notice all the info we got
now this is good for a production or testing environment
but we dont want all those messages in our program
so we can easily disable them by uncommenting the line at the top
# logging.disable(logging.CRITICAL)

log levels:
debug  ,the lowest
info
warning
error
critical ,the highest

you can create log messages and assign levels to them accordingly
logging.debug('message on a debug level')
logging.info('message on an info level')
logging.warning('message on a warning level')
logging.error('message on an error level')
logging.critical('message on a critical level')

in order to disable the messages from printing we can use the following
logging.disable(logging.CRITICAL) or
logging.disable(logging.ERROR) or 
logging.disable(logging.WARNING) or
logging.disable(logging.INFO) or
logging.disable(logging.DEBUG) or

notice that you disable from the level you specify down
ie: logging.disable(logging.WARNING)
disables WARNING, INFO and DEBUG messages


if we want to save the logs to a file instead of displaying them
we change the basic config settings and add a filename argument:
logging.basicConfig(filename='log_messages.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') 
'''