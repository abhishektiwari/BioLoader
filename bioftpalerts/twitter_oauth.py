#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of BioLoader.
#
# Files included in this package BioLoader are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.

import tweepy

def get_access(consumer_key, consumer_secret):
	"""
	This function gets the Access key and secret from Twitter OAuth 
	"""
	mauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	try:
		auth_url = mauth.get_authorization_url()
	except tweepy.TweepError:
		print 'Error! Failed to get request token.'
	else:
		try:
			print 'Please authorize: ' + auth_url
			verifier = raw_input('PIN: ').strip()
			mauth.get_access_token(verifier)
			access_key = mauth.access_token.key
			access_secret = mauth.access_token.secret
			
			print "access_key =", access_key 
			print "access_secret", access_secret
	
			return access_key, access_secret
		
		except tweepy.TweepError:
			print 'Error! Failed to get access token.'
			

