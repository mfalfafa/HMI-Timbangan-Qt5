> Note

To omit Raspi 3 logo at booting:
```
add logo.nologo to /boot/cmdline.txt
```

To disable splash screen on booting:
```
add disable_splash=1 to /boot/config.txt
```

To disable boot messages:
```
remove console=tty1 to /boot/cmdline.txt
```

> References (customize Raspbian Jessie)

1. https://scribles.net/customizing-boot-up-screen-on-raspberry-pi/
2. https://thepihut.com/blogs/raspberry-pi-tutorials/19668676-renaming-your-raspberry-pi-the-hostname
3. https://raspberrypi.stackexchange.com/questions/12827/change-default-username
4. https://raspberrypi.stackexchange.com/questions/7133/how-to-change-user-pi-sudo-permissions-how-to-add-other-accounts-with-different