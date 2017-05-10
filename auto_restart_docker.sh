#!/bin/bash
if [ ! "$(docker ps -q -f name=graphite)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=graphite)" ]; then
        # cleanup
        echo "DOCKER CONTAINER NOT RUNNING..CLEANING UP"
        docker rm graphite
    fi
    # run your container
    docker run --name graphite -v `pwd`/graphite/data \
               -e SECRET_KEY='nanopower' -e STATSD_IPV6=0 \
               -p 80:80 \
               -p 3000:3000 \
               -p 2003:2003 \
               -p 2004:2004 \
               -p 7002:7002 \
               -p 8125:8125/udp \
               -p 8126:8126 \
               --restart unless-stopped \
               -d nanoleaf/graphite-grafana-ec2
fi