import sys
import json
import string
import re

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
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
        'MS': 'Mississippi',
        'MT': 'Montana',
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
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
	}

    states_regex = '|'.join([k for k in states]+[states[k] for k in states])

    happiness = {}
    num_tweets = {}
    for state in states.keys():
        happiness[state] = 0
        num_tweets[state] = 0

    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    for line in tweet_file:
        tweet = json.loads(line)
        if u'text' in tweet:
            exclude = set(string.punctuation)
            words = [w.encode('utf-8').lower() for w in tweet[u'text'].strip().split()]
            words = [''.join(ch for ch in w if ch not in exclude) for w in words]
            score = sum((scores[w] if w in scores else 0) for w in words )
        if u'user' in tweet:
            if u'location' in tweet[u'user']:
                if tweet[u'user'][u'location']:
                    r = re.search(states_regex, tweet[u'user'][u'location'])
                    if r:
                        state = r.group(0)
                        if state in states.keys():
                            happiness[state] += score
                            num_tweets[state] += 1
                        elif state in states.values():
                            for k, v in states:
                                if v == states:
                                    happiness[k] += score
                                    num_tweets[k] += 1

    h = 0
    happiest = ""
    for s, sc in happiness.iteritems():
        if num_tweets[s] > 0 and float(sc)/num_tweets[s] > h:
            h = sc/num_tweets[s]
            happiest = s

    print(happiest)


if __name__ == '__main__':
    main()
