import sys
import schema as sch
import mi_main as mim

test_status = 0

def check_decl(decls, decl):
    global test_status
    if decl in decls:
        print(decl + " present   OK")
    else:
        print(decl + " missing   FAIL")
        test_status = 1

def check_type(obj, t):
    global test_status
    if type(obj) == t:
        print(str(type(obj)) + " found   OK")
    else:
        print(str(type(obj)) + " found, wrong type, should be" + str(t) + "   FAIL")
        test_status = 1

def get_last_word(line):
    words = line.split()
    member = words[len(words)-1]
    #remove ';' from the end, also removes trailing white space
    member = member.split(";")[0]
    #remove '[]' in case of arrays
    member = member.split("[")[0]
    member = member.split("]")[0]
    #remove '()' in case of function
    member = member.split("(")[0]
    member = member.split(")")[0]
    #remove ',' in case of function parameter
    member = member.split(",")[0]

    return member

#does naive parsing to gather class names and member names
def get_class_names(mof_file):
    classes = []
    with open(mof_file) as f:
        file_lines = f.readlines()

    inside_class = False
    inside_func = False
    class_def = []
    class_mem = []
    func_mem = []
    func_name = ""
    for line in file_lines:
        if line.find("class") != -1:
            class_def.append(line.split()[1])

        if line.find("{") != -1:
            inside_class = True
        if line.find("}") != -1:
            inside_class = False
            class_def.append(class_mem)
            classes.append(class_def)
            class_def = []
            class_mem = []

        if line.find("(") != -1:
            if line.find(")") == -1:
                inside_func = True
                func_name = get_last_word(line)

        if line.find(")") != -1:
            if line.find("(") == -1:
                inside_func = False
                class_mem.append([func_name, func_mem])
                func_mem = []
                func_name = ""

        if inside_class:
            if inside_func:
                last_word = get_last_word(line)
                if func_name != last_word:
                    func_mem.append(last_word) 
            else:
                if line.find(";") != -1:
                    #is it a function with no parameters
                    if line.find("()") != -1:
                        class_mem.append([get_last_word(line), []])
                    else:
                        mem_name = get_last_word(line)
                        if(mem_name != ""):
                            class_mem.append(mem_name)

    return classes


mof_file = sys.argv[1]
print("Testing mof file ..." + mof_file)
all_decl = dir(sch)
classes = get_class_names(mof_file)

#check if declarations are correct
check_decl(all_decl, "Weak_qual_decl")
check_type(sch.Weak_qual_decl, sch.omi.MI_QualifierDecl)

check_decl(all_decl, "Weak_qual_decl_value")
check_type(sch.Weak_qual_decl_value, sch.omi.MI_Boolean)

check_decl(all_decl, "Write_qual_decl")
check_type(sch.Weak_qual_decl, sch.omi.MI_QualifierDecl)

check_decl(all_decl, "Write_qual_decl_value")
check_type(sch.Weak_qual_decl_value, sch.omi.MI_Boolean)

#check if class declarations are present
for clazz in classes:
    clazz_name = clazz[0]
    clazz_memb = clazz[1]

    check_decl(all_decl, clazz_name + "_quals")
    check_decl(all_decl, clazz_name + "_properties")
    check_decl(all_decl, clazz_name + "_methods")
    check_decl(all_decl, clazz_name + "_functions")
    check_decl(all_decl, clazz_name + "_class")

    for memb in clazz_memb:
        if type(memb) == list:
            check_decl(all_decl, clazz_name + "_" + memb[0] + "_quals")
            check_decl(all_decl, clazz_name + "_" + memb[0] + "_params")
            check_decl(all_decl, clazz_name + "_" + memb[0] + "_method")

            for param in memb[1]:
                check_decl(all_decl, clazz_name + "_" + memb[0] + "_" + param + "_quals")
                check_decl(all_decl, clazz_name + "_" + memb[0] + "_" + param + "_param")
        else:
            check_decl(all_decl, clazz_name + "_" + memb + "_quals")
            check_decl(all_decl, clazz_name + "_" + memb + "_prop")


exit(test_status)
