# -*- coding: utf-8 -*-

import subprocess

import os
import os.path

from i3pystatus import Status, IntervalModule

#from i3pystatus.mail import imap

#from i3pystatus.updates import pacman, cower

class RestartReminder(IntervalModule):
    settings = required = ()

    def run(self):
        if os.path.exists("/lib/modules/" + os.uname().release):
            self.output = None
        else:
            self.output = {
                "full_text": ": ",
                "color": "#FF1919",
            }

#status = Status(standalone=True)

status = Status(
    logfile='/tmp/i3pystatus_${USER}.log',
        )

status.register("text",
    text="",
    color="#222222")

status.register("clock",
    format=": %I:%M:%S %p",
    interval=5,
    on_leftclick="/usr/bin/gsimplecal",)

status.register("clock",
    format=": %a-%d-%b",
    interval=600,
    on_leftclick="/usr/bin/gsimplecal",)

status.register("text",
    text="|",
    color="#222222")

status.register("disk",
    path="/home",
    format="{percentage_used:.1f}%",
    on_leftclick="termite --geometry=1200x700 --title=glances -e 'glances -1'",)

status.register("disk",
    hints = {"separator": False, "separator_block_width": 5},
    path="/",
    format=": {percentage_used:.1f}%",
    on_leftclick="termite --geometry=1200x700 --title=glances -e 'glances -1'",)

status.register("mem",
    color="#FFFFFF",
    warn_color="#E5E500",
    alert_color="#FF1919",
    format=": {used_mem:.0f} MB",
    on_leftclick="termite --geometry=1200x700 --title=glances -e 'glances -1'",)

status.register("load",
    format=": {avg1} {avg15}",
    on_leftclick="termite --geometry=1200x700 --title=glances -e 'glances -1'",)

status.register("cpu_usage",
    format=": {usage:03}%",
    on_leftclick="termite --geometry=1200x700 --title=glances -e 'glances -1'",)

status.register("text",
    text="|",
    color="#222222")

status.register("shell",
    command="/usr/local/bin/fan.sh",
    error_color="#FFA500",
    on_leftclick="termite --geometry=1300x750 --title=glances -e 'glances -1'",)

status.register("temp",
    file="/sys/devices/platform/coretemp.0/hwmon/hwmon0/temp2_input",
    alert_temp=60,
    alert_color="#FF0000",
    format=": {temp:.0f} °C",
    on_leftclick="termite --geometry=1200x700 --title=glances -e 'glances -1'",)

status.register("pulseaudio",
    format=": {db} dB",
    format_muted=": M",
    color_muted="#FFA500",
    on_leftclick="termite --geometry=1300x350 --title=pulsemixer -e 'pulsemixer'",)

status.register("backlight",
    interval=5,
    format=": {percentage:.0f}%",
    backlight="intel_backlight",
    on_leftclick="/usr/bin/arandr",)

status.register("text",
    text="|",
    color="#222222")

#status.register("uname",
#    format=": {release:.11s}",
#    on_leftclick="termite --hold --geometry=680x380 --title=inxi-sys-info -e '/usr/bin/inxi -Fxz'",)

status.register("uptime",
    interval=10,
    format=": {hours} hrs",
    color="#FFFFFF",
    on_leftclick="termite --hold --geometry=680x380 --title=inxi-sys-info -e '/usr/bin/inxi -Fxz'",)

status.register("battery",
    battery_ident="BAT0",
    interval=5,
    format="{status} {percentage:.0f}% {remaining:%E%hh:%Mm} {consumption:.1f} W",
    alert=True,
    alert_percentage=15,
    color="#FFFFFF",
    critical_color="#FF1919",
    charging_color="#E5E500",
    full_color="#FFFFFF",
    on_leftclick="termite --hold --geometry=680x380 --title=inxi-sys-info -e '/usr/bin/inxi -Fxz'",
    status={
        "DIS": ":",
        "CHR": ":",
        "FULL": ":",
},)

status.register("text",
    text="|",
    color="#222222")

status.register("network",
    interface="enp0s25",
    color_up="#8AE234",
    color_down="#EF2929",
    format_up=": {v4}",
    format_down="",)

status.register("network",
    interface="wlp3s0",
    color_up="#8AE234",
    color_down="#EF2929",
    format_up=": {essid} - {quality:03.0f}%",
    format_down="",)

status.register("text",
    text="|",
    color="#222222")

status.register(RestartReminder())

status.register("runwatch",
    interval=5,
    color_down="#224444",
    color_up="#E5E500",
    path="/tmp/screen_lock_toggled_off.lock",
    on_leftclick="/usr/local/bin/toggle_xautolock.sh",
    name="")

status.register("runwatch",
    interval=5,
    color_down="#224444",
    color_up="#E5E500",
    path="/tmp/openconnect_vpn.lock",
    on_leftclick="/usr/bin/nmcli_dmenu",
    name="")

status.register("runwatch",
    interval=5,
    color_down="#224444",
    color_up="#E5E500",
    path="/tmp/touchpad_toggled.lock",
    name="")

status.register("scratchpad",
     format="{number}  ",
     color="#E5E500",
     always_show=False)

#status.register("updates",
#    format = ": {count}",
#    color="#E5E500",
#    format_no_updates = ": {count}",
#    color_no_updates="#222222",
#    backends = [pacman.Pacman(), cower.Cower()])

# To use the below, first invoke ssh -N -T -L 11111:131.204.120.103:993 AU_Gate

#status.register("mail",
#    email_client="/usr/local/bin/mutt",
#    format=": {unread}",
#    format_plural=": {unread}",
#    color_unread="#00FFFF",
#    backends=[
#        imap.IMAP(
#            # port and ssl are the defaults
#             host="localhost", port=11111, username="XXXXXX", password="XXXXXXXXX"
#            )
#])

status.run()
