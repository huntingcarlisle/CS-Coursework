# CMAKE generated file: DO NOT EDIT!
# Generated by "NMake Makefiles" Generator, CMake Version 3.12

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

!IF "$(OS)" == "Windows_NT"
NULL=
!ELSE
NULL=nul
!ENDIF
SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = C:\Users\hunterc\AppData\Local\JetBrains\Toolbox\apps\CLion\ch-0\182.5107.21\bin\cmake\win\bin\cmake.exe

# The command to remove a file.
RM = C:\Users\hunterc\AppData\Local\JetBrains\Toolbox\apps\CLion\ch-0\182.5107.21\bin\cmake\win\bin\cmake.exe -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "C:\Users\hunterc\Dropbox\Code\CS-Coursework\00_College Courses\Foothill College\C++ Programming\Assignment 06"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "C:\Users\hunterc\Dropbox\Code\CS-Coursework\00_College Courses\Foothill College\C++ Programming\Assignment 06\cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles\Assignment_06.dir\depend.make

# Include the progress variables for this target.
include CMakeFiles\Assignment_06.dir\progress.make

# Include the compile flags for this target's objects.
include CMakeFiles\Assignment_06.dir\flags.make

CMakeFiles\Assignment_06.dir\main.cpp.obj: CMakeFiles\Assignment_06.dir\flags.make
CMakeFiles\Assignment_06.dir\main.cpp.obj: ..\main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="C:\Users\hunterc\Dropbox\Code\CS-Coursework\00_College Courses\Foothill College\C++ Programming\Assignment 06\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Assignment_06.dir/main.cpp.obj"
	C:\PROGRA~2\MICROS~2\2017\COMMUN~1\VC\Tools\MSVC\1414~1.264\bin\Hostx86\x86\cl.exe @<<
 /nologo /TP $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) /FoCMakeFiles\Assignment_06.dir\main.cpp.obj /FdCMakeFiles\Assignment_06.dir\ /FS -c "C:\Users\hunterc\Dropbox\Code\CS-Coursework\00_College Courses\Foothill College\C++ Programming\Assignment 06\main.cpp"
<<

CMakeFiles\Assignment_06.dir\main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Assignment_06.dir/main.cpp.i"
	C:\PROGRA~2\MICROS~2\2017\COMMUN~1\VC\Tools\MSVC\1414~1.264\bin\Hostx86\x86\cl.exe > CMakeFiles\Assignment_06.dir\main.cpp.i @<<
 /nologo /TP $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "C:\Users\hunterc\Dropbox\Code\CS-Coursework\00_College Courses\Foothill College\C++ Programming\Assignment 06\main.cpp"
<<

CMakeFiles\Assignment_06.dir\main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Assignment_06.dir/main.cpp.s"
	C:\PROGRA~2\MICROS~2\2017\COMMUN~1\VC\Tools\MSVC\1414~1.264\bin\Hostx86\x86\cl.exe @<<
 /nologo /TP $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) /FoNUL /FAs /FaCMakeFiles\Assignment_06.dir\main.cpp.s /c "C:\Users\hunterc\Dropbox\Code\CS-Coursework\00_College Courses\Foothill College\C++ Programming\Assignment 06\main.cpp"
<<

# Object files for target Assignment_06
Assignment_06_OBJECTS = \
"CMakeFiles\Assignment_06.dir\main.cpp.obj"

# External object files for target Assignment_06
Assignment_06_EXTERNAL_OBJECTS =

Assignment_06.exe: CMakeFiles\Assignment_06.dir\main.cpp.obj
Assignment_06.exe: CMakeFiles\Assignment_06.dir\build.make
Assignment_06.exe: CMakeFiles\Assignment_06.dir\objects1.rsp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="C:\Users\hunterc\Dropbox\Code\CS-Coursework\00_College Courses\Foothill College\C++ Programming\Assignment 06\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Assignment_06.exe"
	C:\Users\hunterc\AppData\Local\JetBrains\Toolbox\apps\CLion\ch-0\182.5107.21\bin\cmake\win\bin\cmake.exe -E vs_link_exe --intdir=CMakeFiles\Assignment_06.dir --manifests  -- C:\PROGRA~2\MICROS~2\2017\COMMUN~1\VC\Tools\MSVC\1414~1.264\bin\Hostx86\x86\link.exe /nologo @CMakeFiles\Assignment_06.dir\objects1.rsp @<<
 /out:Assignment_06.exe /implib:Assignment_06.lib /pdb:"C:\Users\hunterc\Dropbox\Code\CS-Coursework\00_College Courses\Foothill College\C++ Programming\Assignment 06\cmake-build-debug\Assignment_06.pdb" /version:0.0  /machine:X86 /debug /INCREMENTAL /subsystem:console kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib 
<<

# Rule to build all files generated by this target.
CMakeFiles\Assignment_06.dir\build: Assignment_06.exe

.PHONY : CMakeFiles\Assignment_06.dir\build

CMakeFiles\Assignment_06.dir\clean:
	$(CMAKE_COMMAND) -P CMakeFiles\Assignment_06.dir\cmake_clean.cmake
.PHONY : CMakeFiles\Assignment_06.dir\clean

CMakeFiles\Assignment_06.dir\depend:
	$(CMAKE_COMMAND) -E cmake_depends "NMake Makefiles" "C:\Users\hunterc\Dropbox\Code\CS-Coursework\00_College Courses\Foothill College\C++ Programming\Assignment 06" "C:\Users\hunterc\Dropbox\Code\CS-Coursework\00_College Courses\Foothill College\C++ Programming\Assignment 06" "C:\Users\hunterc\Dropbox\Code\CS-Coursework\00_College Courses\Foothill College\C++ Programming\Assignment 06\cmake-build-debug" "C:\Users\hunterc\Dropbox\Code\CS-Coursework\00_College Courses\Foothill College\C++ Programming\Assignment 06\cmake-build-debug" "C:\Users\hunterc\Dropbox\Code\CS-Coursework\00_College Courses\Foothill College\C++ Programming\Assignment 06\cmake-build-debug\CMakeFiles\Assignment_06.dir\DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles\Assignment_06.dir\depend

