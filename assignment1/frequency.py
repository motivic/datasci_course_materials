import sys
import json
import string
from collections import defaultdict

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])

    total = 0
    freq = defaultdict(int)
    for line in tweet_file:
        tweet = json.loads(line)
        if u'text' in tweet:
            exclude = set(string.punctuation)
            words = [w.encode('utf-8') for w in tweet[u'text'].strip().split()]
            words = [''.join(ch for ch in w if ch not in exclude) for w in words]
            total += len(words)
            for w in words:
                freq[w] += 1

    for w, f in freq.iteritems():
        print "%s %f" % (w, f/total)

if __name__ == '__main__':
    main()
