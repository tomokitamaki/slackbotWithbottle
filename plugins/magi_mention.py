from slackbot.bot import respond_to
import requests
import sys

@respond_to('hey (.*)')
def cheer(message, something):
    if something == '疲れた':
        message.reply('Dont say {}'.format(something))
    else:
        message.reply('there are not {}'.format(something))
@respond_to('tenki')
def cheer(message):
    r = requests.get('http://172.17.0.3/plz/tenki/{}'.format(message))
    message.reply(r.text)
@respond_to('シュガートースト')
def cheer(message):
    message.reply('くだらないこというな')
@respond_to('つかれた')
def cheer(message):
    message.reply('ふぁいと')
@respond_to('I love ([A|B|C|D|E|F|G|H]$)')
def cheer(message, something):
    r = requests.get('http://172.17.0.3/plz/AH/{}'.format(something))
    message.reply(r.text)
