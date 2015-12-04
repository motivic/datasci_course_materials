import sys
import json
import string


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    for line in tweet_file:
        tweet = json.loads(line)
        if u'text' in tweet:
            text = tweet[u'text'].encode('utf-8')
            exclude = set(string.punctuation)
            words = [''.join(ch for ch in w.lower() if ch not in exclude) for w in text.strip().split()]
            score = sum((scores[w] if w in scores else 0) for w in words )
            #print(words)
            print(score)

if __name__ == '__main__':
    main()
