# two1-httpie
## A fork of [HTTPie](https://github.com/jkbrzt/httpie) for the 21 Bitcoin Computer

Usage is at the moment identical to the original, for example:

`$ http httpie.org`

```
HTTP/1.1 302 Found
Connection: close
Content-Length: 292
Content-Type: text/html; charset=iso-8859-1
Date: Sun, 22 Nov 2015 07:47:56 GMT
Location: https://github.com/jkbrzt/httpie
Server: Apache/2.2.15 (CentOS)
X-Awesome: Thanks for trying HTTPie :)

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>302 Found</title>
</head><body>
<h1>Found</h1>
<p>The document has moved <a href="https://github.com/jkbrzt/httpie">here</a>.</p>
<hr>
<address>Apache/2.2.15 (CentOS) Server at httpie.org Port 80</address>
</body></html>
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
