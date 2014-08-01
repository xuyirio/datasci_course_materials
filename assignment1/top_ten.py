import json
import sys
import pdb

def count_tag(line, tag_cnt):
  for (k, v) in line.iteritems():
    if k == "entities" and type(v) is dict:
      for (k2, v2) in v.iteritems():
        if k2 == "hashtags" and len(v2) > 0:
          for tag_obj in v2:
            tag = tag_obj[u'text'].encode('utf-8')
            if tag in tag_cnt:
              tag_cnt[tag] += 1
            else:
              tag_cnt[tag] = 1

def count_tweets(tweet_file, tag_cnt):
  for line in tweet_file:
    decoded_line = json.loads(line)
    count_tag(decoded_line, tag_cnt)

def top_ten_tags(tag_cnt):
  sorted_tags = sorted(tag_cnt.items(), key=lambda x: x[1], reverse=True)
  i = 0
  while i < 10:
    print '{} {}'.format(sorted_tags[i][0], sorted_tags[i][1])
    i += 1

def main():
  tweet_file = open(sys.argv[1])
  tag_cnt = {}
  count_tweets(tweet_file, tag_cnt)
  top_ten_tags(tag_cnt)

if __name__ == '__main__':
  main()
