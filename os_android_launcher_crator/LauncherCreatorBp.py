import os
import os_tools.LoggerHandler as lh
import os_tools.Tools as tools
import os_tools.FileHandler as fh
import time
import pyautogui


##################################################################################
#
# just a bp for the launcher creator
#
##################################################################################


def select_all():
    from sys import platform
    if platform == "darwin":
        hot_key(['command', 'a'])
    else:
        hot_key(['ctrl', 'a'])


def hot_key(btn_list):
    pyautogui.keyDown(btn_list[0])

    time.sleep(1)
    for i in range(1, len(btn_list)):
        print("down" + btn_list[i])
        pyautogui.keyDown(btn_list[i])

    time.sleep(1)
    for i in range(1, len(btn_list)):
        print("up" + btn_list[i])
        pyautogui.keyUp(btn_list[i])

    time.sleep(1)
    pyautogui.keyUp(btn_list[0])


class LauncherCreatorBP:
    STATIC_MAIN_RELATIVE_PATH = 'app/src'
    SECS_COOLDOWN_UNTIL_PROJECT_OPEN = 4

    def __init__(self, custom_android_project_path, icon_files_list, shortcut_keys_to_open_image_asset, launcher_resize_percent, launcher_background_color_hex):
        self.custom_android_project_path = custom_android_project_path
        self.custom_android_project_path = custom_android_project_path
        self.icon_files_list = icon_files_list
        self.shortcut_keys_to_open_image_asset = shortcut_keys_to_open_image_asset
        self.launcher_resize_percent = launcher_resize_percent
        self.launcher_background_color_hex = launcher_background_color_hex
        self.logger = lh.Logger(__file__)  # build the logger
        self.main_path = os.path.join(custom_android_project_path, self.STATIC_MAIN_RELATIVE_PATH)

    def create_launcher_icons(self):

        self.logger.info('-------------------------------')
        self.logger.info(f'Preparing to work on {str(len(self.icon_files_list))} icons')
        time.sleep(1)
        tools.ask_for_input('Please open your custom project in Android Studio and inform me when you are done [done]')

        self.logger.info(f'Now go back to the project and wait {str(self.SECS_COOLDOWN_UNTIL_PROJECT_OPEN)} seconds...')
        time.sleep(self.SECS_COOLDOWN_UNTIL_PROJECT_OPEN)

        for icon_file in self.icon_files_list:
            self.logger.info('-----------------------------------------')
            self.logger.info(f'working on: {fh.get_file_name_from_path(icon_file, False)}')
            self.run_cycle(icon_file)
            self.logger.info('done!')

    def run_cycle(self, icon_file):

        self.clear_old_launcher_files()

        self.logger.info('old files removed. waiting a few seconds for the system to update itself')
        time.sleep(2)
        self.logger.info('open icon creator')
        for key in self.shortcut_keys_to_open_image_asset:
            pyautogui.keyDown(key)

        time.sleep(1)
        for key in self.shortcut_keys_to_open_image_asset:
            pyautogui.keyUp(key)

        self.logger.info('go to path')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')

        self.logger.info('paste path')
        time.sleep(1)
        select_all()
        pyautogui.write(icon_file)

        self.logger.info('disabling trim')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('space')

        self.logger.info('setting resize')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('left', presses=100, interval=0)
        pyautogui.press('right', presses=self.launcher_resize_percent, interval=0)

        time.sleep(1)
        self.logger.info('navigate to background')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('right')

        time.sleep(1)

        self.logger.info('setting background color')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('space')

        self.logger.info('clicking and setting color')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('space')
        color = self.launcher_background_color_hex.replace('#', '')
        select_all()
        pyautogui.write(color)
        time.sleep(2)
        pyautogui.press('enter')

        self.logger.info('clicking next')
        pyautogui.press('enter')

        time.sleep(1)
        self.logger.info('clicking finish')
        pyautogui.press('enter')

        self.logger.info('gathering files...')
        time.sleep(8)
        launcher_made_files = fh.search_files(self.main_path, None, 'ic_launcher')

        # copy all of the icon files to the path, ony by one
        icon_parent_dir = fh.get_parent_path(icon_file)
        icon_file_name_no_ext = fh.get_file_name_from_path(icon_file, False)
        output_main_dir = os.path.join(icon_parent_dir, icon_file_name_no_ext)
        if fh.is_dir_exists(output_main_dir):
            file_over_write_extension = fh.get_extension_from_file(icon_file).replace('.', '_')
            icon_file_name_no_ext += file_over_write_extension
            output_main_dir = os.path.join(icon_parent_dir, icon_file_name_no_ext)
            self.logger.warning(f"icon file with the name '{icon_file_name_no_ext}' already exists. Creating a unique directory: {output_main_dir} to prevent overwrite!")
        fh.create_dir(output_main_dir)

        self.logger.info('saving files...')
        for launcher_file in launcher_made_files:
            curr_launcher_dir = fh.get_parent_path(launcher_file)
            src_idx = curr_launcher_dir.find('src/')
            curr_launcher_dir = curr_launcher_dir[src_idx + 4:]
            curr_launcher_dir_path = os.path.join(icon_parent_dir, icon_file_name_no_ext, curr_launcher_dir)
            fh.create_dir(curr_launcher_dir_path)
            launcher_file_name_with_ext = fh.get_file_name_from_path(launcher_file)
            icon_file_dst = os.path.join(curr_launcher_dir_path, launcher_file_name_with_ext)
            fh.copy_file(launcher_file, icon_file_dst)

        self.logger.info('waiting for next cycle...')
        time.sleep(1.5)

    def clear_old_launcher_files(self):
        self.logger.info('removing all old launcher made files...')
        launcher_made_files = fh.search_files(self.main_path, None, 'ic_launcher')
        fh.remove_files(launcher_made_files)
