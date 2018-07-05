#!/bin/bash

LEVEL=$(xbacklight -get | xargs printf "%.f")

level=`lux -G`

case "$1" in
  "up")
    [[ "$LEVEL" -eq 100 ]]
#    xbacklight -inc 5
    lux -a 10%
    ;;
  "down")
#    xbacklight -dec 5
    lux -s 10%
    ;;
esac

LEVEL=$(xbacklight -get | xargs printf "%.f")
# notification
volnoti-show -s /usr/share/pixmaps/volnoti/display-brightness-symbolic.svg $LEVEL
notify-send "${level}"
