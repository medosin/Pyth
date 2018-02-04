import random
import webbrowser
url=random.randrange(3)
urls=["http://www.twitter.com","http://www.google.com","http://www.facebook.com"]
webbrowser.open(urls[url])
