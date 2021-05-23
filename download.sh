#!/usr/bin/env bash

SESSION_WITH_VALUE="session="$AOC_SESSION
curl https://adventofcode.com/$1/day/$2/input --cookie $SESSION_WITH_VALUE > input.txt
