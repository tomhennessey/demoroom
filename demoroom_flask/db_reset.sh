#!/bin/bash

if [ "$#" != 1 ]; then
	echo "Run script with c to clean or i to init"
	exit 0
fi

if [ $1 == "i" ]; then
	if [ -x "$(command -v pip3)" ]; then
		pip3 install -r requirements.txt
	elif [ -x "$(command -v pip)" ]; then
		pip install -r requirements.txt
	fi
	flask db init
	flask db migrate
	flask db upgrade
	if [ -x "$(command -v python3)" ]; then
		python3 database.py
	elif [ -x "$(command -v python)" ]; then
		python database.py
	fi
	exit 0

elif [ $1 == "c" ]; then
	DB=./app.db
	MIG=./migrations/
	if test -f "$DB"; then
		rm $DB
	fi
	if test -d "$MIG"; then
		rm -rf $MIG
	fi
	exit 0
fi
