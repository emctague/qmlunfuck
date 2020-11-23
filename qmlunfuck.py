# type unfuck
# -----------
# This python script deals with the issue of Qt Creator not being able to recognize element types
# registered using 'QML_ELEMENT'.
#
# It does so by generating a header, 'myprojectname_metatypes.h'.
# Include this header ONLY in main.cpp, and then call `registerTypes()` first thing in `main`.
# Then, Qt Creator will stop whining.

import sys
import json

source_path = sys.argv[1]
dest_path = sys.argv[2]
import_name = sys.argv[3]
import_major = sys.argv[4]

with open(source_path) as f:
    data = json.load(f)


includes = ["QtQml"]
types = []

for file in data:
    includes.append(file["inputFile"])

    for type in file["classes"]:
        if "classInfos" in type and {"name":"QML.Element","value":"auto"} in type["classInfos"]:
            types.append(type["className"])

with open(dest_path, 'w') as f:
    for i in includes:
        f.write(f'#include <{i}>\n')

    f.write('void __attribute__ ((constructor)) registerTypes() {\n')
    for t in types:
        f.write(f'\tqmlRegisterType<{t}>("{import_name}", {import_major}, 0, "{t}");\n')
    f.write('}\n')
