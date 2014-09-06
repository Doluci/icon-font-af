#!/bin/bash

python font-update.py icons.typcn.css ../typicons.font/src/font typicons.woff typicons.ttf > t.css
mv t.css icons.typcn.css
