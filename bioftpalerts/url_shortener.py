#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of BioLoader.
#
# Files included in this package BioLoader are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.

def shortener(url):
	"""
	Accepts URL as string and shorten it using Bit.ly API service. Again
	all key and user details are stored in MongoDB database.
	"""
	try:
		from re import match
		from urllib2 import urlopen, Request, HTTPError
		from urllib import urlencode
		from simplejson import loads
		from pymongo import Connection
	except ImportError, e:
		raise Exception('Required module missing: %s' % e.args[0])
	
	if not match('http://',url) and not match('ftp://',url):
		raise Exception('URL must start with "http://" or "ftp://"')

	#Connect to MongoDB on the default host and port
	connection = Connection()

	#Access the bioftpalerts database
	db = connection.bioftpalerts

	#Get the bitly_api collection
	bitly_connect = db.bitly_api
	
	bitly_user = bitly_connect.find_one()["user"].encode()
	bitly_key = bitly_connect.find_one()["key"].encode()
	print bitly_key, bitly_user
	
	try:
		params = urlencode({'longUrl': url, 'login': bitly_user, 'apiKey': bitly_key, 'format': 'json'})
		req = Request("http://api.bit.ly/v3/shorten?%s" % params)
		response = urlopen(req)
		j = loads(response.read())
		if j['status_code'] == 200:
			return j['data']['url']
		raise Exception('%s'%j['status_txt'])
	except HTTPError, e:
	    raise('HTTP error%s'%e.read())
