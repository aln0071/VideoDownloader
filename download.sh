#!/bin/bash
wget -i urls.txt && speaker-test -t sine -f 1000 -l 1
