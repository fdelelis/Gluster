# All PHONY targets, here for convenience

PROGRAM = gcollect

prefix = /usr
sbindir = $(prefix)/sbin
sysconfdir = /etc

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
        @mkdir -p $(DESTDIR)$(sbindir)/
        @install -m 0750 sbin/$(PROGRAM) $(DESTDIR)$(sbindir)/
        @install -m 0750 sbin/niopid $(DESTDIR)$(sbindir)/
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
	@rm -f $(CLEANDIRS)
