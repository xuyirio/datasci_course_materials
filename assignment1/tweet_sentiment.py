import json
import sys
import pdb

def build_sent(sent_file):
  sent_dic = {}
  for line in sent_file:
    term, score  = line.split("\t")
    sent_dic[term] = int(score)
  return sent_dic

def cal_score(line, sent_dic, s):
  score = s
  for (k, v) in line.iteritems():
    if k == "text":
      encoded_text = v.encode('utf-8')
      words = encoded_text.split(" ")
      score = 0
      for word in words:
        if word in sent_dic:
          score = score + sent_dic[word]
    if type(v) is dict:
      score = score + cal_score(v, sent_dic, score)
  return score

def score_tweets(tweet_file, dic):
  for line in tweet_file:
    decoded_line = json.loads(line)
    print cal_score(decoded_line, dic, 0)

def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])
  sent_dic = build_sent(sent_file)
  score_tweets(tweet_file, sent_dic)

if __name__ == '__main__':
  main()
