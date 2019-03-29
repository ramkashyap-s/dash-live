# Live-Dash
Stream processing pipeline for analyzing live chat data from Twitch IRC

## Architecture
![Alt text](src/docs/pipeline.png "Architecture")

Live-Dash runs on the AWS cloud, using the following cluster configurations:

- 1 t2.large RDS PostgreSQL instance
- 3 m4.large EC2 instances for Kafka brokers and Kafka producers
- 3 m4.large EC2 instances for Spark 
- 1 t2.medium Web-Server

## Setup
- I used pegasus to spin up my clusters. You might want to read [the following](src/README.md)
to setup the enviornment on your localhost to test this out. 
