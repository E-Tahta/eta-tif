INSTALL=install -m 0644
PYTHON_FILE=eta-tif.py
DESKTOP_FILE=eta-tif-autostart.desktop
X_SESSION_FILE=99eta-a11y

install: 
	mkdir -p $(DESTDIR)/usr/share/eta/eta-tif
	install -m 0755 $(PYTHON_FILE) $(DESTDIR)/usr/share/eta/eta-tif
	mkdir -p $(DESTDIR)/usr/bin
	cd $(DESTDIR)/usr/bin && ln -s $(DESTDIR)/usr/share/eta/eta-tif/$(PYTHON_FILE) eta-tif

	mkdir -p $(DESTDIR)/etc/xdg/autostart
	install -m 0644 $(DESKTOP_FILE) $(DESTDIR)/etc/xdg/autostart

	mkdir -p $(DESTDIR)/etc/X11/Xsession.d
	install -m 0644 $(X_SESSION_FILE) $(DESTDIR)/etc/X11/Xsession.d
