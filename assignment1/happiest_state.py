import json
import sys
import pdb

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

def build_sent(sent_file):
  sent_dic = {}
  for line in sent_file:
    term, score  = line.split("\t")
    sent_dic[term] = int(score)
  return sent_dic

def build_state():
  state_dic = {}
  for state in states.iterkeys():
    state_dic[state] = 0
  return state_dic 

def cal_score(line, sent_dic, state_dic):
  score = 0
  for (k, v) in line.iteritems():
    if k == "text":
      encoded_text = v.encode('utf-8')
      words = encoded_text.split(" ")
      for word in words:
        if word in sent_dic:
          score += sent_dic[word]
    if k == "place" and type(v) is dict:
      for (k2, v2) in v.iteritems():
        if k2 == "full_name":
          places = v2.split(", ")
          for place in places:
            if place in state_dic:
              state_dic[place] += score

def score_tweets(tweet_file, sent_dic, state_dic):
  for line in tweet_file:
    decoded_line = json.loads(line)
    cal_score(decoded_line, sent_dic, state_dic)
  happiest_state = ''
  highest_score = 0
  for (k, v) in state_dic.iteritems():
    if v > highest_score:
      highest_score = v
      happiest_state = k
  print happiest_state 

def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])
  sent_dic = build_sent(sent_file)
  state_dic = build_state()
  score_tweets(tweet_file, sent_dic, state_dic)

if __name__ == '__main__':
  main()
