#!/bin/bash

GOLD_PATH="demo/demo.jsonl"
PRED_PATH="demo/demo.jsonl"
python src/eval.py --gold $GOLD_PATH --pred $PRED_PATH --metrics rouge bleu