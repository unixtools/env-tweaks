VERSION=1.0.0
TOP=`pwd`

all:

install:
	mkdir -p $(DESTDIR)/etc/profile.d
	cp env-tweaks.sh $(DESTDIR)/etc/profile.d/env-tweaks.sh

dist:
	rm -rf /tmp/env-tweaks-$(VERSION)
	mkdir /tmp/env-tweaks-$(VERSION)
	cp -pr . /tmp/env-tweaks-$(VERSION)
	cd /tmp/env-tweaks-$(VERSION) && rm -rf *.gz .git .gitignore
	tar -C/tmp -czvf ../env-tweaks-$(VERSION).tar.gz env-tweaks-$(VERSION)
	rm -rf /tmp/env-tweaks-$(VERSION)

deb: dist
	cp ../env-tweaks-$(VERSION).tar.gz ../env-tweaks_$(VERSION).orig.tar.gz
	dpkg-buildpackage -us -uc
	rm ../env-tweaks_$(VERSION).orig.tar.gz

rpm: dist
	rm -rf rpmtmp
	mkdir -p rpmtmp/SOURCES rpmtmp/SPECS rpmtmp/BUILD rpmtmp/RPMS rpmtmp/SRPMS
	cp ../env-tweaks-$(VERSION).tar.gz rpmtmp/SOURCES/
	rpmbuild -ba -D "_topdir $(TOP)/rpmtmp" \
		-D "_builddir $(TOP)/rpmtmp/BUILD" \
		-D "_rpmdir $(TOP)/rpmtmp/RPMS" \
		-D "_sourcedir $(TOP)/rpmtmp/SOURCES" \
		-D "_specdir $(TOP)/rpmtmp/SPECS" \
		-D "_srcrpmdir $(TOP)/rpmtmp/SRPMS" \
		rpm/env-tweaks.spec
	cp $(TOP)/rpmtmp/RPMS/noarch/* ../
	cp $(TOP)/rpmtmp/SRPMS/* ../
	rm -rf rpmtmp
