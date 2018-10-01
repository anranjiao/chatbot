#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 21:19:55 2018

@author: Annora
"""
#多轮多次查询
from wxpy import *
bot = Bot()

from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config

trainer = Trainer(config.load("/Users/Annora/Desktop/chatbot3/config_spacy.yml"))
training_data = load_data('/Users/Annora/rasa_nlu_chi/data/examples/rasa/rasa-stock.md')

interpreter = trainer.train(training_data)
from iexfinance import Stock

def stock_info(message,params):   
    entities = interpreter.parse(message)['entities']
    for ent in entities:
        params[ent["entity"]] = str(ent["value"])
    stock = Stock(params['symbol'])
    if len(params)>1:
        intent, key = '', ''
        intent, key = get_intent(params, stock)
        info = 'the {} of {} is: {}'.format(key, params['symbol'], intent)
    else:
        intent, key = 'stock_search', 'sym'
        sym = params['symbol']
        info = 'What would you like to know about {}?'.format(sym)
    return info, params, key

def get_intent(params,stock):
    print(list(params)[-1])
    if  list(params)[-1] == 'price':
        intent = str(stock.get_price())
        entity = 'price'
    elif list(params)[-1] == 'cap':
        intent = str(stock.get_market_cap())
        entity = 'cap'
    elif list(params)[-1] == 'volume':
        intent = str(stock.get_volume())
        entity = 'volume'
    return intent, entity


def send_message(state, message):
    new_state, response = respond(state, message)
    return new_state, response

def respond(state, message):
    #print(interpret(message))
    new_state, response = policy(state, message)
    return new_state, response

def interpret(message):
    if 'stocks' in message:
        return 'choose'
    if 'no' in message:
        return "thanks"
    if 'yes' in message:
        return "others"
    pattern = re.compile(r'[A-Z]{2,}')
    match = pattern.search(message)
    #print(match.group())
    if match:
        if match.group() in message:
            return 'specify_stock'
    if 'what' in message:
        return 'ask_explanation'
    if 'price' or 'cap' or 'volume' in message:
        return "ask_specific"
    return 'none'

INIT=0 
CHOOSE_STOCK=1
ORDERED=2
SEARCHED = 3
END = 4

def policy(state, message):
    global info,params
    print(info)
    intent = interpret(message)
    if state == INIT:
        if intent == "ask_explanation":
            new_state = INIT
            response = "I'm a bot to help you with stocks"
        elif intent == "choose":
            new_state = CHOOSE_STOCK
            response = "ok, which one would you like to know?"
    if state == CHOOSE_STOCK:
        if intent == "specify_stock":
            new_state = ORDERED
            response = "perfect, I am on the way! {}".format(info)
        elif intent == "ask_explanation":
            new_state = CHOOSE_STOCK
            response = "I can provide the price, the cap and the volume of a stock."
    if state == ORDERED and intent == "ask_specific":
        new_state = SEARCHED
        response = "%s  Would you like to ask about another one? "%info
    if state == SEARCHED:
        if intent == "others":
            new_state = CHOOSE_STOCK
            params = {}
            response = "perfect, which one would you like to know?"
        elif intent == "thanks":
            new_state = END
            response = "Have a good day!"
    return new_state, response

def send_messages(messages):
    state = INIT
    params = {}
    for msg in messages:
        print(msg)
        entities = interpreter.parse(msg)['entities']
        if entities != []:
            global info
            info = ''
            info, params, key = stock_info(msg,params) 
        state ,response= send_message(state,msg)
        print(state, response)

send_messages([
    "what can you do for me?",
    "well then I'd like to know about stocks",
    "what do you mean by that?",
    "about SOHU",
    "the price",
    "no thanks"
])

state = INIT
params = {}
@bot.register(bot.self, except_self=False)
def reply_msg(msg):
    global state,params
    entities = interpreter.parse(msg.text)['entities']
    if entities != []:
        global info
        info = ''
        info, params, key = stock_info(msg.text,params) 
    state, a = send_message(state,msg.text)
    print(state, a)
    msg.reply(a)
