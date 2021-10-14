INSTALL=/usr/bin/install
DESTDIR=/usr/lib/nagios/plugins/

all: pip

pip:
	pip install -r requirements.txt


install: pip
	$(INSTALL) -d $DESTDIR
	$(INSTALL) -m 755 check-consul-service-health.py "$(DESTDIR)/check_consul_service_health"

