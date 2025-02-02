'''
Specifically for the Advanced Python Programming Course
Author: Arta Khosravi
Last Update: Jan. 2025
'''
'''
Using Virtual Environments instead of Operating System (OS) dependant envrionments
helps us to adapt the code to as many different situations, OSs, and versions as possible.
For example my system's Python version is 3.6, but a library 
I need uses Python 3.12.
For that, I can use the cmd code //py -m virtualenv venv//. 
It creates a Virtuan Environment called venv for me.
I first need to have virtualenv installed, which for windows is:
~ py -m pip install virtualenv
But it hasn't been activated yet. Whenever I want to active it, I can
type "source venv/bin/activate" or "venv // Scripts // activate" 
for windows, in vscode or cmd terminal.
If it doesn't work in windows and gives an execution error, try the
"Set-ExecutionPolicy Unrestricted -Scope Process" command in terminal.
'''
'''
In our new Virtual Environment, 
if we install certain packages, only in THIS environment will they work.
If we want a specific version we can apply the command below:
"py -m pip install requests==2.6.0(or any other version)".
'''
'''
We can observe if a package is installed, its requirements and files with:
"py -m pip show (package name)"
'''
'''
"py -m pip freeze" will freeze current's situation.
For example my output is:
certifi==2025.1.31
charset-normalizer==2.0.12
idna==3.10
jdatetime==3.8.2
requests==2.27.1
urllib3==1.26.20
'''
'''
Important face about pip freeze is that if we apply the command below:
"py -m pip freeze > requirements.txt",
then it will make a file that if we (or the admin) type in:
"py -m pip install -r requirements.txt",
the required packages will be installed automatichally.
This way multiple projects will have all the required packages and sources satisfied.
'''