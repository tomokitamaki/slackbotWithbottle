from slackbot.bot import respond_to
import requests
import sys

@respond_to('hey (.*)')
def cheer(message, something):
    if something == '疲れた':
        message.reply('Dont say {}'.format(something))
    else:
        message.reply('there are not {}'.format(something))
@respond_to('つかれた')
def cheer(message):
    message.reply('ふぁいと')
@respond_to('I love ([A|B|C|D|E|H])')
def cheer(message, something):
    r = requests.get('http://172.17.0.3/plz/AH/{}'.format(something))
    message.reply(r.text)
