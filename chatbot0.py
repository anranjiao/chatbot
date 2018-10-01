#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#多选择回答，简单问候
from wxpy import *
bot = Bot()

import random
name = 'Annora'
responses = {'Hello': ['Hello! I am your assistant, {0}'.format(name), 
                           'Hi, call me {0}, what can I do for you?'.format(name), 
                            ':) This is {0}, what would you like to do?'.format(name)], 
            'How is it going?': ['Great! It is my pleasure to help you.',
                                'Pretty good. What would you like to know about stocks?',
                                'Everything goes well. I know many things about stocks.']}

def respond(message):
    if message in responses:
        bot_message = random.choice(responses[message])
    else:
        bot_message = random.choice(responses['default'])
    return bot_message

a = respond('Hello')
print(a)

@bot.register(bot.self, except_self=False)
def reply_msg(msg):
    a = respond(msg.text)
    msg.reply(a)
