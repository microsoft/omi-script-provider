TOP?=$(shell cd ../..; pwd)

STAGING_DIR:=$(TOP)/scriptprovider/staging
INTERMEDIATE_DIR:=$(TOP)/scriptprovider/intermediate
RELEASE_DIR:=$(TOP)/scriptprovider/release

IB_DIR:=$(TOP)/pal/installer/InstallBuilder

UNAME_P:=$(shell uname -p)
ifeq ($(UNAME_P),x86_64)
 PF_ARCH := x64
else
 PF_ARCH := x86
endif

CONFIG_VERSION:=1.1.1

OMI_SCRIPTPROVIDER_VERSION_BUILD=1

SHORT_NAME=OMIScriptProvider
LONG_NAME=OMI Provider for scripting languages for Linux
PROVIDES=omiscriptproviderpkg
DESCRIPTION=Enables OMI providers to be written in scripting languages for Linux
RUN_AS_USER=root

ifeq ("$(wildcard /usr/bin/dpkg-deb)","")
DPKG_LOCATION=--DPKG_LOCATION="$(IB_DIR)/tools/bin/dpkg-deb-$(PF_ARCH)"
else
DPKG_LOCATION=
endif


all:
	@echo "========================= Make DSC installer"
	sudo rm -rf $(STAGING_DIR) $(INTERMEDIATE_DIR) $(RELEASE_DIR)/*.rpm \
		$(RELEASE_DIR)/*.rpm
	mkdir -p $(RELEASE_DIR) $(STAGING_DIR) $(INTERMEDIATE_DIR)
	python $(IB_DIR)/installbuilder.py \
		--BASE_DIR=$(TOP)/scriptprovider \
		--TARGET_DIR=$(RELEASE_DIR) \
		--INTERMEDIATE_DIR=$(INTERMEDIATE_DIR) \
		--STAGING_DIR=$(STAGING_DIR) \
		--PACKAGE_TYPE=RPM \
		--PF=Linux \
		--PFMAJOR=1 \
		--PFMINOR=0 \
		--PFARCH=$(PF_ARCH) \
		--PFDISTRO=ULINUX \
		--VERSION=$(CONFIG_VERSION) \
		--RELEASE=$(OMI_SCRIPTPROVIDER_VERSION_BUILD) \
		--SHORT_NAME=$(SHORT_NAME) \
		--LONG_NAME="$(LONG_NAME)" \
		--PROVIDES=$(PROVIDES) \
		--DESCRIPTION="$(DESCRIPTION)" \
		--RUN_AS_USER="$(RUN_AS_USER)" \
		--OUTPUTFILE=$(SHORT_NAME)-$(CONFIG_VERSION)-$(OMI_SCRIPTPROVIDER_VERSION_BUILD).ssl_$(SSL_VERSION).$(PF_ARCH) \
		--DATAFILE_PATH="$(TOP)/scriptprovider/installbuilder" \
		Base_OMIScriptProvider.data

	@echo "========================= Make DSC installer"
	sudo rm -rf $(STAGING_DIR) $(INTERMEDIATE_DIR) 
	mkdir -p $(RELEASE_DIR) $(STAGING_DIR) $(INTERMEDIATE_DIR)
	python $(IB_DIR)/installbuilder.py \
		--BASE_DIR=$(TOP)/scriptprovider \
		--TARGET_DIR=$(RELEASE_DIR) \
		--INTERMEDIATE_DIR=$(INTERMEDIATE_DIR) \
		--STAGING_DIR=$(STAGING_DIR) \
		--PACKAGE_TYPE=DPKG \
		--PF=Linux \
		--PFMAJOR=1 \
		--PFMINOR=0 \
		--PFARCH=$(PF_ARCH) \
		--PFDISTRO=ULINUX \
		--VERSION=$(CONFIG_VERSION) \
		--RELEASE=$(OMI_SCRIPTPROVIDER_VERSION_BUILD) \
		--SHORT_NAME=$(SHORT_NAME) \
		--LONG_NAME="$(LONG_NAME)" \
		--PROVIDES=$(PROVIDES) \
		--DESCRIPTION="$(DESCRIPTION)" \
		--RUN_AS_USER="$(RUN_AS_USER)" \
		--OUTPUTFILE=$(SHORT_NAME)-$(CONFIG_VERSION)-$(OMI_SCRIPTPROVIDER_VERSION_BUILD).ssl_$(SSL_VERSION).$(PF_ARCH) \
		$(DPKG_LOCATION) \
		--DATAFILE_PATH="$(TOP)/scriptprovider/installbuilder" \
		Base_OMIScriptProvider.data
