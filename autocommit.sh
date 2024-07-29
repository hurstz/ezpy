#!/bin/bash

TIMESTAMP=$(date -u +"%Y%m%dT%H%M%SZ")
DIR="$(dirname "$(realpath "$0")")"

cd "$DIR"

read -p "Add, commit, and push all changes now? (y/n): " response

if [[ "$response" == "y" || "$response" == "Y" ]]; then
    git add .
    git commit -m "$TIMESTAMP"
    git push
else
    echo "OK."
fi

cd -
