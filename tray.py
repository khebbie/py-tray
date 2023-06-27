#!/usr/bin/python3
import gi
import signal
import sys
import subprocess

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

class TrayIcon(Gtk.StatusIcon):
    def __init__(self):
        Gtk.StatusIcon.__init__(self)
        self.set_from_stock(Gtk.STOCK_HOME)  # Use any stock icon you wish

        self.connect("popup-menu", self.on_right_click)
        #self.connect("activate", self.on_left_click)

    def on_right_click(self, icon, event_button, event_time):
        self.make_menu(event_button, event_time)

    #def on_left_click(self, icon):
    #    print("You left clicked the tray icon")

    def on_bash_command(self, item):
        # list device `pactl list short sinks`
        command = "pactl set-default-sink alsa_output.usb-Kingston_HyperX_Virtual_Surround_Sound_00000000-00.analog-stereo"
        subprocess.call(command, shell=True)

    def make_menu(self, event_button, event_time):
        menu = Gtk.Menu()
        bash_command_item = Gtk.MenuItem("HyperX")
        bash_command_item.connect("activate", self.on_bash_command)
        menu.append(bash_command_item)


        quit_item = Gtk.MenuItem("Quit")
        quit_item.connect("activate", Gtk.main_quit)

        menu.append(quit_item)

        menu.show_all()

        # Popup the menu
        menu.popup(None, None, None, self, event_button, event_time)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Enable Ctrl+C

    TrayIcon()
    Gtk.main()
