#!/usr/bin/python3

from owasp.info import *
from owasp.config import *
from owasp.crypst import *
from lib.config import *
import lib.globals
import subprocess

def info():
    info001()
    info002()
    info003()
    info004()
    info005()
    info006()
    info007()
    info008()
    info009()
    info010()

def config():
    config001()

def crypst():
    crypst001()

def owasp():
    checkConfig()

    if("info" in lib.globals.TESTS):
        #info()
        print("info")
    if("config" in lib.globals.TESTS):
        #config()
        print("config")
    if("crypst" in lib.globals.TESTS):
        crypst()
        #print("crypst")
        #subprocess.call("sudo pip install netifaces", shell=True)
        