**week #2,  Saturday 21 MAR 2026**
## Task #1
 Q1: First we need to know which numbers corrispond to which permision
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
 
 then from this we can #`sudo chmod 640 file` 
 
 Q2: #`sudo chmod 755 file`

 Q3: #`sudo chmod 664`

 Q4: `640`

 Q5: the file can't be accesable anymore, has the permissions has been locked even for the root, so no he can't cat it but the root can still change the file's permissions to enable read,write,and exec again

 Q6: #`touch Audit.txt && sudo chmod 750`

 Q7: As shown above in the table, `741` = `rwxr----x`

 Q8: `500` = `r-x`

 Q9: `r-xrw-r--` = `564`

 ## Task #2
 - FLAG_1: i extracted the metadata by using `exiftool` or `exiftool challenge.jpg` and found this under comment `Comment                         : FLAG{ALWAYS_Check_Metadata}`
 ![Alt img](/home/whxbi/Pictures/Screenshots/Screenshot_20260322_101130.png)
 - FLAG_2: i used `strings` or `strings challenge.jpg`to find any readable text in that noise and found `FLAG{Strings_leak_information}`
 ![Alt text](/home/whxbi/Pictures/Screenshots/Screenshot_20260322_101130.png)
 - FLAG_3: i wanted to check if there was any hidden files insides the img so i used `binwalk` or `binwalk -e challenge` where `-e` extracts any hidden file, and i found a hidden zip and extracted it, when `cd` to the extraction there's a file numbered `12793`, again when `cd` to it we find a file named `flag4.txt` and when `cat` this base64 format appears `Umt4QlIzdGhjSEJsYm1SbFpGOTZhWEI5Q2c9PQo=` and when decoded with `echo "Umt4QlIzdGhjSEJsYm1SbFpGOTZhWEI5Q2c9PQo=" | base64 -d` another base46 format appears `RkxBR3thcHBlbmRlZF96aXB9Cg==` when decoded `echo "RkxBR3thcHBlbmRlZF96aXB9Cg==" | base64 -d` the flag shows app `FLAG{appended_zip}`
 ![Alt text](/home/whxbi/Pictures/Screenshots/Screenshot_20260322_101210.png)
 - FLAG_4: i wanted to check the `steghide` and it asked for the passphrase so i knew i had to use `stegseek` to brute force the password so i used `stegseek challenge.jpg weakpass_4.txt` weakpass is basically a file the contains a lot of password combinations and stegseek is using it to crack the password of challenge.jpg, after stegseek finished the passsphrase was `password123` and it auto created a file that extracted the flag5 from the steghide using the passphrase, and the file contained: `FLAG{steghide_protected}`
 ![Alt text](/home/whxbi/Pictures/Screenshots/Screenshot_20260322_101301.png)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
