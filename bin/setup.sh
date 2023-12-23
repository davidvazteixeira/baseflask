#!/bin/bash

case $1 in
  p)
  requirement="requirements/production.txt"
  ;;

  t)
  requirement="requirements/test.txt"
  ;;
  
  d)
  requirement="requirements/development.txt"
  ;;

  *)
  echo - "  "Choose your environment running:
  echo - "    "$ $0 p: production
  echo - "    "$ $0 d: development
  exit
  ;;
esac

if [ "$2" == "--remove" ]; then
  echo - Removing old .env
  rm -rf .env
fi

python3 -m venv .env
source .env/bin/activate

echo - Using $requirement file
pip install -r "$requirement" 

echo - Done
echo
echo "   "Do not forget always to activate your environment:
echo "      "$ source .env/bin/activate
