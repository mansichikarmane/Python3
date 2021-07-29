#!/bin/bash

echo ''

echo start bash script

read -p 'Please enter your name: ' ans

if [ $ans == 'Mansi' ]
then
  echo hello world, my name is $ans
else  
  echo hello world, your name is $ans
fi 

echo '' 
