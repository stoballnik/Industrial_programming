#!/usr/bin/env bash
docker rm  -f $(docker ps -aq)

docker-compose up -d --build

sleep 15

sudo docker exec -d hw1_consumer_1 python3 consumer.py
sudo docker exec -it hw1_producer_1 python3 producer.py

