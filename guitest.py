import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import os
from os.path import exists
from os.path import expanduser
from pathlib import Path

import shutil
import subprocess

class MyWindow1(Gtk.Window):
	def __init__(self):
			super().__init__(title="Anvils Toolkit")
			self.set_border_width(10)
			self.set_default_size(640, 300)
			self.set_position(Gtk.WindowPosition.CENTER)
			self.set_resizable(False)
			button1 = Gtk.Button(label="Update System")
			button1.set_hexpand(True)
			button1.connect("clicked", self.on_button1_clicked)
			frame1 = Gtk.Frame(label="Anvils")
			
			button2 = Gtk.Button(label="Install Gaming Utils")
			button2.set_hexpand(True)
			button2.connect("clicked", self.on_button2_clicked)
			
			button3 = Gtk.Button(label="Setup Production Software")
			button3.set_hexpand(True)
			button3.connect("clicked", self.on_button3_clicked)

			button4 = Gtk.Button(label="Wiki")
			button4.set_hexpand(True)
			button4.connect("clicked", self.on_button4_clicked)

			button5 = Gtk.Button(label="News")
			button5.set_hexpand(True)
			button5.connect("clicked", self.on_button5_clicked)

			grid1 = Gtk.Grid(row_spacing    = 10,
								column_spacing = 10,
								column_homogeneous = True)
				#grid1.attach(image1,  0, 0, 3, 2)
				#grid1.attach(label1,  0, 2, 3, 2)
				#grid1.attach(label2,  0, 4, 3, 2)
				#grid1.attach(label3,  0, 6, 3, 1)
			grid1.attach(button1, 0, 7, 1, 1)
			grid1.attach(button2, 1, 7, 1, 1)
			grid1.attach(button3, 2, 7, 1, 1)
			grid1.attach(button4, 0, 8, 1, 1)
			grid1.attach(button5, 1, 8, 1, 1)
				#grid1.attach(button6, 2, 8, 1, 1)
				#grid1.attach(button7, 1, 9, 1, 1)
				#grid1.attach(label4,  0, 10, 3, 1)
			#grid1.attach(check,   2, 11, 1, 1)

			self.add(frame1)
			frame1.add(grid1)
	def on_button1_clicked(self, widget):
			print("LOG [USER CHOSE UPDATE SYSTEM!]")
			subprocess.run(["pkexec", "apt upgrade"])
	def on_button2_clicked(self, widget):
			print("LOG [USER CHOSE INSTALL GAMING UTILS! OPENING POPUP]")
			win1.hide()
			win2.show_all()
			
	def on_button3_clicked(self, widget):
			print("LOG [USER CHOSE TO INSTALL PRODUCTION SOFTWARE! OPENING POPUP!]")
			win1.hide()
			win3.show_all()
	def on_button4_clicked(self, widget):
			print("LOG [USER CHOSE TO OPEN ANVILS WIKI!]")
			subprocess.run(["xdg-open", "https://iamshivayep.github.io/Anvils-Wiki"])
	def on_button5_clicked(self, widget):
			print("LOG [USER CHOSE TO OPEN ANVILS NEWS!]")
			subprocess.run(["xdg-open", "https://iamshivayep.github.io/AnvilsProject/news"])
