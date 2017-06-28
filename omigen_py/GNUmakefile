# define some aliases
MKDIR:=mkdir -p -m 777
RM:=rm -f
SED:=sed
COPY:=cp
MKDEP:=-MD


LOCAL_DIR:=$(shell pwd)
OMI_TOP?=$(shell cd ../../omi/Unix; pwd)
OMI_OUTPUT_DIR:=$(OMI_TOP)/output


include $(OMI_OUTPUT_DIR)/omi.mak
include $(OMI_OUTPUT_DIR)/config.mak


GEN_OUTPUT_DIR:=$(OMI_OUTPUT_DIR)/obj/gen
GEN_SOURCE_DIR:=$(SRCDIR)/gen


BIN_PATH:=$(LOCAL_DIR)/bin


EXECUTABLE:=omigen_py


$(BIN_PATH)/$(EXECUTABLE) :


INCLUDE_PATH+=$(INCDIR)
INCLUDE_PATH+=$(SRCDIR)
INCLUDE_PATH+=$(SRCDIR)/common


INCLUDES+=$(addprefix -I,$(INCLUDE_PATH))


SOURCES:=main.cpp
SOURCES+=py_gen.cpp
SOURCES+=options.cpp


OBJECTS:=$(addprefix $(BIN_PATH)/,$(SOURCES:.cpp=.o))


# add object files from omi/output/obj/gen
OMI_GEN_OBJECTS:=$(GEN_OUTPUT_DIR)/Parser.o
OMI_GEN_OBJECTS+=$(GEN_OUTPUT_DIR)/QualifierDecls.o


LDFLAGS+=-L$(LIBDIR)


LIBS+=-lmof
LIBS+=-lbase
LIBS+=-lpal
LIBS+=$(shell $(BUILDTOOL) syslibs)


CPPFLAGS+=$(INCLUDES)


# compile rule
$(BIN_PATH)/%.o : %.cpp
	@echo ...compiling: $(@F)
	$(COMPILE.cpp) $(MKDEP) $< -o $@
	@-$(COPY) $(BIN_PATH)/$*.d $(BIN_PATH)/$*.P;
	@$(SED) -e 's/#.*//' -e 's/^[^:]*: *//' -e 's/ *\\$$//' -e '/^$$/ d' \
	    -e 's/$$/ :/' < $(BIN_PATH)/$*.d >> $(BIN_PATH)/$*.P
	@$(RM) $(BIN_PATH)/$*.d


# compile rule for omigen objects
$(GEN_OUTPUT_DIR)/%.o : $(GEN_SOURCE_DIR)/%.cpp
	$(MAKE) -C $(SRCDIR)/gen $@


# link rule
$(BIN_PATH)/$(EXECUTABLE) : \
	$(OBJECTS) $(OMI_GEN_OBJECTS)
	@echo ...linking: $(EXECUTABLE)
	$(LINK.cpp) -o $@ $^ $(LIBS)


# a rule to make root bin directory
$(BIN_PATH) :
	$(MKDIR) $(BIN_PATH)


# rules for output when running the clean target
.phony : clean-text
clean-text :
	@echo ...deleting: executable, object, and dependency files!


# rules doing the cleanup in the root bin directory
.phony : clean-action
clean-action :
	@$(RM) $(BIN_PATH)/$(EXECUTABLE) \
	$(OBJECTS) $(OBJECTS:.o=.P)


# master clean target
clean : clean-text clean-action


# include shared dependency files
-include $(BIN_PATH)/*.P
