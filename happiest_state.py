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
from collections import OrderedDict


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
    
    word = []
    words = []
    tweets = {}
    tweettext = []
    tweets_data = []
    dictionary = {}
    value = 0
    happystates = OrderedDict()
    

    states = OrderedDict()
    states = { 
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
        }


    #print happystates

    with io.open(ft.name,"r", encoding="utf-8") as tweet_file:
        for key in states.keys():
            happystates[key] = 0
        for line in tweet_file:
            tweets_data = json.loads(line)
            
        
        #for p in tweets_data['statuses']:
        #     print p['user']['location']
        #     print p['user']['description'].lower().encode('utf-8').decode('unicode_escape').encode('ascii','ignore').encode('utf-8')
            
            
            
        #print states.values()
   
            
            
        for p in tweets_data['statuses']:
            #print p
            words.append(p['text'].lower().encode('utf-8').decode('unicode_escape').encode('ascii','ignore').encode('utf-8').strip().split(" "))
            #words = re.sub(".|?|!|(|)", "",words)
        #print words
        #     #tweettext[term.lower().encode('utf-8').decode('unicode_escape').encode('ascii','ignore').encode('utf-8')] = score
        #     #print tweettext.keys()
        #print words
            #print p['user']['location']
            #print p['user']['description'].lower().encode('utf-8').decode('unicode_escape').encode('ascii','ignore').encode('utf-8')
            
            
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
                            for key in happystates:
                                for abv in states:
                                    #print abv
                                    if p['user']['location'] == states[abv]:
                                    #print  ("found one ") + p['user']['location']
                                        happystates[abv] = value + happystates[abv]
                                    elif (p['user']['location']).encode('utf-8').strip().find(abv) != -1:
                                        happystates[abv] = value + happystates[abv]
                        value = 0
    for (term , value) in sorted(happystates.iteritems(), key = lambda x:-x[1])[:1]:
        print str(term)
                                
                                #elif p['user']['location'] in states.values():
                                    #happystates[states] = value + happystates[state]
                                    #else:
                                        #contine
                #sorted(wordsFreqDict.keys())
                            

                    #print str(term) + ' ' + str(value)
                    #print p['user']['location']

            
                #print p['user']['description'].lower().encode('utf-8').decode('unicode_escape').encode('ascii','ignore').encode('utf-8')
                
        #print happystates.items()
            #print i
                #for j in [i].['location']:
                    #print j
    
        #print json.dumps(tweets_data['statuses'])
        #for p in tweets_data['statuses']:
           # print p
            


            
            
        # for term in words:
        #     for word in term:
        #         #print word
        #         for key in scores:
               
        #             if word == key:
        #                 #print (key + str(word))
        #                 value = value + scores[key]
        #     print str(value)
        #     value = 0
            
                
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
