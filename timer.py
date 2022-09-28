import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
import datetime
import time
import threading 
import os
import platform


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Timer")
        self.set_border_width(10)
        self.set_size_request(200,100)
        self.vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.add(self.vbox_right)
        self.fr_label = Gtk.Label()
        self.vbox_right.pack_start(self.fr_label, True, True, 0)
        self.show_all()


def update_label(label, text):
    label.set_text(text)


def countdown(total_seconds):
    while total_seconds >= 0:
        timer = datetime.timedelta(seconds = total_seconds)
        GLib.idle_add(update_label, win.fr_label, str(timer))
        win.show_all()
        time.sleep(1)
        total_seconds -= 1
        print('timer', timer)
    else:
        print("Done")
        if platform.system() =='Linux':
            os.system('paplay --volume=63000 /usr/share/sounds/freedesktop/stereo/bell.oga')
        else:
            os.system('(New-Object System.Media.SoundPlayer).playsync()')



class FirstMainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Timer Data")
        self.set_border_width(10)
        self.set_size_request(200,100)
    
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.add(vbox_right)

        self.lst_label = Gtk.Label()
        self.lst_label.set_text("Minutes:")
        self.lst_label.set_alignment(0.05,0)
        vbox_right.pack_start(self.lst_label, True, True, 0)

        self.last = Gtk.Entry()
        vbox_right.pack_start(self.last, True, True, 0)

        self.th_label = Gtk.Label()
        self.th_label.set_text("Seconds:")
        self.th_label.set_alignment(0.05,0)
        vbox_right.pack_start(self.th_label, True, True, 0)

        self.third = Gtk.Entry()
        vbox_right.pack_start(self.third, True, True, 0)

        self.button = Gtk.Button(label="Add")
        self.button.connect('clicked', self.on_click)
        vbox_right.pack_start(self.button, True, True, 0)

    def clear_text(self):
        self.last.delete_text(0, -1)
        self.third.delete_text(0, -1)

    def on_click(self, button):
        print(self.last.get_text() + ' ' + self.third.get_text())
        if self.last.get_text() == '':
            self.in_seconds = int(self.third.get_text())
        if self.third.get_text() == '':
            self.in_seconds = int(self.last.get_text())*60 
        if self.last.get_text() != '' and self.third.get_text() != '':
            self.in_seconds = int(self.last.get_text())*60 + int(self.third.get_text())
        self.clear_text()
        self.destroy()
        win = MainWindow()
        win.show_all()
        thread = threading.Thread(daemon=True, target=countdown, args=[self.in_seconds])
        thread.start()
        win.connect("delete-event",Gtk.main_quit)



win_one = FirstMainWindow()
win_one.connect("delete-event",Gtk.main_quit)
win_one.show_all()

win = MainWindow()
win.hide()

Gtk.main()