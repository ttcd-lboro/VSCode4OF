# VSCode4OF
This example .vscode folder provides all the settings necessary to allow microsoft's intellisense engine to read the correct include paths for an OpenFOAM solver.

This is assuming OpenFOAM has been compiled using the DEBUG flag and otherwise configured as here: https://github.com/Rvadrabade/Debugging-OpenFOAM-with-Visual-Studio-Code/tree/master

Run either the rebuild task or the readIncludePaths tasks to generate the c_cpp_properties.json file based on the c_cpp_properties.json.orig template and the contents of Make/options.
