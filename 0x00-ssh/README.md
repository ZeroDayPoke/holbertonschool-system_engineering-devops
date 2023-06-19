# 0x00. SSH

This project is part of the Holberton School curriculum. In this project, you will learn about SSH, how to use it to connect to remote servers, and how to configure it.

## Synopsis

This project covers:

- What is a server
- Where servers usually live
- What is SSH
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`

## File Descriptions

- [`0-use_a_private_key`](https://github.com/ZeroDayPoke/holbertonschool-system_engineering-devops/blob/master/0x00-ssh/0-use_a_private_key): Bash script that uses ssh to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.
- [`1-create_ssh_key_pair`](https://github.com/ZeroDayPoke/holbertonschool-system_engineering-devops/blob/master/0x00-ssh/1-create_ssh_key_pair): Bash script that creates an RSA key pair named `school` with the passphrase `betty`.
- [`2-ssh_config`](https://github.com/ZeroDayPoke/holbertonschool-system_engineering-devops/blob/master/0x00-ssh/2-ssh_config): File that contains the configuration for an SSH connection to the host `5580-web-01` using the username `ubuntu` and the identity file `~/.ssh/school`.

## Author

Chris Stamper - [ZeroDayPoke](https://github.com/ZeroDayPoke)
