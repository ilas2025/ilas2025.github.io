#!/bin/bash

wget --output-file="get-minis-1.log" "https://docs.google.com/spreadsheets/d/1IQkcuu7cRXA5wlwMJspwSSfZNHIdXoapZBKufdFIayc/export?format=csv&gid=0" -O "minis.csv"
wget --output-file="get-minis-2.log" "https://docs.google.com/spreadsheets/d/1IQkcuu7cRXA5wlwMJspwSSfZNHIdXoapZBKufdFIayc/export?format=csv&gid=1179422031" -O "mini-speakers.csv"

python mini-json.py
