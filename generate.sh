#!/bin/bash

for value in {1..15}
do
    python bingo.py > boards/output$value.html
done