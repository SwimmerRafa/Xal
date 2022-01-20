#!/bin/bash
eval "$(conda shell.bash hook)"
conda activate testserver
gunicorn -w=1 -b 0.0.0.0:8080 run:app