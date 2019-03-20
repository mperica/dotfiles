#!/bin/bash

APP=light
LEVEL=$(light | xargs printf "%.f")
#LEVEL=$(xbacklight -get | xargs printf "%.f")

case "$1" in
  "up")
    [[ "$LEVEL" -eq 100 ]]
#    xbacklight -inc 5
#    lux -a 10%
		light -A 5
    ;;
  "down")
#    xbacklight -dec 5
#    lux -s 10%
		light -U 5
    ;;
esac


# notification
volnoti-show -s /usr/share/pixmaps/volnoti/display-brightness-symbolic.svg $LEVEL
notify-send "${level}"
