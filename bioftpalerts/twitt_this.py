#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of BioLoader.
#
# Files included in this package BioLoader are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.
import sys
import tweepy
import twitter_oauth
from pymongo import Connection

def twitt_me(twitt_string):
	"""
	Accepts twitts as string and post on bioftpalerts twitter account, 
	all keys and secrets are stored in MongoDB. If access key and secret
	is expired then it will call the OAuth to get new values and update
	in database.
	"""
	#Connect to MongoDB on the default host and port
	connection = Connection()

	#Access the bioftpalerts database
	db = connection.bioftpalerts

	#Get the consumer collection
	consumer = db.twitter_consumer

	CONSUMER_KEY = consumer.find_one()["key"].encode()
	CONSUMER_SECRET = consumer.find_one()["secret"].encode()

	#Get the access collection
	access = db.twitter_access

	ACCESS_KEY = access.find_one()["key"].encode()
	ACCESS_SECRET = access.find_one()["secret"].encode()
	
	try:	
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
		api = tweepy.API(auth)
		api.update_status(twitt_string)
			
	except tweepy.TweepError:
		print "Invalid / expired Token"
		print "Unexpected error:", sys.exc_info()[0]
		access_key, access_secret = twitter_oauth.get_access(CONSUMER_KEY, CONSUMER_SECRET)
		db.twitter_access.update({"key":ACCESS_KEY}, {"key":access_key,"secret":access_secret})
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(access_key, access_secret)
		api = tweepy.API(auth)
		api.update_status(twitt_string)
	


