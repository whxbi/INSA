# Linux & Cybersecurity introduction
> Saturday, March 7, 2026

- everything in Linux is basicaly a file and a directory
- **Pentest**: we test and check everything to the limit of what we are allowed to
- **Red-team**: full attack to check the target's vulnerability's


## Linux Directory's
| Directory | Description |
|-----------|-------------|
| `/` | Root — the top of the entire filesystem |
| `/bin` | Essential user binaries (e.g., `ls`, `cp`, `cat`) |
| `/sbin` | System binaries — used by admins (e.g., `reboot`, `ifconfig`) |
| `/boot` | Bootloader and kernel files (GRUB lives here) |
| `/dev` | Device files — hardware is represented as files here |
| `/etc` | System-wide configuration files |
| `/home` | Personal directories for each user |
| `/lib` | Shared libraries needed by `/bin` and `/sbin` |
| `/media` | Auto-mount point for removable drives (USB, CD) |
| `/mnt` | Temporary manual mount point |
| `/opt` | Optional/third-party software packages |
| `/tmp` | Temporary files — cleared on reboot |
| `/usr` | User utilities, applications, and secondary hierarchy |
| `/var` | Variable data — logs, databases, mail spools |
| `/var/log` | System and application logs |
| `/root` | Home directory for the root superuser |

## Red vs Blue focus
| Directory | Team | Why |
|-----------|------|-----|
| `/var/log` | 🔵 Blue | Monitor for intrusion attempts and anomalies |
| `/etc` | 🔵 Blue | Watch for unauthorized config changes |
| `/etc/shadow` | 🔵 Blue | Contains hashed passwords — must be protected |
| `/tmp` | 🔴 Red | World-writable, perfect for dropping malicious scripts |
| `/home` | 🔴 Red | Primary target for user data exfiltration |
| `/root` | 🔴 Red | Achieving access here = full system compromise |

# Linux Operations & File Permissions
> Sunday, March 8, 2026

## Linux File Permissions
 | Permissions   | Octal(numeric)   | Letters(Symbolic)   |
 | :-----------: | :-----: | :-------: |
 | no permission |    0    |   ---     |
 | Execute       |    1    |   --x     |
 | Write         |    2    |   -w-     | 
 | Write+Execute |    3    |   -wx     |
 | Read          |    4    |   r--     |
 | Read+Execute  |    5    |   r-x     | 
 | Read+Write    |    6    |   rw-     | 
 | Read+Write+Execute|    7    |   rwx     |

 ### Useful sources
> https://overthewire.org/wargames/bandit/
