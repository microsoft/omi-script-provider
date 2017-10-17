ifndef OSP_OUTPUTDIR
  OSP_OUTPUTDIR=$(TOP)/scriptprovider/output
endif

-include $(OSP_OUTPUTDIR)/config.mak

ifndef CONFIG_MAK
$(error "Please use ./configure script to configure for this platform")
endif
