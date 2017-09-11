# define some aliases
MKDIR:=mkdir -p -m 777
RM:=rm -f
SED:=sed
COPY:=cp
MKDEP:=-MD


TOP?=$(shell cd ../..; pwd)


include $(TOP)/omi/Unix/output/omi.mak
include $(TOP)/omi/Unix/output/config.mak


BIN_PATH:=$(TOP)/scriptprovider/bin
OBJ_PATH:=$(TOP)/scriptprovider/obj


PROVIDER=OMIScriptProvider
LIBRARY=lib$(PROVIDER).so


$(BIN_PATH)/$(LIBRARY) :


INCLUDE_PATH+=$(INCDIR)


CPPFLAGS+=$(addprefix -I,$(INCLUDE_PATH))


SOURCES:=client.cpp
SOURCES+=debug_tags.cpp
SOURCES+=mi_context.cpp
SOURCES+=mi_function_table.cpp
SOURCES+=mi_instance.cpp
SOURCES+=mi_main.cpp
SOURCES+=mi_memory_helper.cpp
SOURCES+=mi_module.cpp
SOURCES+=mi_schema.cpp
SOURCES+=mi_script_extensions.cpp
SOURCES+=mi_value.cpp
SOURCES+=server.cpp
SOURCES+=server_protocol.cpp
SOURCES+=shared_protocol.cpp
SOURCES+=socket_wrapper.cpp


OBJECTS:=$(addprefix $(OBJ_PATH)/,$(SOURCES:.cpp=.o))


# add obj path dependencies to the object files
$(OBJECTS) : | $(OBJ_PATH)


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
$(BIN_PATH)/$(LIBRARY) : \
	$(OBJECTS) | $(BIN_PATH)
	@echo ...linking: $(LIBRARY)
	$(CXX) -shared -o $@ $^


# a rule to make root bin directory
$(BIN_PATH) :
	$(MKDIR) $(BIN_PATH)

# a rule to make the obj directory
$(OBJ_PATH) :
	$(MKDIR) $(OBJ_PATH)


# an install rule
install : $(BIN_PATH)/$(LIBRARY)
	@echo ...installing: $(LIBRARY)
	@$(COPY) $(BIN_PATH)/$(LIBRARY) $(CONFIG_LIBDIR)/$(LIBRARY)
	@grep -cq '^\W*script=\-\-Python:' $(CONFIG_SYSCONFDIR)/omireg.conf || \
		echo 'script=--Python:python2.7:client.py' >> \
		$(CONFIG_SYSCONFDIR)/omireg.conf
	@grep -cq '^\W*script=\-\-python:' $(CONFIG_SYSCONFDIR)/omireg.conf || \
		echo 'script=--python:python2.7:client.py' >> \
		$(CONFIG_SYSCONFDIR)/omireg.conf


# an uninstall rule
uninstall :
	@echo ...removing: $(LIBRARY)
	@$(RM) $(CONFIG_LIBDIR)/$(LIBRARY)


# rules for output when running the clean target
.phony : clean-text
clean-text :
	@echo ...deleting: library, object, and dependency files!


# rules doing the cleanup in the root bin directory
.phony : clean-action
clean-action :
	@$(RM) $(BIN_PATH)/$(LIBRARY) \
	$(OBJECTS) $(OBJECTS:.o=.P)


# master clean target
clean : clean-text clean-action


# include shared dependency files
-include $(OBJ_PATH)/*.P
