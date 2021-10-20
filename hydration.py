import random
import ast
import os
from datetime import datetime
import time
import tweepy 
import json
import csv
import sys

import time
import mmap
import random
from collections import defaultdict

# Usage: hydration.py [api_keys_file] [input] [key_no]

api = None
def read_api_keys():
  all_keys = []
  with open(sys.argv[1], "r") as inptr:
    for i in range(75):
      inptr.readline()
      consumer_key=inptr.readline().lstrip("consumer_key=\"").rstrip("\"\n")
      consumer_secret=inptr.readline().lstrip("consumer_secret=\"").rstrip("\"\n")
      access_key=inptr.readline().lstrip("access_key=\"").rstrip("\"\n")
      access_secret=inptr.readline().lstrip("access_secret=\"").rstrip("\"\n")
      inptr.readline()

      all_keys.append([consumer_key, consumer_secret, access_key, access_secret])
  
  return all_keys

def setup_tweepy():
  global api

  api_keys = read_api_keys()
  key_num = int(sys.argv[3]) - 1

  # assign the values accordingly 
  consumer_key=api_keys[key_num][0].lstrip().rstrip()
  consumer_secret=api_keys[key_num][1].lstrip().rstrip()
  access_key=api_keys[key_num][2].lstrip().rstrip()
  access_secret=api_keys[key_num][3].lstrip().rstrip()
  
  # authorization of consumer key and consumer secret 
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    
  # set access to user's access key and access secret  
  auth.set_access_token(access_key, access_secret) 
    
  # calling the api  
  api = tweepy.API(auth, wait_on_rate_limit = True)

# def reformat(data):
#   data = data.split("},")
#   ans = []
#   for i in range(len(data)-1):
#     tweet = data[i]
#     try:
#       tweet = tweet + "}"
#       ans.append(json.loads(tweet))
#     except:
#       print("Error in reformat ", tweet, i, len(data), data[i-1])
#       exit()
#   return ans

def convert_line_to_dict(line): 
  # return ast.literal_eval(ast.literal_eval(line))
  d = {}
  id_str = "\'ID\': "
  id_start = line.find(id_str)
  id_end_indx = id_start + len(id_str)

  label_str = ", \'label\': "
  label_start = line.find(label_str)
  label_end_indx = label_start + len(label_str)

  text_str = ", \'text\': "
  text_start = line.find(text_str)
  text_end_indx = text_start + len(text_str)

  d['ID'] = line[id_end_indx: label_start].lstrip('\'').rstrip('\'')
  d['label'] = line[label_end_indx: text_start].lstrip('\'').rstrip('\'')
  d['text'] = line[text_end_indx: -2].lstrip('\'').rstrip('\'')

  return d

def classify(tweet_id):
  status = None
  global api
  try:
    status = api.get_status(tweet_id) 
  # except tweepy.RateLimitError as e:
  #   print("Rate limit error exceed waiting for 15 mins")
  #   print(datetime.now())
  #   time.sleep(60 * 15)
  #   return ("Rate limit", "")
  except Exception as e:
    if(str(e).find("Could not authenticate you") != -1 or str(e).find("Authentication") != -1 or str(e).find("token") != -1):
      print(str(e))
      exit()
    return {"error": str(e)}

  text = status.text.strip('\n').strip('\r')
  d = status._json
  # print(text)
  if (status.in_reply_to_status_id != None):
    d["label"] = "reply"
  elif (text.find("RT @") != -1 or (hasattr(d, 'retweeted_d'))):
    d["label"] = "retweet"
  else:
    d["label"] = "source"
  return d

# def has_US_location(tweet):
#   # change it to consider only user_location
#   return str(tweet).find("\'us\', \'state\'") != -1

def mapcount(filename):
    f = open(filename, "r+")
    buf = mmap.mmap(f.fileno(), 0)
    lines = 0
    readline = buf.readline
    while readline():
      lines += 1
    return lines

def create_folder_if_doesnt_exit(d):
  isExist = os.path.exists(d)
  if not isExist:
    # Create a new directory because it does not exist 
    os.makedirs(d)

def main():
  print("Started = ", sys.argv)
  file_to_process = sys.argv[2]
  print("Processing = ", file_to_process)
  
  # what percentage of the data to keep
  target = 5.0 / 100

  with open(file_to_process, "r") as inptr:
    all_lines = inptr.readlines()
    random.shuffle(all_lines)
    total = len(all_lines)

  print("Total = ", total)

  setup_tweepy()

  create_folder_if_doesnt_exit("./Output")

  filtered_num = 0
  processed_num = 0
  index = {}
  mode = "w"
  if (os.path.exists("./Output/" + file_to_process + ".csv")):
    with open("./Output/" + file_to_process + ".csv", "r") as inptr:
      lines = 0 #mapcount("./Output/" + file_to_process + "_categorized.csv")
      reader = csv.reader(inptr)
      for row in reader:
        lines += 1
        d = convert_line_to_dict(row[0])
        index[d['ID']] = True

      print("Indexed ", lines, " lines")
      processed_num += lines

      mode = "a"

  with open("./Output/" + file_to_process + ".csv", mode) as outptr:
    writer = csv.writer(outptr) 
    # try:
    for line in all_lines:
      # stop once done
      if(processed_num / total >= target):
        print("Target hit = ", processed_num, " / ", total, " = ", processed_num / total)
        exit()

      id = line.strip('\n')
      print(id)
      # we have already looked at this tweet
      if (id in index):
        continue

      processed_num += 1
      tweet = classify(id)

      # You can remove all_fields from below to avoid excess data storage
      writer.writerow([tweet])

      if(processed_num % 1000 == 0):
        print("Processed: ", processed_num, " Filtered: ", filtered_num)
    # except Exception as e:
    #   print ("Error = ", e)
    #   exit()


if __name__ == '__main__':
  if (len(sys.argv) != 4):
    print("# Usage: hydration.py [api_keys_file] [input] [key_no]")    
    exit()
  main()
