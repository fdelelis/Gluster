# All PHONY targets, here for convenience

PROGRAM = gcollect

prefix = /usr
sbindir = $(prefix)/sbin
sysconfdir = /etc
pkgbuilddir := $(shell pwd)/pkg-build
pkgdir := $(shell pwd)/pkgs

RPMBUILD = rpmbuild --define "_topdir $(pkgbuilddir)" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir $(pkgdir)" \
        --define "_srcrpmdir %{_rpmdir}" \
        --define "_sourcedir  %{_topdir}"

SUBDIRS = \
	./ \
	sbin/ \
	conf/ \
	conf/$(PROGRAM)/ \
	conf/$(PROGRAM)/ganglia.d/ \
	conf/$(PROGRAM)/ganglia.custom.d/ \

CLEANDIRS = \
	$(addsuffix *~,$(SUBDIRS)) \
	$(addsuffix *.bak,$(SUBDIRS)) \
	$(addsuffix *.tmp,$(SUBDIRS)) \
	$(addsuffix *.out,$(SUBDIRS))

.PHONY: install clean test sense
all: clean

install:
	@echo "Installing the program"
	@echo "DESTDIR set to " $(DESTDIR)
	@mkdir -p $(DESTDIR)$(sbindir)/
	@install -m 0750 sbin/$(PROGRAM) $(DESTDIR)$(sbindir)/
	@install -m 0750 sbin/niopid $(DESTDIR)$(sbindir)/

	@echo "Installing the configuration files"
	@install -m 0750 -d $(DESTDIR)$(sysconfdir)/$(PROGRAM)
	@install -m 0640 conf/$(PROGRAM)/$(PROGRAM).cfg $(DESTDIR)$(sysconfdir)/$(PROGRAM)/
	@for configdir in `ls -d conf/$(PROGRAM)/*.d`; do \
	  configdir=`basename $${configdir} .d`; \
	  echo $${configdir}; \
	  install -m 0750 -d $(DESTDIR)$(sysconfdir)/$(PROGRAM)/$${configdir}.d; \
	  install -m 0750 -d $(DESTDIR)$(sysconfdir)/$(PROGRAM)/$${configdir}.custom.d; \
	  install -m 0640 conf/$(PROGRAM)/$${configdir}.d/* $(DESTDIR)$(sysconfdir)/$(PROGRAM)/$${configdir}.d/; \
	done
clean:
	@echo "Cleaning house"
	@rm -f $(CLEANDIRS)
	@rm -rf $(pkgbuilddir) $(pkgdir)
	@rm -f $(PROGRAM).tgz

sdist: clean
	@echo "Creating tarball"
	@tar -czf $(PROGRAM).tgz * --exclude=*.spec

prep_pkgbuild: sdist
	@echo "Preparing for package build"
	@mkdir -p $(pkgbuilddir)
	@mkdir -p $(pkgdir)
	@mv $(PROGRAM).tgz $(pkgbuilddir)

srpm: prep_pkgbuild
	@echo "Building source package (RPM)"
	@$(RPMBUILD) -bs $(PROGRAM).spec

rpms: prep_pkgbuild
	@echo "Building package (RPM)"
	@$(RPMBUILD) -ba $(PROGRAM).spec

deb: prep_pkgbuild
	@echo "Building package (DEB)"
	@echo "Not yet implemented, feel free to." 
