# define some aliases
MKDIR:=mkdir -p -m 777
RM:=rm -f
SED:=sed
COPY:=cp
MKDEP:=-MD


TOP?=$(shell cd ../..; pwd)
OMI_OUTPUT_DIR:=$(TOP)/omi/Unix/output


include $(OMI_OUTPUT_DIR)/omi.mak
include $(OMI_OUTPUT_DIR)/config.mak
include $(TOP)/scriptprovider/config.mak


GEN_OUTPUT_DIR:=$(OMI_OUTPUT_DIR)/obj/gen
GEN_SOURCE_DIR:=$(SRCDIR)/gen


BIN_PATH:=$(OSP_OUTPUTDIR)/bin
OBJ_PATH:=$(OSP_OUTPUTDIR)/obj


EXECUTABLE:=omigen_py


$(BIN_PATH)/$(EXECUTABLE) :


INCLUDE_PATH+=$(INCDIR)
INCLUDE_PATH+=$(SRCDIR)
INCLUDE_PATH+=$(SRCDIR)/common


INCLUDES+=$(addprefix -I,$(INCLUDE_PATH))


SOURCES:=omigen_py.cpp
SOURCES+=py_gen.cpp
SOURCES+=options.cpp


OBJECTS:=$(addprefix $(OBJ_PATH)/,$(SOURCES:.cpp=.o))


# add obj path dependencies to the object files
$(OBJECTS) : | $(OBJ_PATH)


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
$(OBJ_PATH)/%.o : %.cpp
	@echo ...compiling: $(@F)
	$(COMPILE.cpp) $(MKDEP) $< -o $@
	@-$(COPY) $(OBJ_PATH)/$*.d $(OBJ_PATH)/$*.P;
	@$(SED) -e 's/#.*//' -e 's/^[^:]*: *//' -e 's/ *\\$$//' -e '/^$$/ d' \
	    -e 's/$$/ :/' < $(OBJ_PATH)/$*.d >> $(OBJ_PATH)/$*.P
	@$(RM) $(OBJ_PATH)/$*.d


# compile rule for omigen objects
$(GEN_OUTPUT_DIR)/%.o : $(GEN_SOURCE_DIR)/%.cpp
	$(MAKE) -C $(SRCDIR)/gen $@


# link rule
$(BIN_PATH)/$(EXECUTABLE) : \
	$(OBJECTS) $(OMI_GEN_OBJECTS) | $(BIN_PATH)
	@echo ...linking: $(EXECUTABLE)
	$(LINK.cpp) -o $@ $^ $(LIBS)


# a rule to make root bin directory
$(BIN_PATH) :
	$(MKDIR) $(BIN_PATH)


# a rule to make the obj directory
$(OBJ_PATH) :
	$(MKDIR) $(OBJ_PATH)


# an install rule
install : $(BIN_PATH)/$(EXECUTABLE)
	@echo ...installing: $(EXECUTABLE)
	@$(COPY) $(BIN_PATH)/$(EXECUTABLE) $(CONFIG_BINDIR)/$(EXECUTABLE)


# an uninstall rule
uninstall :
	@echo ...removing: $(EXECUTABLE)
	@$(RM) $(CONFIG_BINDIR)/$(EXECUTABLE)


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
-include $(OBJ_PATH)/*.P
