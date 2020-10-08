#!/bin/bash

iconv -c -f utf8 -t ascii blogs/$1 > newblogs/$1
sed -i ""  "s/&nbsp;/ /g" newblogs/$1
sed -i ""  "s/&/and/g" newblogs/$1
