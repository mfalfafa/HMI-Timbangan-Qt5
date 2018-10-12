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