import json
import sys
import pdb

def build_sent(sent_file):
  sent_dic = {}
  for line in sent_file:
    term, score  = line.split("\t")
    sent_dic[term] = int(score)
  return sent_dic

def cal_score(line, sent_dic, term_dic):
  for (k, v) in line.iteritems():
    if k == "text":
      encoded_text = v.encode('utf-8')
      words = encoded_text.split(" ")
      score = 0
      for word in words:
        if word in sent_dic:
          score = score + sent_dic[word]
      for word in words:
        if word not in sent_dic:
          if word not in term_dic:
            term_dic[word] = score
          else:
            s = term_dic[word] + score
            term_dic[word] = s
    if type(v) is dict:
      cal_score(v, sent_dic, term_dic)

def score_tweets(tweet_file, sent_dic, term_dic):
  tweet_cnt = 0
  for line in tweet_file:
    tweet_cnt += 1
    decoded_line = json.loads(line)
    cal_score(decoded_line, sent_dic, term_dic)
  return tweet_cnt

def print_term_sent(cnt, term_dic):
  for (k, v) in term_dic.iteritems():
    if v != 0:
      s = v/float(cnt)
      print '{} {}'.format(k, v)

def lines(fp):
  print str(len(fp.readlines()))

def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])
#  lines(sent_file)
#  lines(tweet_file)
  sent_dic = build_sent(sent_file)
  term_dic = {}
  cnt = score_tweets(tweet_file, sent_dic, term_dic)
  print_term_sent(cnt, term_dic)

if __name__ == '__main__':
  main()
