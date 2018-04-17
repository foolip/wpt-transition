#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

# virtualenv initialization
if [[ ! -f "env/bin/activate" ]]; then
    virtualenv -p python3 --no-site-packages env
fi
set +u
source env/bin/activate
set -u
pip install -U -r requirements.txt

python invite.py
