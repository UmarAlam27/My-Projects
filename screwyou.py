import time
import webbrowser
import random
while (True):
    sites = random.choice(['google.com','youtube.com', 'facebook.com'])
    visit = 'http://{}'.format(sites)
    webbrowser.open(visit)
    seconds= random.randrange(5,20)
    time.sleep(seconds)
