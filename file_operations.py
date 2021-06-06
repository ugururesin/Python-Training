def get_file_ext(filename):
	return filename[filename.index(".")+1:]

def get_filename_length(filename):
	return len(filename.rsplit('.', 1)[0])

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