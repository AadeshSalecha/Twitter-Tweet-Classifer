import mmap

def mapcount(filename):
  f = open(filename, "r+")
  buf = mmap.mmap(f.fileno(), 0)
  lines = 0
  readline = buf.readline
  while readline():
    lines += 1
  return lines

def merge():
with open("./Output/en_geo_2020-03-06.json_categorized.csv", "w") as outptr:
  for num in range(1, 14):
    with open("./Split_03_06/split_" + str(num) + ".json_categorized.csv", "r") as inptr:
      outptr.write(inptr.read())

def main():
  max_lines = mapcount("./Data/en_geo_2020-03-06.json")
  max_split = 13
  each = int(max_lines / max_split)
  with open("./Data/en_geo_2020-03-06.json", "r") as inptr:
    for num in range(1, max_split):
      print(num)
      with open("./Split_03_06/split_" + str(num) + ".json", "w") as outptr:
        for i in range(each):
          outptr.write(inptr.readline())
  
    with open("./Split_03_06/split_" + str(max_split) + ".json", "w") as outptr:
      while True:
        line = inptr.readline()
        if not line:
          break
        outptr.write(line)

if __name__ == '__main__':
	main()