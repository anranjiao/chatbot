#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from wxpy import *
bot = Bot()

from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
trainer = Trainer(config.load("/Users/Annora/Desktop/chatbot3/config_spacy.yml"))
training_data = load_data('/Users/Annora/rasa_nlu_chi/data/examples/rasa/rasa-stock.md')
interpreter = trainer.train(training_data)
#单轮多次查询
from iexfinance import Stock
params = {}
def respond(message,params):
    entities = interpreter.parse(message)['entities']
    for ent in entities:
        params[ent["entity"]] = str(ent["value"])
    stock = Stock(params['symbol'])
    if len(params)>1:
        intent, key = '', ''
        intent, key = get_intent(params, stock)
        response = 'the {} of {} is: {}'.format(key, params['symbol'], intent)
    else:
        intent, key = 'stock_search', 'sym'
        response = 'What would you like to know about {}'.format(params['symbol'])
    return response, params, key

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

@bot.register(bot.self, except_self=False)
def reply_msg(msg):
    global params
    key = ''
    response, params, key = respond(msg.text,params)
    print(params)
    msg.reply(response)
