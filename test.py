# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 

import urllib

doc = urllib.urlopen('https://www.cbr.ru/currency_base/daily.aspx?date_req=05.10.2017').read()
usd = '\xd0\x94\xd0\xbe\xd0\xbb\xd0\xbb\xd0\xb0\xd1\x80 \xd0\xa1\xd0\xa8\xd0\x90'
buf = doc.find(usd)
usd = doc[buf+len(usd)+11:buf+len(usd)+18]
eur = '\xd0\x95\xd0\xb2\xd1\x80\xd0\xbe'
buf = doc.find(eur)
eur = doc[buf+len(eur)+11:buf+len(eur)+18]

