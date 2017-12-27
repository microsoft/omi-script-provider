TOP?=$(shell cd ..; pwd)

include $(TOP)/scriptprovider/config.mak


all : SCRIPTPROVIDER PYTHONWRAPPER OMIGEN_PY TEST


.phony : SCRIPTPROVIDER
SCRIPTPROVIDER :
	$(MAKE) -C $(TOP)/scriptprovider/provider \
		$(OSP_OUTPUTDIR)/bin/libOMIScriptProvider.so


.phony : PYTHONWRAPPER
PYTHONWRAPPER :
	cd $(TOP)/scriptprovider/python && $(CONFIG_PYTHON_NAME) omi_setup.py \
       build --build-temp $(OSP_OUTPUTDIR)/python/build


.phony : OMIGEN_PY
OMIGEN_PY :
	$(MAKE) -C $(TOP)/scriptprovider/omigen_py \
		$(OSP_OUTPUTDIR)/bin/omigen_py


.phony : TEST
TEST :
	$(MAKE) -C $(TOP)/scriptprovider/test \
		$(OSP_OUTPUTDIR)/bin/test


.phony : clean
clean :
	$(MAKE) -C $(TOP)/scriptprovider/provider clean
	cd $(TOP)/scriptprovider/python && $(CONFIG_PYTHON_NAME) omi_setup.py clean
	$(MAKE) -C $(TOP)/scriptprovider/omigen_py clean
	$(MAKE) -C $(TOP)/scriptprovider/test clean


.phony : install
install :
	$(MAKE) -C $(TOP)/scriptprovider/provider install
	cd $(TOP)/scriptprovider/python && $(CONFIG_PYTHON_NAME) omi_setup.py \
       install
	$(MAKE) -C $(TOP)/scriptprovider/omigen_py install


.phony : release
release : SCRIPTPROVIDER PYTHONWRAPPER OMIGEN_PY
	$(MAKE) -C $(TOP)/scriptprovider/installbuilder
