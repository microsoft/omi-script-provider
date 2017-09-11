import sys
import schema as sch

test_status = 0

def check_decl(decls, decl):
    if decl in decls:
        print(decl + " present   OK")
    else:
        print(decl + " missing   FAIL")
        test_status = 1

def check_type(obj, t):
    if type(obj) == t:
        print(str(type(obj)) + " found   OK")
    else:
        print(str(type(obj)) + " found, wrong type, should be" + str(t) + "   FAIL")
        test_status = 1


test_name = sys.argv[1]
print("Testing class ..." + test_name)
all_decl = dir(sch)


check_decl(all_decl, "Weak_qual_decl")
check_type(sch.Weak_qual_decl, sch.omi.MI_QualifierDecl)

check_decl(all_decl, "Weak_qual_decl_value")
check_type(sch.Weak_qual_decl_value, sch.omi.MI_Boolean)

check_decl(all_decl, "Write_qual_decl")
check_type(sch.Weak_qual_decl, sch.omi.MI_QualifierDecl)

check_decl(all_decl, "Write_qual_decl_value")
check_type(sch.Weak_qual_decl_value, sch.omi.MI_Boolean)


exit(test_status)
