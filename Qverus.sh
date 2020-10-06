#!/bin/bash
read -p "masukan alamat dompet anda ( contoh : RRc2K2tNiSJxUyuyp1eig6mpN5Kn4McY8k ) >> " dompet;
while [ true ];
do
  clear
  python3 kontrolVerus.py $dompet
  sleep 5
done