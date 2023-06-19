# 0x00. Shell, basics

This directory contains various scripts demonstrating basic shell commands.

## File Descriptions

### Mandatory

- `0-current_working_directory`: Prints the absolute path name of the current working directory.
- `1-listit`: Displays the list of the current directory's contents.
- `2-bring_me_home`: Changes the working directory to the user's home directory.
- `3-listfiles`: Displays the current directory contents in a long format.
- `4-listmorefiles`: Displays the current directory contents, including hidden files, in a long format.
- `5-listfilesdigitonly`: Displays the current directory contents in a long format, with user and group IDs displayed numerically, and hidden files.
- `6-firstdirectory`: Creates a directory named `holberton` in the `/tmp/` directory.
- `7-movethatfile`: Moves the file `betty` from `/tmp/` to `/tmp/holberton`.
- `8-firstdelete`: Deletes the file `betty` in `/tmp/holberton`.
- `9-firstdirdeletion`: Deletes the directory `holberton` that is in the `/tmp` directory.
- `10-back`: Changes the working directory to the previous one.
- `11-lists`: Lists all files (even ones with names beginning with a period character), in the current directory and the parent of the working directory and the `/boot` directory, in long format.
- `12-file_type`: Prints the type of the file named `iamafile` located in the `/tmp` directory.
- `13-symbolic_link`: Creates a symbolic link to `/bin/ls`, named `__ls__`.
- `14-copy_html`: Copies all the HTML files from the current directory to the parent of the working directory, but only copies files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

### Advanced

- `100-lets_move`: Moves all files beginning with an uppercase letter to the directory `/tmp/u`.
- `101-clean_emacs`: Deletes all files in the current working directory that end with the character `~`.
- `102-tree`: Creates the directories `welcome/`, `welcome/to/`, and `welcome/to/holberton` all at once.
- `103-commas`: Executes the `ls -map` command, which lists the directory contents in a format that appends indicators to entries and separates them with commas.

## Author

Chris Stamper - [ZeroDayPoke](https://github.com/ZeroDayPoke)
