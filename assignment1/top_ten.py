import sys
import json
from collections import defaultdict
import operator

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])

    freq = defaultdict(int)
    for line in tweet_file:
        tweet = json.loads(line)
        if u'entities' in tweet:
            #print(tweet[u'entities'])
            if u'hashtags' in tweet[u'entities']:
                #print tweet[u'entities'][u'hashtags']
                for hashtag in tweet[u'entities'][u'hashtags']:
                    #print(hashtag)
                    freq[hashtag["text"]] += 1

    sorted_freq = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)[:10]
    # print(sorted_freq)
    for h, c in sorted_freq:
        print "%s %d" % (h, c)

if __name__ == '__main__':
    main()
