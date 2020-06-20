#!/bin/bash
ls *.ts | sort -V > mylist.txt;
{ xargs cat < mylist.txt ; } > all.ts;
ffmpeg -i all.ts -acodec copy -vcodec copy all.mp4;
