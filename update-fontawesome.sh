#!/bin/bash

python font-update.py icons.fa.css ../Font-Awesome/fonts fontawesome-webfont.woff fontawesome-webfont.ttf > t.css
mv t.css icons.fa.css
