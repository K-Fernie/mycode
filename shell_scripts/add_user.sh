#!/bin/bash

#Gathering information from the user for the user, password and group
echo "Please enter the name of the user to add" 
read USER

echo "Please enter the group name" 
read GROUP

echo "Please enter the password"
read PASSWORD

#Adding the new user
sudo useradd -m -p $PASSWORD $USER

#Letting the user know that the user add was successful
echo "$USER was added" 

#Checking that the group already exists in the system
if grep -q $GROUP /etc/group; 
then
    echo "Group Exists adding user to existing group"
else
    sudo groupadd $GROUP
fi

#Add the new user to the specified group
sudo usermod -aG $GROUP $USER

#Let the user know that the script was successful
echo "$USER was added to $GROUP"



