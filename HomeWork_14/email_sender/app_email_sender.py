from modules.Subscribers.utils import loadSubscribers
from modules.Subscribers.email import sendemail

subscribers = loadSubscribers()
n = 1
for n in range(1, len(subscribers)):
    sendemail(subscribers[n]["email"], subscribers[n]['name'], subscribers[0]['email'])
    n += 1
