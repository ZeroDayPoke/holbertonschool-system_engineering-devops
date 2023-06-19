# 0x01. Shell, permissions

This project is part of the Holberton School curriculum. In this project, you will learn about shell permissions, how to change them, and how to manage users and groups.

## Synopsis

This project covers:

- What do the commands `chmod`, `sudo`, `su`, `chown`, `chgrp`, `id`, `groups`, `whoami`, `adduser`, `useradd`, and `addgroup` do
- Linux file permissions
- How to represent each of the three sets of permissions (owner, group, and other) as a single digit
- How to change permissions, owner and group of a file
- Why can't a normal user `chown` a file
- How to run a command with root privileges
- How to change user ID or become superuser

## File Descriptions

### Mandatory

- `0-iam_betty`: Script that switches the current user to the user `betty`.
- `1-who_am_i`: Script that prints the effective username of the current user.
- `2-groups`: Script that prints all the groups the current user is part of.
- `3-new_owner`: Script that changes the owner of the file `hello` to the user `betty`.
- `4-empty`: Script that creates an empty file called `hello`.
- `5-execute`: Script that adds execute permission to the owner of the file `hello`.
- `6-multiple_permissions`: Script that adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.
- `7-everybody`: Script that adds execution permission to the owner, the group owner and the other users, to the file `hello`
- `8-James_Bond`: Script that sets the permission to the file `hello` as follows:
- `9-John_Doe`: Script that sets the mode of the file `hello` to `-rwxr-x-wx`.
- `10-mirror_permissions`: Script that sets the mode of the file `hello` the same as `olleh`’s mode.
- `11-directories_permissions`: Script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
- `12-directory_permissions`: Script that createsa directory called `dir_holberton` with permissions 751 in the working directory.
- `13-change_group`: Script that changes the group owner to `holberton` for the file `hello`.
- `14-change_owner_and_group`: Script that changes the owner to `betty` and the group owner to `holberton` for all the files and directories in the working directory.
- `15-symbolic_link_permissions`: Script that changes the owner and the group owner of the file `_hello` to `vicent` and `staff` respectively.
- `16-if_only`: Script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.

### Advanced

- [`100-change_owner_and_group`](https://github.com/ZeroDayPoke/holbertonschool-system_engineering-devops/blob/master/0x01-shell_permissions/100-change_owner_and_group): A script that changes the owner and group owner of the file `_hello` to `vincent` and `staff` respectively.
- [`101-symbolic_link_permissions`](https://github.com/ZeroDayPoke/holbertonschool-system_engineering-devops/blob/master/0x01-shell_permissions/101-symbolic_link_permissions): A script that changes the owner and group owner of the symbolic link `_hello` to `vincent` and `staff` respectively.
- [`102-if_only`](https://github.com/ZeroDayPoke/holbertonschool-system_engineering-devops/blob/master/0x01-shell_permissions/102-if_only): A script that changes the owner of the file `hello` to `vincent` only if it is owned by the user `guillaume`.
- [`103-Star_Wars`](https://github.com/ZeroDayPoke/holbertonschool-system_engineering-devops/blob/master/0x01-shell_permissions/103-Star_Wars): A script that will play the StarWars IV episode in the terminal.

## Author

Chris Stamper - [ZeroDayPoke](https://github.com/ZeroDayPoke)
