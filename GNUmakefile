TOP?=$(shell cd ..; pwd)


all : SCRIPTPROVIDER PYTHONWRAPPER OMIGEN_PY TEST


.phony : SCRIPTPROVIDER
SCRIPTPROVIDER :
	$(MAKE) -C $(TOP)/scriptprovider/provider \
		$(TOP)/scriptprovider/bin/libOMIScriptProvider.so


.phony : PYTHONWRAPPER
PYTHONWRAPPER :
	cd $(TOP)/scriptprovider/python && python2.7 omi_setup.py build


.phony : OMIGEN_PY
OMIGEN_PY :
	$(MAKE) -C $(TOP)/scriptprovider/omigen_py \
		$(TOP)/scriptprovider/bin/omigen_py


.phony : TEST
TEST :
	$(MAKE) -C $(TOP)/scriptprovider/test \
		$(TOP)/scriptprovider/bin/test


.phony : clean
clean :
	$(MAKE) -C $(TOP)/scriptprovider/provider clean
	cd $(TOP)/scriptprovider/python && python2.7 omi_setup.py clean
	$(MAKE) -C $(TOP)/scriptprovider/omigen_py clean
	$(MAKE) -C $(TOP)/scriptprovider/test clean


.phony : install
install :
	$(MAKE) -C $(TOP)/scriptprovider/provider install
	cd $(TOP)/scriptprovider/python && python2.7 omi_setup.py install
	$(MAKE) -C $(TOP)/scriptprovider/omigen_py install


.phony : release
release : SCRIPTPROVIDER PYTHONWRAPPER OMIGEN_PY
	$(MAKE) -C $(TOP)/scriptprovider/installbuilder
