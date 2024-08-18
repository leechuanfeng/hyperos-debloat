# Xiaomi HyperOS Debloat List (JUL 2024)
If you're frustrated with the pre-installed applications on your new phone, you're not alone. Many of these apps can be redundant or intrusive, often causing issues such as push notifications and excessive battery drain.

By using ADB (Android Debug Bridge), you can safely remove these unwanted applications without the need for rooting. This method is less risky than manual removal and ensures that system variables remain intact, allowing you to continue receiving OTA updates without issues.

This script is designed to help Xiaomi phone users remove unnecessary pre-installed applications and bloatware from their devices. 
By running this script, you can declutter your phone, improve performance, and free up storage space.

**DISCLAIMER: Use at your own risk. I am not responsible for anything that could happen to your phone. It is highly recommended to use it on a new phone or on a clean state after your phone is reset.**

## Debloat List (HyperOS 1.0.7.0.UNAMIXM)
This list is curated and tested for **HyperOS 1.0.7.0.UNAMIXM**
- Xiaomi 14 Ultra Global Edition
- Redmi Note 13 Pro+ 5G

# Setting Up
## Download Python
Install python on your computer from https://www.python.org/downloads/

## Download ADB (Android Debug Bridge)
Download the platform-tools for ADB
https://developer.android.com/tools/releases/platform-tools

Unzip the folder into this project.

## Steps to Enable Developer Mode on HyperOS
Steps are to be done on your phone.

1. Open Settings.
2. Tap on About phone.
3. Tap on OS version multiple times until Developer Mode is enabled.
4. Go back to Settings, then select Additional settings.
5. Tap on Developer options and toggle it on.
6. Scroll down and find USB debugging, then toggle it on to enable USB Debugging.
7. Check the instructions and click OK.

If unsure, please follow some youtube video.

## Verify Device Is Connected
Use a compatible USB cable to connect your phone to a USB port on your computer. If this is the first time connecting your phone to this computer, you may see a prompt on your phone asking you to authorize the connection. Tap Allow or OK to grant permission.

To verify if your device is properly connected and recognized by ADB (Android Debug Bridge), open Command Prompt or Terminal on your computer,
enter the following and you should be able to see a similar output:
```
./platform-tools/adb devices

List of devices attached
12345abc        device
```

# Debloating
## Generate List of App On Phone
Run the command to get the list of apps on your phone
```
./platform-tools/adb shell pm list packages > app.txt
```

## Custom Debloat List
To customize the list of apps to be removed, you can add the apps into the `debloat_list/donotuninstall.txt`. 


## Generate List of App to Uninstall
Run the script to get the list of app to uninstall
```
python main.py
```

Two list will be generated, one will `uninstall_list.txt` the apps that will be uninstalled and `remaining_list.txt` will be the remaining apps.

## Uninstalling of Apps
On Window:
Rename uninstall_list.txt to uninstall_list.bat, run the uninstall_list.bat file
```
./uninstall_list.bat
```


On Linux 
Rename uninstall_list.txt to uninstall_list.sh, run the uninstall_list.sh file
```
./uninstall_list.sh
```

Otherwise you can run the uninstall command individually in the `uninstall_list.txt`.

# Reference
The debloat list is taken from \
https://github.com/0x192/universal-android-debloater/blob/main/resources/assets/uad_lists.json