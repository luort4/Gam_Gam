# Gam_Gam
Utilization of Gam Scripts for automation

# Installation
Gam_Gam runs on Python3 and requires certain Libraries to be installed. To install the needed Python Libraries run the command:

`pip3 -r install requirements.txt`

Gam will also be required, specifically GAMADV-XTD3. This has been tested with version 6.22.10.
Gam will also require the use of API keys and updated Super Admin permissions to utilize the commandline interface. For more information please refer to this installation guide (Video also included in Article): https://taming.tech/installing-gamadv-xtd3-on-macos/

# Initial Setup

In the `groups_google.py` script, the varible `which_gam` needs to be given the binary location of wherever gam may lie in. 

This can be found running a `which gam` command in the terminal, and then copying and pasting into the variable location.

# How to use

To onboard groups and set aliases for the users the flag of `execute` or `exec` would need to be used to allow the python script to execute. If you run without these flags, they will instead print the Gam commands that are loaded for that user.

# Examples

**```python groups_google.py```**  <-- this will show the Gam commands that are loaded for the users

**```python groups_google.py execute```** <-- this will execute the commmands, can also use `exec`

<!--- YnVnZ3k0Mg== --->
