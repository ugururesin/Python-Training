def get_file_ext(filename):
	return filename[filename.index(".")+1:]

programming_extensions = {
	".c":"C and C++ source code file",
	".cgi and .pl":"Perl script file",
	".class":"Java class file",
	".cpp":"C++ source code file",
	".cs":"Visual C# source code file",
	".h":"C, C++, and Objective-C header file",
	".java":"Java Source code file",
	".php":"PHP script file"
}