# SDUcs Data Structure and Algorithm QA System

## data process
run geneCql.py we create the neo4j database

## train_data
we make train data as json structure

run train_dataprocess.py
## train
we use bert checkpoint and idcnn with multi-loss layer by keras

run train/run_train.sh

## use model
run deploy/run_deploy.sh
***first run***

we can get data by api
**127.0.0.1:2020**

## predict

use prefromgraph.py to do it

## front
you are supposed to modify static/js/main.js to modify your ip adress
***second run***

## backend

run server.py to find your work in ***youadress:5000***
