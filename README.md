# two1-httpie
## A fork of [HTTPie](https://github.com/jkbrzt/httpie) for the 21 Bitcoin Computer

Usage is at the moment identical to the original, for example:

`$ http --verbose http://10.147.17.15:12012/fortune`

```
GET /fortune HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: bS2zfE4hSAlFQ6n5YUz8vomOtWc7hLr1iw5ReA8y9kt2li3UHDtL8oKdWZMQh7sANI2HihuXtw5PzRHmz2/Fiw==
Bitcoin-Transfer: {"payee_username": "jgarzik", "payee_address": "1FY1haXddue5unhceM5ceVZZuvpP8CwhSR", "description": "http://10.147.17.15:12012/fortune", "timestamp": 1448265196.551775, "payer": "bf_testserver", "amount": 10}
Connection: keep-alive
Host: 10.147.17.15:12012
User-Agent: two1-httpie/0.0.1

HTTP/1.0 200 OK
Content-Length: 41
Content-Type: text/html; charset=utf-8
Date: Mon, 23 Nov 2015 07:53:17 GMT
Server: Werkzeug/0.11.2 Python/3.4.2

You are going to have a new love affair.
```

1. HTTP 402 errors are handled behind the scenes using BitTransferRequests, the off-chain payment method.
2. Max price per request is currently hard-coded to 10,000 satoshis.

## Installation

Clone this repository, then install via pip::

`$ git clone https://github.com/bitcoinfees/two1-httpie.git`

`$ pip3 install --upgrade ./two1-httpie`


## Test it out!

Send me a couple of 21 BC satoshis (much appreciated as I don't have a 21 BC to mine with):

`$ http --verbose --form 10.145.66.31:5001/donate amount=<donate amount> message="optional message"`
