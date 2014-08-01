import json
import sys
import pdb

def count_word(line, word_cnt):
  total = 0
  for (k, v) in line.iteritems():
    if k == "text":
      encoded_text = v.encode('utf-8')
      fixed_text = encoded_text.replace('\n', '')
      words = fixed_text.split(" ")
      for word in words:
        total += 1
        if word in word_cnt:
          word_cnt[word] += 1
        else:
          word_cnt[word] = 1
      return total
    if type(v) is dict:
      total = count_word(v, word_cnt)
  return total

def count_tweets(tweet_file, word_cnt):
  total_cnt = 0
  for line in tweet_file:
    decoded_line = json.loads(line)
    total_cnt += count_word(decoded_line, word_cnt)
  return total_cnt

def print_frequency(word_cnt, total_cnt):
  for (k, v) in word_cnt.iteritems():
    f = v / float(total_cnt)
    print '{} {}'.format(k, f)

def main():
  tweet_file = open(sys.argv[1])
  word_cnt = {}
  total_cnt = count_tweets(tweet_file, word_cnt)
  print_frequency(word_cnt, total_cnt)

if __name__ == '__main__':
  main()
