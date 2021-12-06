# eecs4314-assignment3
Pertinent information for a Makefile-based dependency extraction method

# Foreword
This README outlines the steps you can use to:
1. Generate dependencies for PostgreSQL-13.4
2. Parse the generated dependency files and output them in the raw TA format. 

For instructions on generating the dependency files, start at <insert link> [Part 1](#part-1). If you'd like to simply parse the generated dependency files (which we provide with this repo), you may proceed directly to [Part 2](#part-2).
 
# Part 1
  
Instructions for generating the dependency files (Tested on CentOS). Please follow these instructions if you want to generate the object-level dependency files for PostgreSQL-13.4. If you'd like to simply parse the generated dependency files (which we provide in this repo), you may skip to [Part 2](#part-2). 

- Clone the repo
- Unzip the postgresql-13.4.tar.gz file to extract the PostgreSQL source code. 
- Rename the `configure` script in the source-code folder to `configure.original`
- Copy the `configure` script present in this repo to the source-code folder
- Run the `configure` script: `./configure`
- Check that there is a `Makefile.global` file created in the `./src/` folder
- From the parent of the `./src/` folder, run the `make all` command
- This will generate the object and the dependency files for each source file
- You can copy over the dependency files (`.d` files) to a separate folder by running the following command: ``$ cp --parents `find -name \*.d` ./dependencyfiles/``
- The following step is optional (For your convenience, we have included the `dependencyfiles` folder in this repo)
- For our group's purposes, we had all the above steps done on a CentOS machine (EECS Red Server). We then copied the `dependencyfiles` folder to one of the group member's local machines (Windows10) where he wrote and tested the Python script. 


# Part 2
  
Instructions for parsing the generated dependency files (Written and tested on Windows 10)

- If you haven't already, please clone the repo
- Within the repo, navigate to the `pythonscripts` folder
- Run the Python script `getDeps.py`: `$ python3 getDeps.py`
- You will see the parsed output in the raw TA format
  - You can redirect the output of the script to a file by: `$ python3 getDeps.py > YourFileName`

# Platforms and Dependencies
- Source code on CentOS7 (CentOS Linux Release 7.9.2009)
- Python Script on Windows10 Home (OS Build - 19042.1348) 
- Python version 3.8.3
- Python Packages: 
  - os (Part of the standard library)
  - glob (Part of the standard library)
