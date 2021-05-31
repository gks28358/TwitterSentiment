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

def datadictionary(ft):

    
    #word = []
    words = []
    #tweets = {}
    #tweettext = []
    tweets_data = []
    #dictionary = {}
    hashtags = {}
    hashlist = []
    value = 0



    with io.open(ft.name,"r", encoding="utf-8") as tweet_file:

        for line in tweet_file:
            tweets_data = json.loads(line)
          
        for p in tweets_data['statuses']:
            #print p    
                        #words.append(p['text'].lower().encode('utf-8').decode('unicode_escape').encode('ascii','ignore').encode('utf-8').split(" "))
            for i in p:
                #print i
                #print p['entities']['hashtags']
                for j in p['entities']['hashtags']:
                     hashlist.append(j['text'].encode('utf-8').decode('unicode_escape').encode('ascii','ignore').encode('utf-8'))
      
                        
    
                        
                    
        #print hashlist
            
        for term in hashlist:
            
                #for word in term:
                #print word
            #for key in hashlist:
                
                #print (str(key) + str(term) + scores(key))
        #     term = term.split(" ")
        #     words.append(term)
        #     print(words)
                #dictionary = dict.fromkeys(words,0)
                #print dictionary.items()

                            #value = value + hashtags[key]
                    if (term not in hashtags.keys()):
                        hashtags[term] = hashlist.count(term)
                    
                         
                                
                    
        for (term , value) in sorted(hashtags.iteritems(), key = lambda x:-x[1])[:10]:
            print str(term) + ' ' + str(value)
                                
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
            
    #print hashtags.items()

            
            
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
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
    
    #lines(sent_file)
    #lines(tweet_file)
    datadictionary(tweet_file)

if __name__ == '__main__':
    main()
