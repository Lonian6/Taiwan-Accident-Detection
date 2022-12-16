#!/bin/bash

cat $1 | awk -F "," '{
    if(NR!=1){
        printf("%s \n", $5)
    }
}' | xargs yt-dlp --format "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]" -N 10 -P $2
