import os
import os_tools.logger_handler as lh
import os_tools.tools as tools
import os_tools.file_handler as fh
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
        pyautogui.keyDown(btn_list[i])

    time.sleep(1)
    for i in range(1, len(btn_list)):
        pyautogui.keyUp(btn_list[i])

    time.sleep(1)
    pyautogui.keyUp(btn_list[0])


class LauncherCreatorBP:
    STATIC_MAIN_RELATIVE_PATH = 'app/src'
    SECS_COOLDOWN_UNTIL_PROJECT_OPEN = 4

    def __init__(self, custom_android_project_path, icon_files_list, output_path, shortcut_keys_to_open_image_asset, launcher_resize_percent, launcher_background_color_hex, delete_icon_after_done):
        self.custom_android_project_path = custom_android_project_path
        self.custom_android_project_path = custom_android_project_path
        self.icon_files_list = icon_files_list
        self.output_path = output_path
        self.shortcut_keys_to_open_image_asset = shortcut_keys_to_open_image_asset
        self.launcher_resize_percent = launcher_resize_percent
        self.launcher_background_color_hex = launcher_background_color_hex
        self.logger = lh.Logger(__file__)  # build the logger
        self.main_path = os.path.join(custom_android_project_path, self.STATIC_MAIN_RELATIVE_PATH)
        self.delete_icon_after_done = delete_icon_after_done

    def create_launcher_icons(self):

        self.logger.info('-------------------------------')
        self.logger.info(f'Preparing to work on {str(len(self.icon_files_list))} icons')
        time.sleep(1)
        tools.ask_for_input('Please open your custom project in Android Studio and inform me when you are done [done]')

        self.logger.info(f'Now go back to the project and wait {str(self.SECS_COOLDOWN_UNTIL_PROJECT_OPEN)} seconds...')
        time.sleep(self.SECS_COOLDOWN_UNTIL_PROJECT_OPEN)

        for i in range(0, len(self.icon_files_list)):
            self.logger.info('-----------------------------------------')
            self.logger.info(f'working on: {fh.get_file_name_from_path(self.icon_files_list[i], False)}')
            res = self.run_cycle(self.icon_files_list[i])
            if res:
                self.logger.info('done!')
            else:
                tools.ask_for_input("ERROR: It seems like the process failed for " + self.icon_files_list[i] + ". Let me know when you are ready to run on the same file [Enter]")
                i -= 1

    def run_cycle(self, icon_file):

        self.clear_old_launcher_files()

        self.logger.info('old files removed. waiting a few seconds for the system to update itself')
        time.sleep(2)

        # open image assets
        hot_key(self.shortcut_keys_to_open_image_asset)

        time.sleep(1)
        # navigate to path
        self.logger.info('go to path')
        pyautogui.press('tab', 7, 0.1)

        self.logger.info('paste path')
        time.sleep(1)
        select_all()
        pyautogui.write(icon_file, interval=0.1)

        self.logger.info('disabling trim')
        pyautogui.press('tab', 3, 0.1)
        pyautogui.press('space')

        self.logger.info('setting resize')
        pyautogui.press('tab', 2, 0.1)
        pyautogui.press('left', presses=100, interval=0)
        pyautogui.press('right', presses=self.launcher_resize_percent, interval=0)

        time.sleep(1)
        self.logger.info('navigate to background')
        pyautogui.press('tab', 9, 0.1)
        pyautogui.press('right')

        time.sleep(1)

        self.logger.info('setting background color')
        pyautogui.press('tab', 3, 0.1)
        pyautogui.press('space')

        self.logger.info('clicking and setting color')
        pyautogui.press('tab', 3, 0.1)
        pyautogui.press('space')
        color = self.launcher_background_color_hex.replace('#', '')
        select_all()
        pyautogui.write(color, interval=0.1)
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
        fh.create_dir(self.output_path)

        # copy all of the icon files to the path, ony by one
        icon_file_name_no_ext = fh.get_file_name_from_path(icon_file, False)
        output_main_dir = os.path.join(self.output_path, icon_file_name_no_ext)
        if fh.is_dir_exists(output_main_dir):
            file_over_write_extension = fh.get_extension_from_file(icon_file).replace('.', '_')
            icon_file_name_no_ext += file_over_write_extension
            output_main_dir = os.path.join(self.output_path, icon_file_name_no_ext)
            self.logger.warning(f"icon file with the name '{icon_file_name_no_ext}' already exists. Creating a unique directory: {output_main_dir} to prevent overwrite!")
        fh.create_dir(output_main_dir)

        # if no launcher made files, it means that for some reason the process failed
        if not launcher_made_files:
            return False

        self.logger.info('saving files...')
        for launcher_file in launcher_made_files:
            curr_launcher_dir = fh.get_parent_path(launcher_file)
            src_idx = curr_launcher_dir.find('src/')
            curr_launcher_dir = curr_launcher_dir[src_idx + 4:]
            curr_launcher_dir_path = os.path.join(self.output_path, icon_file_name_no_ext, curr_launcher_dir)
            fh.create_dir(curr_launcher_dir_path)
            launcher_file_name_with_ext = fh.get_file_name_from_path(launcher_file)
            icon_file_dst = os.path.join(curr_launcher_dir_path, launcher_file_name_with_ext)
            fh.copy_file(launcher_file, icon_file_dst)

        if self.delete_icon_after_done:
            fh.remove_file(icon_file)
        self.logger.info('waiting for next cycle...')
        time.sleep(1.5)
        return True

    def clear_old_launcher_files(self):
        self.logger.info('removing all old launcher made files...')
        launcher_made_files = fh.search_files(self.main_path, None, 'ic_launcher')
        fh.remove_files(launcher_made_files)
