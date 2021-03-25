import pandas as pd
import ast

def convert_line_to_dict(line): 
  return ast.literal_eval(line)

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


def read_file(file_name):
  d = []
  with open(file_name, "r") as inptr:
    for line in inptr:
      d.append(convert_line_to_dict(line))
  
  print(d)

if __name__ == "__main__":
  data = "./Output/sample.json_categorized.csv"
  google_data = [['{\'ID\': \'1240511872421396482\', \'label\': "[{\'code\': 144, \'message\': \'No status found with that ID.\'}]", \'text\': \'\'}'], ['{\'ID\': \'1240511872828235776\', \'label\': \'retweet\', \'text\': \'RT @Justice_4Vizag: #Paracetamol is the first line medicine to cure #Coronavirus , No evidence on other drugs " : Doctor At Landon School O…\'}'], ["{'ID': '1240511886082420736', 'label': 'Not in US', 'text': ''}"], ["{'ID': '1240511889286684672', 'label': 'Not in US', 'text': ''}"], ["{'ID': '1240511893787365378', 'label': 'Not in US', 'text': ''}"]]

  # data = read_file(file_name)
  # str1 = """[['{\'ID\': \'1240511872421396482\', \'label\': "[{\'code\': 144, \'message\': \'No status found with that ID.\'}]", \'text\': \'\'}'], ['{\'ID\': \'1240511872828235776\', \'label\': \'retweet\', \'text\': \'RT @Justice_4Vizag: #Paracetamol is the first line medicine to cure #Coronavirus , No evidence on other drugs " : Doctor At Landon School O…\'}'], ["{'ID': '1240511886082420736', 'label': 'Not in US', 'text': ''}"], ["{'ID': '1240511889286684672', 'label': 'Not in US', 'text': ''}"], ["{'ID': '1240511893787365378', 'label': 'Not in US', 'text': ''}"]]"""
  # d = convert_line_to_dict(str1)
  for item in google_data:
    print(item)
    print(convert_line_to_dict(item[0]))
