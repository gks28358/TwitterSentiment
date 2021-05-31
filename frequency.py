# -*- coding: utf-8 -*-

import sys
import json
import codecs
import csv
import urllib
#import pandas as pd
import re
import io
import string


def conversions(term):
    subbed = re.sub("\u2019", "'", term)
    return subbed

def datadictionary(ft):
    # affinfile =  open(fp.name)
    # scores = {} # initialize an empty dictionary
    # for line in affinfile.readlines():
	#     term, score = line.split("\t") # The file is tab-delimited. "\t" means "tab character”
	#     scores[term] = int(score) # Convert the score to an integer.
    #print(scores.items()) # Print every (term, score) pair in the dictionary
    
    freq2 = {}
    frequency ={}
    word = []
    words = []
    tweet = {}
    tweets = {}
    tweettext = []
    tweets_data = []
    #tweets_data['search_metadata'] = []
    dictionary = {}
    value = 0
    count = 0  
    with io.open(ft.name,"r", encoding="utf-8") as tweet_file:
    
        for line in tweet_file:
            tweets_data = json.loads(line)
            #print tweets_data
            
            
        for p in tweets_data['statuses']:
            words.append(p['text'].lower().encode('utf-8').decode('unicode_escape').encode('ascii','ignore').encode('utf-8').split(" "))

            
        
        for term in words:
            
            for word in term:
                freqcount = 0
                word = word.replace('.', '').replace(',', '').replace('?','').replace('!','').replace('(','').replace(')','')
                frequency[word] = count 
        #print frequency
                if word not in freq2:
                    freq2[word] = float(1)
                else:
                #freqcount = freqcount + 1
                    freq2[word] += float(1) 
        #print freq2

        for word in freq2:
            count = float(count) + float(freq2[word])
        #print count
        for word in freq2:
            print str(word) + ' ' ,  (float(freq2[word]/count))

def lines(fp):
    print str(len(fp.readlines()))

def main():
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
    
    #lines(sent_file)
    #lines(tweet_file)
    datadictionary(tweet_file)

if __name__ == '__main__':
    main()