class MyWindow2(Gtk.Window):
	def __init__(self):
			super().__init__(title="Install Game Utilities")
			self.set_border_width(5)
			self.set_default_size(740, 480)
			self.set_position(Gtk.WindowPosition.CENTER)
			self.set_resizable(False)
			frame2 = Gtk.Frame(label="Game Utils")
			buttonsteam = Gtk.Button(label="Install Steam")
			buttonsteam.set_hexpand(True)
			buttonsteam.connect("clicked", self.on_buttonsteam_clicked)
			#button2 = Gtk.Button(label="Install Gaming Utils")
			#button2.set_hexpand(True)
			#button2.connect("clicked", self.on_button2_clicked)

			grid2 = Gtk.Grid(row_spacing    = 10,
								column_spacing = 10,
								column_homogeneous = True)
				#grid1.attach(image1,  0, 0, 3, 2)
				#grid1.attach(label1,  0, 2, 3, 2)
				#grid1.attach(label2,  0, 4, 3, 2)
				#grid1.attach(label3,  0, 6, 3, 1)
			grid2.attach(buttonsteam, 0, 7, 1, 1)
			#grid1.attach(button2, 1, 7, 1, 1)
				#grid1.attach(button3, 2, 7, 1, 1)
				#grid1.attach(button4, 0, 8, 1, 1)
				#grid1.attach(button5, 1, 8, 1, 1)
				#grid1.attach(button6, 2, 8, 1, 1)
				#grid1.attach(button7, 1, 9, 1, 1)
				#grid1.attach(label4,  0, 10, 3, 1)
			#grid1.attach(check,   2, 11, 1, 1)

			self.add(frame2)
			frame2.add(grid2)
	
	def on_buttonsteam_clicked(self, widget):
			print("LOG {User Chose To Install steam}")
			subprocess.run(["pkexec", "apt install steam"])

class MyWindow3(Gtk.Window):
	def __init__(self):
			super().__init__(title="Install Game Utilities")
			self.set_border_width(5)
			self.set_default_size(740, 480)
			self.set_position(Gtk.WindowPosition.CENTER)
			self.set_resizable(False)
			frame3 = Gtk.Frame(label="Production Software")
			buttonop1 = Gtk.Button(label="Install Kdenlive")
			buttonop1.set_hexpand(True)
			buttonop1.connect("clicked", self.on_buttonop1_clicked)
			buttonop2 = Gtk.Button(label="Install OBS Studio")
			buttonop2.set_hexpand(True)
			buttonop2.connect("clicked", self.on_buttonop2_clicked)
			buttonop3 = Gtk.Button(label="Back to Main Menu")
			buttonop3.set_hexpand(True)
			buttonop3.connect("clicked", self.on_mainmenu_clicked)
			#button2 = Gtk.Button(label="Install Gaming Utils")
			#button2.set_hexpand(True)
			#button2.connect("clicked", self.on_button2_clicked)

			grid3 = Gtk.Grid(row_spacing    = 10,
								column_spacing = 10,
								column_homogeneous = True)
				#grid1.attach(image1,  0, 0, 3, 2)
				#grid1.attach(label1,  0, 2, 3, 2)
				#grid1.attach(label2,  0, 4, 3, 2)
				#grid1.attach(label3,  0, 6, 3, 1)
			grid3.attach(buttonop1, 0, 7, 1, 1)
			grid3.attach(buttonop2, 1, 7, 1, 1)
				#grid1.attach(button3, 2, 7, 1, 1)
				#grid1.attach(button4, 0, 8, 1, 1)
				#grid1.attach(button5, 1, 8, 1, 1)
				#grid1.attach(button6, 2, 8, 1, 1)
			grid3.attach(buttonop3, 2, 8, 1, 1)
				#grid1.attach(label4,  0, 10, 3, 1)
			#grid1.attach(check,   2, 11, 1, 1)

			self.add(frame3)
			frame3.add(grid3)
	
	def on_buttonop1_clicked(self, widget):
			print("LOG [USER CHOSE KDENLIVE TO BE INSTALLED!]")
			subprocess.run(["pkexec", "apt install kdenlive"])			
	def on_buttonop2_clicked(self, widget):
			print("LOG [USER CHOSE OBS-STUDIO TO BE INSTALLED!]")
			subprocess.run(["pkexec", "apt install obs-studio"])

	def on_mainmenu_clicked(self, widget):
		print("User wants to go back to the main win1")
		win3.hide()
		win1.show_all()

win1 = MyWindow1()
win2 = MyWindow2()
win3 = MyWindow3()
win1.connect("destroy", Gtk.main_quit)
win1.show_all()
win2.connect("destroy", Gtk.main_quit)
win3.connect("destroy", Gtk.main_quit)
Gtk.main()
