#!/usr/bin/env python3

import sys
import csv
import argparse
import boto3


def get_args():
  parser = argparse.ArgumentParser(description='Process command line values.')

  parser.add_argument('--read-file', dest='readfile', required=True, help='file to read in')
  parser.add_argument('--write-file', dest='writefile', required=True, help='file to write to')
  parser.add_argument('--access-key', dest='accesskey', required=True, help='AWS access key')
  parser.add_argument('--secret-key', dest='secretkey', required=True, help='AWS secret key')
  parser.add_argument('--upload-bucket', dest='uploadbucket', required=True, help='bucket to upload file to in S3')
  parser.add_argument('--file-path', dest='filepath', required=True, help='path of where to load the file')
  parser.add_argument('--aws-service', dest='awsservice', required=False, default='s3', help='service to use in AWS')
  
  args = parser.parse_args()
  return args


def upload_to_s3(args):
  client = boto3.client(args.awsservice, aws_access_key_id=args.accesskey, aws_secret_access_key=args.secretkey)
  path = args.filepath + '/' + args.writefile
  client.upload_file(args.writefile, args.uploadbucket, path)


def main():
  args = get_args()
  read_csv(args)
  write_csv(args)
  upload_to_s3(args)
  

def read_csv(args):
  print("Reading of CSV")

  with open(args.readfile, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
      print(', '.join(row))

  print()


def write_csv(args):
  list = generate_list()

  print("Write of CSV")

  with open(args.writefile, 'w') as csvfile:
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
