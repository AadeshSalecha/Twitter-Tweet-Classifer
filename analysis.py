import json
import csv
import ast

def reformat(usr_loc):
  # Sample - "{'country_code': 'us', 'state': 'Indiana'}"
  country = usr_loc.get("country_code", "None")
  state = usr_loc.get("state", "None")
  return (country, state)

def convert_line_to_dict(line): 
  return ast.literal_eval(line.lstrip().rstrip())
  # d = {}
  # id_str = "\'ID\': "
  # id_end_indx = line.find(id_str) + len(id_str)
  # label_str = "\'label\': "
  # label_end_indx = line.find(label_str) + len(label_str)
  # text_str = "\'text\': "
  # text_end_indx = line.find(text_str) + len(text_str)

  # d['ID'] = line[id_end_indx: label_end_indx - len(label_str)]
  # d['label'] = line[label_end_indx: text_end_indx - len(text_str)]
  # d['text'] = line[text_end_indx: -2]

  # return d
  
def main():
  all_files = ['en_geo_2020-04-03-029.json', 'en_geo_2020-03-06.json', 'en_geo_2020-02-20.json', 'en_geo_2020-03-31-027.json', 'en_geo_2020-04-19-043.json', 'en_geo_2020-03-02.json', 'en_geo_2020-02-17.json', 'en_geo_2020-03-18.json', 'en_geo_2020-03-17-034.json', 'en_geo_2020-02-07.json', 'en_geo_2020-04-25.json', 'en_geo_2020-03-26-049.json', 'en_geo_2020-04-16-039.json', 'en_geo_2020-02-10.json', 'en_geo_2020-04-04.json', 'en_geo_2020-02-18.json', 'en_geo_2020-02-02.json', 'en_geo_2020-02-25.json', 'en_geo_2020-04-24-053.json', 'en_geo_2020-03-28-025.json', 'en_geo_2020-03-24.json', 'en_geo_2020-04-06-036.json', 'en_geo_2020-03-23-023.json', 'en_geo_2020-03-15.json', 'en_geo_2020-02-04.json', 'en_geo_2020-03-08.json', 'en_geo_2020-03-22.json', 'en_geo_2020-02-26.json', 'en_geo_2020-04-21-050.json', 'en_geo_2020-03-20.json', 'en_geo_2020-03-05.json', 'en_geo_2020-03-13-024.json', 'en_geo_2020-02-13.json', 'en_geo_2020-03-19.json', 'en_geo_2020-02-27.json', 'en_geo_2020-04-15-055.json', 'en_geo_2020-04-20-057.json', 'en_geo_2020-04-29.json', 'en_geo_2020-03-10.json', 'en_geo_2020-04-05-030.json', 'en_geo_2020-02-21.json', 'en_geo_2020-03-01.json', 'en_geo_2020-02-12.json', 'en_geo_2020-02-23.json', 'en_geo_2020-03-12-022.json', 'en_geo_2020-04-28.json', 'en_geo_2020-04-17-042.json', 'en_geo_2020-04-11-031.json', 'en_geo_2020-03-03.json', 'en_geo_2020-04-27.json', 'en_geo_2020-03-27-020.json', 'en_geo_2020-02-28.json', 'en_geo_2020-04-14-035.json', 'en_geo_2020-02-06.json', 'en_geo_2020-04-01-046.json', 'en_geo_2020-03-04.json', 'en_geo_2020-02-16.json', 'en_geo_2020-04-07-044.json', 'en_geo_2020-04-02-054.json', 'en_geo_2020-04-09-033.json', 'en_geo_2020-03-07.json', 'en_geo_2020-03-21.json', 'en_geo_2020-02-05.json', 'en_geo_2020-04-13-041.json', 'en_geo_2020-04-26-052.json', 'en_geo_2020-02-11.json', 'en_geo_2020-02-29.json', 'en_geo_2020-03-11.json', 'en_geo_2020-04-10-058.json', 'en_geo_2020-02-01.json', 'en_geo_2020-02-08.json', 'en_geo_2020-04-12-028.json', 'en_geo_2020-03-29-032.json', 'en_geo_2020-03-25.json', 'en_geo_2020-03-16.json', 'en_geo_2020-02-03.json', 'en_geo_2020-04-30.json', 'en_geo_2020-04-08-040.json', 'en_geo_2020-02-09.json', 'en_geo_2020-04-18-038.json', 'en_geo_2020-02-22.json', 'en_geo_2020-04-22-056.json', 'en_geo_2020-02-15.json', 'en_geo_2020-03-09.json', 'en_geo_2020-04-23-048.json', 'en_geo_2020-03-30-045.json', 'en_geo_2020-02-14.json', 'en_geo_2020-02-19.json', 'en_geo_2020-03-14.json', 'en_geo_2020-02-24.json']
  all_files_without_feb = [f for f in all_files if f.find("en_geo_2020-02") == -1]
  all_files_without_feb.sort()

  # not working for these 
  # all_files_without_feb = ['en_geo_2020-03-12-022.json', 'en_geo_2020-03-14.json', 'en_geo_2020-03-15.json', 'en_geo_2020-04-26-052.json']

  for file in all_files_without_feb:
    print(file)
    with open("./Final Data (Standardized 1.75)/" + file + "_standardized.csv", "r") as standardized:
      with open("./Data/" + file, "r") as data:
        with open("./Geolocation/" + file + "_standardized_retweet.csv", "w") as outptr:
          writer = csv.writer(outptr)
          standardized_reader = csv.reader(standardized)
          
          for line in standardized_reader:
            # try:
              tweet = json.loads(data.readline())
              d = convert_line_to_dict(line[0])
              if(d['ID'] != tweet['tweet_id']):
                print(d)
                print("Error")

                line = 1
                skipped = 0
                while (d['ID'] != tweet['tweet_id']):
                  skipped += 1
                  line = data.readline()
                  if (not line):
                    break
                  tweet = json.loads(line)

                print(d['ID'] == tweet['tweet_id'], " now ", str(d["ID"]), " ", str(tweet['tweet_id']), " ", skipped)

              if (d['label'] == "retweet"):            
                writer.writerow(["\'" + str(d['ID']) + "\'", reformat(tweet['user_location'])])
            # except Exception as e:
            #   print("Error")
            #   break


  for file in all_files_without_feb:
    print(file)
    with open("./Final Data (Standardized 1.75)/" + file + "_standardized.csv", "r") as standardized:
      with open("./Data/" + file, "r") as data:
        with open("./Geolocation/" + file + "_standardized_source.csv", "w") as outptr:
          writer = csv.writer(outptr)
          standardized_reader = csv.reader(standardized)
          
          for line in standardized_reader:
            # try:
              tweet = json.loads(data.readline())
              d = convert_line_to_dict(line[0])
              if(d['ID'] != tweet['tweet_id']):
                print(d)
                print("Error")

                line = 1
                skipped = 0
                while (d['ID'] != tweet['tweet_id']):
                  skipped += 1
                  line = data.readline()
                  if (not line):
                    break
                  tweet = json.loads(line)

                print(d['ID'] == tweet['tweet_id'], " now ", str(d["ID"]), " ", str(tweet['tweet_id']), " ", skipped)

              if (d['label'] == "source"):            
                writer.writerow(["\'" + str(d['ID']) + "\'", reformat(tweet['user_location'])])
            # except Exception as e:
            #   print("Error")
            #   break


if __name__ == "__main__":
  main()