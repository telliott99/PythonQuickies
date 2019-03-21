#! /bin/bash

rm tmp/*
last=$(python selection.py $1)
echo $last
convert -delay 75 -loop 3 tmp/*.png -delay 250 $last animated.gif
open -a Safari animated.gif
