#!/usr/bin/python

import sys
import config

def main():
  # youtuber = "freeCodeCamp"

  # # a few ways to concatenate strings
  # print("subscribe to " + youtuber)
  # print("subscribe to {}".format(youtuber))
  # print(f"subscribe to {youtuber}")

  # print("Let's play madlibs!")

  # adj1 = input("Enter an Adjective: ")
  # verb1 = input("Next a Verb: ")
  # verb2 = input("Another Verb: ")

  # adj2 = input("Just one more Adjective: ")
  # famous_person = input("Finally a famous Person: ")

  # madlib = f"Today was so {adj1}! I got a lot done because \
  # I love to {verb1}. The best motivation to work hard is to stay hungry, {verb2} and try to stay {adj2} like you are {famous_person} " 

  # print(madlib)

  # print(sys.argv[1])

  for i in range(len(sys.argv)):
    print(sys.argv[i])

  print(type(sys.argv))
  # print(config.arg1, config.arg2)

if __name__ == "__main__":
  main()