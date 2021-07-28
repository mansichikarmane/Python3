import sys
import csv


def main():
  read_csv()
  write_csv()
  

def read_csv():
  print("Reading of CSV")

  with open(sys.argv[1], newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
      print(', '.join(row))

  print()


def write_csv():
  list = generate_list()

  print("Write of CSV")

  with open(sys.argv[2], 'w') as csvfile:
      writer = csv.writer(csvfile)
      
      for row in list:
        writer.writerow(row)
  
  print()


def generate_list():
  print("Generating List")

  list1 = []
  list1.append('testA')

  for i in range(5):
    list1.append(i) 

  list2 = []
  list2.append('testB')

  for i in range(5):
    list2.append(i)
  
  list3 = []
  list3.append('testC')

  for i in range(5):
    list3.append(i)


  list = zip(list1, list2, list3)
  print(list)
  print()

  return list


if __name__ == "__main__":
  main()
