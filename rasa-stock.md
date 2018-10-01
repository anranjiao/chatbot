## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir

## intent: stock_search
- i'm looking for a stock
- I would like to know about the stock
- I am searching for a stock
- i'm looking for a stock called [AAPL](symbol)
- i am interested in [PG](symbol)
- show me the stock of [Tesla Inc.](name)
- show me the [price](price) of [FB](symbol)
- show me stock which is [19.82](price)
- [SOHU](symbol) with [19.82](price)
- show me the [market value](cap) of [SOHU](symbol)
- i am looking for the [capitalization](cap) of the stock in [Apple Inc.](name)
- search for stocks
- something about [PG](symbol)
- something about the stock of [Sina Corporation](name)
- Can you tell me the [turnover](volume) of [IBM](symbol)?
- please give me the [turnover](volume) of [Apple Inc.](name)
- i need the [capitalization](cap)
- What is the [price](price)?
- I am looking for [volume](volume)
- I am looking for [price](price) of this stock
- I am looking the [company name](name)
- I am looking for the [cap](cap)
- [volume](volume) of [AMZN](symbol)

## synonym: volume
+ volum
* vlume

## synonym: capitalization
- cap
- captalization

## regex:zipcode
- [A-Z]{2,}

## regex: symbol
- hey[^\s]*