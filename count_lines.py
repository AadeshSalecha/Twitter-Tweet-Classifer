import mmap
import sys
from os import listdir
from os.path import isfile, join

def simplecount(filename):
  lines = 0
  for line in open(filename):
      lines += 1
  return lines

def mapcount(filename):
    f = open(filename, "r+")
    buf = mmap.mmap(f.fileno(), 0)
    lines = 0
    readline = buf.readline
    while readline():
      lines += 1
    return lines

def main():
  input_dir = "./" + sys.argv[1]
  onlyfiles_p = [f for f in listdir(input_dir) if isfile(join(input_dir, f))]
  onlyfiles = []
  # for s in onlyfiles_p:
  #   if(s.find("en_geo_2020-02") == -1 and s.find("en_geo_2020-03") == -1):
  #     onlyfiles.append(s)
  onlyfiles = onlyfiles_p

  processed = 0
  for file in onlyfiles:
    processed += mapcount(input_dir + "/" + file)
    print("Total processed = ", processed)
  print("Total processed = ", processed, " Total # files = ", len(onlyfiles))

if __name__ == '__main__':
  all_files = ['en_geo_2020-04-03-029.json', 'en_geo_2020-03-06.json', 'en_geo_2020-02-20.json', 'en_geo_2020-03-31-027.json', 'en_geo_2020-04-19-043.json', 'en_geo_2020-03-02.json', 'en_geo_2020-02-17.json', 'en_geo_2020-03-18.json', 'en_geo_2020-03-17-034.json', 'en_geo_2020-02-07.json', 'en_geo_2020-04-25.json', 'en_geo_2020-03-26-049.json', 'en_geo_2020-04-16-039.json', 'en_geo_2020-02-10.json', 'en_geo_2020-04-04.json', 'en_geo_2020-02-18.json', 'en_geo_2020-02-02.json', 'en_geo_2020-02-25.json', 'en_geo_2020-04-24-053.json', 'en_geo_2020-03-28-025.json', 'en_geo_2020-03-24.json', 'en_geo_2020-04-06-036.json', 'en_geo_2020-03-23-023.json', 'en_geo_2020-03-15.json', 'en_geo_2020-02-04.json', 'en_geo_2020-03-08.json', 'en_geo_2020-03-22.json', 'en_geo_2020-02-26.json', 'sample.json', 'en_geo_2020-04-21-050.json', 'en_geo_2020-03-20.json', 'en_geo_2020-03-05.json', 'en_geo_2020-03-13-024.json', 'en_geo_2020-02-13.json', 'en_geo_2020-03-19.json', 'en_geo_2020-02-27.json', 'en_geo_2020-04-15-055.json', 'en_geo_2020-04-20-057.json', 'en_geo_2020-04-29.json', 'en_geo_2020-03-10.json', 'en_geo_2020-04-05-030.json', 'en_geo_2020-02-21.json', 'en_geo_2020-03-01.json', 'en_geo_2020-02-12.json', 'en_geo_2020-02-23.json', 'en_geo_2020-03-12-022.json', 'en_geo_2020-04-28.json', 'en_geo_2020-04-17-042.json', 'en_geo_2020-04-11-031.json', 'en_geo_2020-03-03.json', 'en_geo_2020-04-27.json', 'en_geo_2020-03-27-020.json', 'en_geo_2020-02-28.json', 'en_geo_2020-04-14-035.json', 'en_geo_2020-02-06.json', 'en_geo_2020-04-01-046.json', 'en_geo_2020-03-04.json', 'en_geo_2020-02-16.json', 'en_geo_2020-04-07-044.json', 'en_geo_2020-04-02-054.json', 'en_geo_2020-04-09-033.json', 'en_geo_2020-03-07.json', 'en_geo_2020-03-21.json', 'en_geo_2020-02-05.json', 'en_geo_2020-04-13-041.json', 'en_geo_2020-04-26-052.json', 'en_geo_2020-02-11.json', 'en_geo_2020-02-29.json', 'en_geo_2020-03-11.json', 'en_geo_2020-04-10-058.json', 'en_geo_2020-02-01.json', 'en_geo_2020-02-08.json', 'en_geo_2020-04-12-028.json', 'en_geo_2020-03-29-032.json', 'en_geo_2020-03-25.json', 'en_geo_2020-03-16.json', 'en_geo_2020-02-03.json', 'en_geo_2020-04-30.json', 'en_geo_2020-04-08-040.json', 'en_geo_2020-02-09.json', 'en_geo_2020-04-18-038.json', 'en_geo_2020-02-22.json', 'en_geo_2020-04-22-056.json', 'en_geo_2020-02-15.json', 'en_geo_2020-03-09.json', 'en_geo_2020-04-23-048.json', 'en_geo_2020-03-30-045.json', 'en_geo_2020-02-14.json', 'en_geo_2020-02-19.json', 'en_geo_2020-03-14.json', 'en_geo_2020-02-24.json']
  all_files_without_feb = [f for f in all_files if f.find("en_geo_2020-02") == -1]
  all_files_without_feb.sort()

  if(str(sys.argv[1]).lstrip().rstrip() == "-a"):
    print("here")
    for i in range(len(all_files_without_feb)):
      total = mapcount("./Data/" + all_files_without_feb[i])
      processed = mapcount("./Output/" + all_files_without_feb[i] + "_categorized.csv")
      print(all_files_without_feb[i], ", ", processed, " / ", total, " = ", round(processed / total * 100.00, 2))
  else:
    total = mapcount("./Data/" + all_files_without_feb[int(sys.argv[2]) - 1])
    processed = mapcount("./Output/" + all_files_without_feb[int(sys.argv[2]) - 1] + "_categorized.csv")
    print(all_files_without_feb[int(sys.argv[2]) - 1], ", ", processed, " / ", total, " = ", round(processed / total * 100.00, 2))