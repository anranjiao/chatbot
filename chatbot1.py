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

#单轮单次查询，支持不同形式的提问和一定容错
from iexfinance import Stock
params = {}
def respond(message, params): 
    entities = interpreter.parse(message)['entities']
    for ent in entities:
        params[ent["entity"]] = str(ent["value"])
    stock = Stock(params['symbol'])
    response, entity = intent(params, stock)
    return response, params, entity

def intent(params,stock):
    if 'price' in params:
        intent = str(stock.get_price())
        entity = 'price'
    elif 'cap' in params:
        intent = str(stock.get_market_cap())
        entity = 'cap'
    elif 'volume' in params:
        intent = str(stock.get_volume())
        entity = 'volume'
    return intent, entity

@bot.register(bot.self, except_self=False)
def reply_msg(msg):
    params = {}
    entity = ''
    response, params, entity = respond(msg.text,params)
    print(params)
    msg.reply('the {} of {} is: {}'.format(entity, params['symbol'], response))