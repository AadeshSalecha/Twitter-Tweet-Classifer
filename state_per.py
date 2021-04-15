import json
import csv
import ast

def reformat(usr_loc):
  # Sample - "{'country_code': 'us', 'state': 'Indiana'}"
  country = usr_loc.get("country_code", "None")
  state = usr_loc.get("state", "None")
  return (country, state)
  
def main():
  files = ["en_geo_2020-03-01.json", "en_geo_2020-03-02.json", "en_geo_2020-03-03.json", "en_geo_2020-03-04.json", "en_geo_2020-03-05.json", "en_geo_2020-03-06.json", "en_geo_2020-03-07.json", "en_geo_2020-03-08.json", "en_geo_2020-03-09.json", "en_geo_2020-03-10.json", "en_geo_2020-03-11.json", "en_geo_2020-03-12-022.json", "en_geo_2020-03-13-024.json", "en_geo_2020-03-14.json", "en_geo_2020-03-15.json", "en_geo_2020-03-16.json", "en_geo_2020-03-17-034.json", "en_geo_2020-03-18.json", "en_geo_2020-03-19.json", "en_geo_2020-03-20.json", "en_geo_2020-03-21.json", "en_geo_2020-03-22.json", "en_geo_2020-03-23-023.json", "en_geo_2020-03-24.json", "en_geo_2020-03-25.json", "en_geo_2020-03-26-049.json", "en_geo_2020-03-27-020.json", "en_geo_2020-03-28-025.json", "en_geo_2020-03-29-032.json", "en_geo_2020-03-30-045.json", "en_geo_2020-03-31-027.json", "en_geo_2020-04-01-046.json", "en_geo_2020-04-02-054.json", "en_geo_2020-04-03-029.json", "en_geo_2020-04-04.json", "en_geo_2020-04-05-030.json", "en_geo_2020-04-06-036.json", "en_geo_2020-04-07-044.json", "en_geo_2020-04-08-040.json", "en_geo_2020-04-09-033.json", "en_geo_2020-04-10-058.json", "en_geo_2020-04-11-031.json", "en_geo_2020-04-12-028.json", "en_geo_2020-04-13-041.json", "en_geo_2020-04-14-035.json", "en_geo_2020-04-15-055.json", "en_geo_2020-04-16-039.json", "en_geo_2020-04-17-042.json", "en_geo_2020-04-18-038.json", "en_geo_2020-04-19-043.json", "en_geo_2020-04-20-057.json", "en_geo_2020-04-21-050.json", "en_geo_2020-04-22-056.json", "en_geo_2020-04-23-048.json", "en_geo_2020-04-24-053.json", "en_geo_2020-04-25.json"]

  banned_states = ["None", "Puerto Rico", "American Samoa", "Northern Mariana Islands", "United States Virgin Islands", "Guam"]
  global_count = 0
  for file in files:
    with_valid_state = 0
    us = 0
    with open("./Data/" + file, "r") as data:
      line = data.readline()
      
      while (line):
        tweet = json.loads(line)            
        (country, state) = reformat(tweet['user_location'])

        if(country == "us" and state not in banned_states):
          with_valid_state += 1
          global_count += 1
        if(country == "us"):
          us += 1

        line = data.readline()
    print(file, " ", with_valid_state, " " , us)
  print(global_count, " in total")


if __name__ == "__main__":
  main()