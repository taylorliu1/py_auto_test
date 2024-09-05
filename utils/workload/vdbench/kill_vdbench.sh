#!/bin/bash
for pid in $( ps -ef | grep vdbench | grep -v grep | awk '{print $2}' | tr '\n' ' ');
do
  if [[ -n $pid ]]; then
    echo ${pid}
    kill -9 $pid 2>/dev/null
  fi
  #kill ${i} 2>/dev/nul
  sleep 2
done
#ps -ef | grep vdbench | grep -v grep | awk '{print $2}' | tr '\n' ' '|xargs kill -9
