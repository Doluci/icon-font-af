#!/bin/bash

mv icons.fa.css icons.fa.css.bak
python font-update.py icons.fa.css.bak ../Font-Awesome/fonts fontawesome-webfont.woff fontawesome-webfont.ttf > icons.fa.css
