# -*- coding: utf-8 -*-


import PyQt4.Qt as qt



def CreateThreadClass(func):
	class Thread(qt.QThread):
		def run(self):
			func()
	return Thread






