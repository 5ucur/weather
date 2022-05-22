#!/bin/bash

if [ $# -eq 0 ]
then
    echo "Use argument [[local|online]|[L|O]]"
elif [ $1 == "L" ] || [ $1 == "local" ]
then
    python3 server.py $1
elif [ $1 == "O" ] || [ $1 == "online" ]
then
    bash -c 'ngrok http 12345 &'
    sleep 2
    curl --silent http://127.0.0.1:4040/api/tunnels | jq '.tunnels[0].public_url' > ~/Desktop/weather
    curl --silent http://127.0.0.1:4042/api/tunnels | jq '.tunnels[0].public_url' >> ~/Desktop/weather
    sleep 2
    python3 server.py $1
else
    echo "Use argument [[local|online]|[L|O]]"
fi
