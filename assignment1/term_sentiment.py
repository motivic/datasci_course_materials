import sys
import json
#import string
from collections import defaultdict
import re

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    pos_cnt = defaultdict(lambda: 0.1)
    neg_cnt = defaultdict(lambda: 0.1)

    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    for line in tweet_file:
        tweet = json.loads(line)
        if u'text' in tweet:
            text = tweet[u'text'].encode('utf-8')
            #exclude = set(string.punctuation)
            #words = [''.join(ch for ch in w.lower() if ch not in exclude) for w in text.strip().split()]
            words = [w.lower() for w in text.strip().split()]
            score = sum((scores[w] if w in scores else 0) for w in words)
            for w in words:
                if w in scores:
                    continue
                r = re.match("\w+", w)
                if r:
                    word = r.group(0)
                #print(w)
                if score > 0:
                    pos_cnt[word] += 1
                elif score < 0:
                    neg_cnt[word] += 1

    for w in set.union(set(pos_cnt.keys()), set(neg_cnt.keys())):
        print "%s %f" % (w, pos_cnt[w]/neg_cnt[w])

if __name__ == '__main__':
    main()
