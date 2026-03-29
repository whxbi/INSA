----------------------------------------------------------------------------------------
**week #2 Saturday 21 MAY 2026**

systemfiles is basically a file in an operating sysytem that makes everything works
### /root
the file that contains every file in an OS
### /bin
binary execlusive, contains commmands to use 
### /boot
connects to your OS
### /dev
has the hardwares scripts like terminal devices, usb ...
### /etc 
contains conf files of all yor programs, and startup or shutdown scripts 
### /home
where the users files are
### ./lib
contains libraries essential to the binary like firmwares 
### /media
mount points for. where temporary files are at, like flashs or usb, after we unmount the usb the system made a dir for it so it is temporary 
### /mnt 
temporary mount directory where sysadmins can mount 
we do this because if not mounted and the pc was shutdown all the files in the usb will be deleted
### /opt
optional applicatons pkgs

## Research quiz

## Linux user manangment
basically it is an task where it tells who can access or control the system asd it also makes sure which user has the appropriate priveleges 
### root
the root user has full permision to do, read, execute, remove, change, basically anything in the system. the root can also add as many users and he can assign different permision to the users in the system for example to enable a user to use sudo bin the `visudo` conf and uncommenting wheel
### user
the user is the one who is added by the root and can use the OS, the user initially has minumal acccess to the root 
### sudo
since the user has no full access and sometimes to install a package through terminal he needs the permission from the root, that's what sudo is for, it acts a root while still in the users session, in oreder to use sudo the user has to insert the root's password after prompted to

## Package installation
if a users wants to install a program or an app, linux has an official place to install them same as the microsoft store, it differs from distro to distro, for example in the ARCH distro the official pkgs installation command is `sudo -S pacman` what makes ARCH unique is that it hasd multiple pkg installers if the disired pkg isn't in the official package manager, which is the Arch User Repositories(AUR), to install pkgs from the AUR a differnet command is used, like `yay` 
other distros pkgs can be accessed by `apt` (for Debian based distors) and `pkg` (for FreeBSD)

## Script installation
scripts are text files that contain a code or a command, ends with .py or .sh can be installed or executed
to install a script we  `bash ./install.sh` or if it was a language based prog `python3 install.py` but if the user has no permission to exedcute the script we `sudo chmod +x install.sh` to give the user the permision

## software
software are basically the apps we use like browsers or editing apps or games which can be install from the pkg manager the distro's store (Store center for ARCH) 

## shell
the place where your code can be written and get interpreted or translated and even executed
for example when we run `ls` or `cat` bash (or other shells) is what gives this code meaning and runs it

## ping and or
`|` append

----------------------------------------------------------------------------------------

**week #2 Sunday 22 MAY 2026**

## LAN 
- work son limited are
- doesn't require network, it can work with hotsspot
- can be used by maximum 253 
## PAN
- more of personal on local device like shareit
## MAN 
- covers cities
## WAN | Internet
- long distance communication
## IP

# class
 - **class a**: the network holds 24 bits and the host holds 8 bits
  - the first block holds from 1-127 and the rest blocks holds 255
 - **class b**:  128-191, the network and hosts holds 16 bit
 - **class c**: 192-223, the network/host holds 24/8 bits,
 - **class d**: 224-239, 32

## excercise
- 0.0.0.0 special
- 127.0.0.0 class a
- 128.0.0.0 class b
- 192.0.0.0 class c
- 191.225.0.0 special
- 223.225.225.0 class c
- 225.225.0.0 special
- 192.127.32.0 class c
- 10.1.1.1 special
- 192,168,1,1 class c

# OSI 
- it's a mental framework that understands how data moves accross a network, from a device to another
  ## Layer 1 Physical 
  - it takes raw bits to the physical device
  - wifi and bluetooth cars and be a good example as the proccess binary values and sends it to the air or a device
  - `ip link shsow` 
  ## Layer 2 Data Link 
  - handles comms b/n devices on the same network
  - when laptop connects to the router, the 2 layeer makes sure the right data reaches the laptop
  - tools: `ip addr show` `sudo tcpdump -i wlan0 -e` 
  ## Layer 3 Network
  - getting data from devices across different nerworks, so not locally like layer 2
  - or basically getting the data from your network to the server you're searching for
  - tools: `ip route show` `ping` `traceroute`
  ## Layer 4 Transport
  - makes sure the data arrives accuratley and in order by using key protocols (set of rules that a device follow to communicate)
  - **TCP**: guaranteis all data sent arrives at teh other side in correct oreder
  - prevents sender from overwhelming the receiver
  - used in web browsing, emails, file transfers
  - **UDP**: sends data without establishing any session
  - packets may be not in order and also can be duplicated, but it's very fast
  - **Port**: it acts like a guard opening the right door for guests and cautiosly in order attackers to not exploit
  - youtubes port is 443,80 which is a port to view and watch only
  - port 22 is for SSH
  - 587 is for smtp
  - FTP is on port 20 and 21
  - 23 is for telnet
  - there are 30 top ports
  - tools: `nc` , `nmap`
  ## Layer 5 Session
  - establish presistent connections like SSH, telnet, FTP
  - can be used for remote login, video calls, db sessions.
  - tools: `ssh` , `telnet`
  ## Layer 6 present
  -
  ## Layer 7 Application
  -

**ARP protocol**
  ## MAC address
 - the first 3 pairs are reseerved for the company manufacture and the other 3 pairs are unique ID for the device
--------------------------------------------------------------------------------------------------
