# -*- coding: utf-8 -*-

import sys
import json
import codecs
import csv
import urllib
import re
import io
import string


def conversions(term):
    subbed = re.sub("\u2019", "'", term)
    return subbed

def datadictionary(ft, fp):
    affinfile =  open(fp.name)
    scores = {} # initialize an empty dictionary
    for line in affinfile.readlines():
	        term, score = line.split("\t") # The file is tab-delimited. "\t" means "tab character”
	        scores[term] = int(score) # Convert the score to an integer.
            #print(scores.items()) # Print every (term, score) pair in the dictionary
    wordt3 = {}
    wordt2 = []
    wordt = []
    words = []
    tweet = {}
    tweets = {}
    #splittweet = {}
    tweet_data = []
    tweettext = []
    
    #tweets_data['search_metadata'] = []
    dictionary = {}
    value = 0
    with io.open(ft.name,"r", encoding="utf-8") as tweet_file:
        for line in tweet_file:
            #print line
            #tweets_data = line
            tweettext = json.loads(line)
            #print tweettext
            for i in tweettext['statuses']:
                 #if "text" in i.keys():
                    #tweet_data.append(i["text"])
                    #print tweet_data
                    words.append(i['text'].lower().encode('utf-8').decode('unicode_escape').encode('ascii','ignore').encode('utf-8').split())
        #print words
            #tweet_data.append(tweettext['text'])
            #print tweet_data
            
            #print tweet_data['text']
        #print tweettext[2]
            #tweettext.append(tweets_data['statuses']

        #print tweets_data
            
        #for i in tweettext:       
            #wordt = json.loads(i)
           # wordt2 = (wordt['statuses'])
        #print wordt2
        
        #for j in tweet_data:    
            #wordt2 = dict(wordt2['text'])
            #words.append(tweet_data['text'].lower().encode('utf-8').decode('unicode_escape').encode('ascii','ignore').encode('utf-8').split(" "))
                
            #print words
            #words = re.sub(".|?|!|(|)", "",words)
        
            #word.append(tweettext[term].lower().encode('utf-8').decode('unicode_escape').encode('ascii','ignore').encode('utf-8')] = score
        #     #print tweettext.keys()
            #print wordt2            
            
        for term in words:
            for word in term:
                #print word
                for key in scores:
                #print (str(key) + str(term) + scores(key))
        #     term = term.split(" ")
        #     words.append(term)
        #     print(words)
                #dictionary = dict.fromkeys(words,0)
                #print dictionary.items()
                    if word == key:
                        #print (key + str(word))
                        value = value + scores[key]
            print str(value)
            value = 0
            
                #     #print key
                #     if dictionary[key] in scores.keys():
                #         #tweets_data[term] = tweets_data.value() + dictionary.value()
                #         #print tweettext[term]
                #         #print (key) 
                #         #print ([key])
                #         #tweettext[term] = dictionary[key] + tweettext[term] 
                #         #print tweettext[term] 
                #     #else:
                #         #print(dictionary[key])
                        
                #         #print key
                #         print dictionary[key] 
                #         print tweettext[term] 
                #         #print tweettext[term] 
                    
                         
                #print tweettext[term]
                #words = []
                #dictionary = {}

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    #lines(sent_file)
    #lines(tweet_file)
    datadictionary(tweet_file, sent_file)

if __name__ == '__main__':
    main()
