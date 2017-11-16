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


BIN_PATH:=$(OSP_OUTPUTDIR)/bin
OBJ_PATH:=$(OSP_OUTPUTDIR)/obj


EXECUTABLE:=test


$(BIN_PATH)/$(EXECUTABLE) :


INCLUDE_PATH+=$(INCDIR)
INCLUDE_PATH+=$(TOP)/scriptprovider/provider
INCLUDE_PATH+=$(SRCDIR)
INCLUDE_PATH+=$(SRCDIR)/common


INCLUDES+=$(addprefix -I,$(INCLUDE_PATH))


SOURCES:=test.cpp
SOURCES+=test_helper.cpp
SOURCES+=traits_test.cpp
SOURCES+=repeat_test.cpp
SOURCES+=default_delete_test.cpp
SOURCES+=internal_counted_ptr_test.cpp
SOURCES+=unique_ptr_test.cpp
SOURCES+=mi_type_test.cpp
SOURCES+=mi_script_extensions_test.cpp
SOURCES+=mi_memory_helper_test.cpp
SOURCES+=socket_wrapper_test.cpp
SOURCES+=shared_protocol_test.cpp
SOURCES+=mi_value_test.cpp
SOURCES+=getopt_test.cpp


OBJECTS:=$(addprefix $(OBJ_PATH)/,$(SOURCES:.cpp=.o))


# add obj path dependencies to the object files
$(OBJECTS) : | $(OBJ_PATH)


LDFLAGS+=-L$(BIN_PATH)
LDFLAGS+=-L$(LIBDIR)
LDFLAGS+=-Wl,-R/$(BIN_PATH)
LIBS+=-lOMIScriptProvider
LIBS+=-lbase
LIBS+=-lpal

CPPFLAGS+=$(INCLUDES)


# compile rule
$(OBJ_PATH)/%.o : %.cpp
	@echo ...compiling: $(@F)
	$(COMPILE.cpp) $(MKDEP) $< -o $@
	@-$(COPY) $(OBJ_PATH)/$*.d $(OBJ_PATH)/$*.P;
	@$(SED) -e 's/#.*//' -e 's/^[^:]*: *//' -e 's/ *\\$$//' -e '/^$$/ d' \
	    -e 's/$$/ :/' < $(OBJ_PATH)/$*.d >> $(OBJ_PATH)/$*.P
	@$(RM) $(OBJ_PATH)/$*.d


# link rule
$(BIN_PATH)/$(EXECUTABLE) : \
	$(OBJECTS) | $(BIN_PATH)
	@echo ...linking: $(EXECUTABLE)
	$(LINK.cpp) -o $@ $^ $(LIBS)


# a rule to make root bin directory
$(BIN_PATH) :
	$(MKDIR) $(BIN_PATH)


# a rule to make the obj directory
$(OBJ_PATH) :
	$(MKDIR) $(OBJ_PATH)


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
