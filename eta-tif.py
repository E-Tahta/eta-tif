#!/usr/bin/env python2.7

import pyatspi
import dbus, signal

keyboard = None
session_bus = dbus.SessionBus()


def getdbusinterface(name, path, interface):
    obj = session_bus.get_object(name, path)
    return dbus.Interface(obj, dbus_interface=interface)


def getkeyboard():
    try:
        obj = getdbusinterface('org.eta.virtualkeyboard',
                               '/VirtualKeyboard',
                               'org.eta.virtualkeyboard')
        return obj
    except Exception as e:
        print(e)
        return None


def onfocuschanged(e):
    global keyboard
    keyboard = getkeyboard()
    try:
        if keyboard is not None:
            atspi_role = e.source.getRole()
            print (str(atspi_role))

            if pyatspi.ROLE_TEXT == atspi_role or pyatspi.ROLE_ENTRY == atspi_role or pyatspi.ROLE_COMBO_BOX == atspi_role:
                keyboard.show(False)
            elif pyatspi.ROLE_PASSWORD_TEXT == atspi_role:
                keyboard.show(True)
            else:
                keyboard.hide()
            return
        else:
            keyboard = getkeyboard()
    except Exception as e:
        print(e)
        return

def sighandler(signum, frame):
    import sys
    sys.exit(0)

signal.signal(signal.SIGTERM, sighandler)
signal.signal(signal.SIGINT, sighandler)

pyatspi.Registry.registerEventListener(onfocuschanged, 'focus')
pyatspi.Registry.start()