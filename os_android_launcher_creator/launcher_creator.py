from os_android_launcher_creator.bp import _launcher_creator as lc
from os_android_launcher_creator.bp import _vector_creator as vc
from typing import Callable, Any, Iterable
from os_android_launcher_creator.LauncherObj import ImgObj

from typing import List

######################################################################
# This module aim is to create a launcher icon for a given app using #
# Android Studio automation                                          #
######################################################################

screen_width = False
screen_height = False


def create_launcher_icons(custom_android_project_path,
                          img_obj_list: list[ImgObj],
                          shortcut_keys_to_open_image_asset=list['shift', 'b'],
                          launcher_resize_percent=50,
                          launcher_background_color_hex='#ffffff',
                          skip_if_output_dir_exists=True):
    """
    Will create a launcher icons from a given icon
    NOTICE: the automation need to run in an open project in Android Studio so make sure you open one to work on!

    Args:
        custom_android_project_path: the current open Android Studio project
        img_obj_list: a list containing the ImgObj. Every ImgObj contains the path to the launcher and and a path to the destination files to be copied
        shortcut_keys_to_open_image_asset: the list of buttons to hold together in order to open the Image Asset in Android Studio
        launcher_resize_percent: the resize percents of the icon to fit the frame in the editor
        launcher_background_color_hex: the color of the background of the icons
        skip_if_output_dir_exists: if set to True, when the algorithm will find that the output dir already exists it will skip the launcher creation of the current iteration
    """
    inst = lc.LauncherCreatorBP(custom_android_project_path, img_obj_list, shortcut_keys_to_open_image_asset, launcher_resize_percent, launcher_background_color_hex, skip_if_output_dir_exists)
    inst.create_launcher_icons()


def create_vector_icons(custom_android_project_path,
                          launcher_obj_list: list[ImgObj],
                          shortcut_keys_to_open_vector_asset=list['shift', 'l']):
    """
    Will create a vector icons from a given icon
    NOTICE: the automation need to run in an open project in Android Studio so make sure you open one to work on!

    Args:
        custom_android_project_path: the current open Android Studio project
        launcher_obj_list: a list containing the ImgObj. Every ImgObj contains the path to the launcher and and a path to the destination files to be copied
        shortcut_keys_to_open_image_asset: the list of buttons to hold together in order to open the Image Asset in Android Studio
        launcher_resize_percent: the resize percents of the icon to fit the frame in the editor
        launcher_background_color_hex: the color of the background of the icons
        skip_if_output_dir_exists: if set to True, when the algorithm will find that the output dir already exists it will skip the launcher creation of the current iteration
    """
    inst = vc.VectorCreatorBP(custom_android_project_path, launcher_obj_list, shortcut_keys_to_open_image_asset, launcher_resize_percent, launcher_background_color_hex, skip_if_output_dir_exists)
    inst.create_vector_assets()
