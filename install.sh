#!/bin/bash

# check if the current user is root
if [[ $(sudo whoami) != "root" ]];then
    echo -e "Looks like the current user '$(whoami)' is either a 'non-root' user or is not a 'sudoer'.\nPlease switch to 'root' or grant this user 'sudo' privileges.\nExiting....\n"
    exit
fi
