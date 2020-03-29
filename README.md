Introduction
------------

This module will create an app launcher (logo) using Android Studio in all sizes and shapes (web, round) and in all dpis (mipmap-anydpi-v26, mipmap-hdpi, mipmap-mdpi, mipmap-xhdpi, mipmap-xxhdpi, mipmap-xxxhdpi, values).

Notice: you need to use the tools of Android Studio to make it work. I recommend to create a sample project and run on it.

## Installation
Install via pip:

    pip install os-android-launcher-creator

## Quick Usage       
From Python:
    
    import os_android_launcher_creator.LauncherCreator as lc
    
    lc.create_launcher_icons(custom_android_project_path='/Users/home/Programming/android/sample_project',
                             icon_files_list=['path/to/first/icon1.svg', 'path/to/second/icon2.svg'],
                             shortcut_keys_to_open_image_asset=['shift', 'b'],
                             launcher_resize_percent=50,
                             launcher_background_color_hex='#ffffff')
  
## Functions and Signatures
    def create_launcher_icons(custom_android_project_path, icon_files_list, shortcut_keys_to_open_image_asset,  launcher_resize_percent=50, launcher_background_color_hex='#ffffff'):
        """
        Will create a launcher icon from a given icon
        NOTICE: the automation need to run in an open project in Android Studio so make sure you open one to work on!
    
        Args:
            custom_android_project_path: the current open Android Studio project
            icon_files_list: a list of all of the icons you wish to turn on to launcher icons
            shortcut_keys_to_open_image_asset: the list of buttons to hold together in order to open the Image Asset in Android Studio
            launcher_resize_percent: the resize percents of the icon to fit the frame in the editor
            launcher_background_color_hex: the color of the background of the icons
        """

![output](/images/sample.png)
## Licence
MIT