#!/usr/bin/python

def check_anagrams(s1, s2):

    if(sorted(s1.lower()) == sorted(s2.lower())):
        print(s1 + " and " + s2 + " are anagrams.")
    else:
        print(s1 + " and " + s2 + " aren't anagrams.")        


s1 = "listen"
s2 = "sileNt"

s3 = "aaaaa"
s4 = "bbbbb"

check_anagrams(s1, s2)
check_anagrams(s3, s4)
