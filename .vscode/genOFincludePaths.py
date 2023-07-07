import sys
import re
import os
import shutil

def genOFincludePaths():

    with open('Make/options', 'r') as file:
        content = file.read()

    # Extract the entries from EXE_INC using regular expressions
    matches = re.findall(r'-I\s*(.*?)\\', content)

    include_paths = []

    # Trim leading and trailing whitespace from each match
    for match in matches:
        path = match.strip()
        path = path.replace('$(','${env:')
        path = path.replace(")","}")
        include_paths.append(path)

    return(include_paths)

if __name__ == "__main__":
    # Check if an argument is provided
    if len(sys.argv) > 1:
        # Get the input value from the command line argument
        thePath = str(sys.argv[1])
        os.chdir(thePath)
        shutil.copy('.vscode/c_cpp_properties.json.orig', '.vscode/c_cpp_properties.json')

        # Call the function and store the result
        result = genOFincludePaths()
        #result = ', '.join(result)
        
        # Print the output variable
        # print(result)
        src_dir =os.environ['FOAM_SRC']

        with open('.vscode/c_cpp_properties.json', 'r') as file:
            jsoncontent = file.read()
            #jsoncontent = jsoncontent.replace("${FOAM_SRC}",src_dir)
            jsoncontent = jsoncontent.replace('"includePath": [','"includePath": ['+ "\"${env:WM_PROJECT_DIR}/src/OpenFOAM/lnInclude\",\"lninclude\"," + '"'+"\",\"".join(result)+'"')
            jsoncontent = jsoncontent.replace('LIB_SRC','FOAM_SRC')
        print('jsoncontent:')
        print(jsoncontent)
        
        with open('.vscode/c_cpp_properties.json', 'w') as file:
            file.write(jsoncontent)

    else:
        print("Please provide an input value.")
