# chatbot
to search the price, the cap and the volume of stocks

这是一个基于python识别意图，使用iexfinance API，用于查询股票基本信息的聊天机器人，可以实现意图：股价（price）、市值（cap）、成交量（volume），并且集成在微信，语言为英文。

多选择回答：发送”Hello","How is it going?"，与机器人寒暄。
单轮单次查询：直接询问股票的（price）、市值（cap）、成交量（volume），如“Tell me the price of AAPL"
单轮多次查询：分步进行问询，如依次发送“something about SOHU”，“about the price”，“the cap“，”and the volume",可以获得SOHU的相关信息。
多轮多次查询：最终实现版本。可以获取机器人功能、多轮问询不同股票的相关信息。
