
import requests
import pywin
import pprint


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)


if __name__ == '__main__':
    speak("hello FRIENDS  I M GONNA SHOW YOU A NEWSTELLER")
    url = ('http://newsapi.org/v2/top-headlines?'
           'sources=the-hindu&'
           'apiKey=72d285323fdd46abaf17e464736030d0')
    r = requests.get(url)
    response = r.json()
    pprint.pprint(response)

    for i in response['articles']:
        speak(i['title'])
        speak("moving on to the next news")