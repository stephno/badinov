#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ----------------------------------------------------------------------
# Name		:	Pr. Badinov (v.1.0)
# Purpose	:	Simple number base conversion tool (bases: 2, 10, 16).
#
# Author	:	Steph. N.
# Created	:	2017, Feb. 21st
# Licence 	:	GNU GPL (v.3). See LICENCE for details.
#-----------------------------------------------------------------------

from tkinter import * 
from tkinter import ttk

import math

#=======================#
# Conversion procedures #
# ======================#

# This array stores the different values
# for the hexadecimal result.
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
		 'A', 'B', 'C', 'D', 'E', 'F']


#--------#
# BASE 2 #
#--------#

# Base 10 -> Base 2
def binConvert(decValue):
	# Initializing the result variable.
	binResult = ''

	# Getting the number to convert.
	if decValue == 0:
		binResult = "0"
	else:
		while decValue != 0:
			tmpResult = str(decValue % 2)
			binResult = tmpResult + binResult
			decValue = decValue // 2

	return binResult

# Base 2 -> Base 10
def decConvertB(binValue):
	# Initializing the result
	# and exponent variables.
	decResult = 0
	expo = 0

	# Getting the number to convert.
	while len(binValue) > 0:
	 decResult +=  int(binValue[-1:]) * pow(2, expo)
	 binValue = binValue[:-1] # Removing the last char of the string.
	 expo += 1

	return decResult


#---------#
# BASE 16 #
#---------#

# Base 10 -> Base 16
def hexaConvert(decValue):
	# Initializing the result variable.
	hexaResult = ''

	# Getting the number to convert.
	if decValue == 0:
		hexaResult = "0"
	else:
		while decValue != 0:
			hexaResult = digit[decValue % 16] + hexaResult
			decValue = decValue // 16

	return hexaResult

# Base 16 -> Base 10
def decConvertH(hexValue):
	# Initializing the result
	# and exponent variables.
	decResult = 0
	expo = 0

	# Getting the number to convert.
	hexValue = hexValue.upper() # User might use lower/upper case, it doesn’t matter.

	while len(hexValue) > 0:
	 decResult +=  digit.index(hexValue[-1]) * pow(16, expo)
	 hexValue = hexValue[:-1] # Removing the last char of the string.
	 expo += 1

	return decResult

# To put things in the right places.
def convert(*args):
	try:
		# When entering a decimal number.
		if decimal.get():
			decValue = int(decimal.get())
			binValue = binary.get()
			hexValue = hexa.get()

			binary.set(binConvert(decValue))
			hexa.set(hexaConvert(decValue))

		# When entering a binary number.
		if binary.get():
			binValue = binary.get()
			decValue = decimal.get()
			hexValue = hexa.get()

			binToDec = decConvertB(binValue)
			decimal.set(binToDec)
			hexa.set(hexaConvert(binToDec))

		# When entering an hexa number.
		if hexa.get():
			hexValue = hexa.get()
			decValue = decimal.get()
			binValue = binary.get()

			hexToDec = decConvertH(hexValue)
			decimal.set(hexToDec)
			binary.set(binConvert(hexToDec))

		# Easter Egg
		if str(decValue) == "42" or binValue == "101010" or hexValue == "2A":
			ttk.Label(mainFrame, text = "Deep Thought!").grid(column = 2, row = 4, sticky = (W, E))
		else:
			ttk.Label(mainFrame, text = "").grid(column = 2, row = 4, sticky = (W, E))

	except ValueError:
		pass

#=============#
# GUI section #
# ============#

# About window
def aboutWindow():
	# Child window
	aboutWin = Toplevel()
	aboutWin.title("About Pr. Badinov…")
	aboutWin.geometry('250x100')

	# Display info
	aboutMsg1 = "Pr. Badinov (1.0)"
	aboutMsg2 = "GNU GPL v.3"
	aboutMsg3 = "Copyright © 2017 Steph. N."
	msg1 = Label(aboutWin, text = aboutMsg1, font = ("bold", 16)).pack()
	msg2 = Label(aboutWin, text = aboutMsg2).pack()
	msg3 = Label(aboutWin, text = aboutMsg3).pack()

	# Close Child window and return to the root window
	wrapButton = Button(aboutWin, text = "Close", command = aboutWin.destroy).pack()


# Root Window
window = Tk()
window.title("Pr. Badinov")

# Set the global interface up.
mainFrame = ttk.Frame(window, padding = "3 3 12 12")
mainFrame.grid(column = 0, row = 0, sticky = (N, W, E, S))
mainFrame.columnconfigure(0, weight = 1)
mainFrame.rowconfigure(0, weight = 1)

#----------------------#
# The different items  #
#----------------------#
decimal = StringVar()
binary = StringVar()
hexa = StringVar()

decimal_entry = ttk.Entry(mainFrame, width = 7, textvariable = decimal)
decimal_entry.grid(column = 2, row = 1, sticky = (W, E))

binary_entry = ttk.Entry(mainFrame, width = 7, textvariable = binary)
binary_entry.grid(column = 2, row = 2, sticky = (W, E))

hexa_entry = ttk.Entry(mainFrame, width = 7, textvariable = hexa)
hexa_entry.grid(column = 2, row = 3, sticky = (W, E))

ttk.Button(mainFrame, text="Convert", command = convert).grid(column = 2, row = 5, sticky = (W, E))

ttk.Label(mainFrame, text = "Decimal:").grid(column = 1, row = 1, sticky = E)
ttk.Label(mainFrame, text = "Binary:").grid(column = 1, row = 2, sticky = E)
ttk.Label(mainFrame, text = "Hexa:").grid(column = 1, row = 3, sticky = E)
ttk.Label(mainFrame, text= "").grid(column = 2, row = 4, sticky = (W, E))

# Adjusting paddings and focus.
for child in mainFrame.winfo_children(): child.grid_configure(padx = 5, pady = 5)
decimal_entry.focus()
window.bind('<Return>', convert)


#-------------------#
# A little menu bar #
#-------------------#
menuBar = Menu(window)
window.config(menu = menuBar)

menu1 = Menu(menuBar, tearoff = 0)
menuBar.add_cascade(label = "File", menu = menu1)
menu1.add_command(label = "Quit (Ctrl + Q)", command = window.quit)

menu2 = Menu(menuBar, tearoff = 0)
menuBar.add_cascade(label = "Help", menu = menu2)
menu2.add_command(label = "About", command = aboutWindow)

# “Good night everybody!”
window.bind('<Control-q>', quit)

window.mainloop()