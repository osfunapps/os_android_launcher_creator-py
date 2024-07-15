import os
import os_tools.logger_handler as lh
import os_tools.tools as tools
import os_file_handler.file_handler as fh
import time
from os_btns_automation import btns_automation
from os_android_launcher_creator.LauncherObj import ImgObj
from os_file_stream_handler import file_stream_handler as fsh


######################################
# just a bp for the launcher creator #
######################################

class VectorCreatorBP:
    STATIC_MAIN_RELATIVE_PATH = os.path.join('app', 'src')
    SECS_COOLDOWN_UNTIL_PROJECT_OPEN = 4
    LOGGER_TAG = '[Vector Creator]'

    def __init__(self, custom_android_project_path, img_obj_list: list[ImgObj], shortcut_keys_to_open_vector_asset):
        self.logger = lh.Logger(name=self.LOGGER_TAG)  # build the logger
        self.custom_android_project_path = custom_android_project_path
        self.img_obj_list = img_obj_list
        self.shortcut_keys_to_open_vector_asset = shortcut_keys_to_open_vector_asset
        self.main_path = os.path.join(custom_android_project_path, self.STATIC_MAIN_RELATIVE_PATH)

    def create_vector_assets(self):
        self.print_ln()
        self.logger.info(f'Preparing to work on {str(len(self.img_obj_list))} icons')
        time.sleep(1)
        tools.ask_for_input('Please open your custom project in Android Studio and inform me when you are done [done]')

        self.logger.info(f'Now go back to the project and wait {str(self.SECS_COOLDOWN_UNTIL_PROJECT_OPEN)} seconds...')
        time.sleep(self.SECS_COOLDOWN_UNTIL_PROJECT_OPEN)

        for i in range(0, len(self.img_obj_list)):
            curr_vector_obj = self.img_obj_list[i]
            self.print_ln()
            name = fh.get_dir_name(fh.get_parent_path(curr_vector_obj.icon_path))
            self.logger.info(f'Working on: "{name}"...')

            # run current launcher
            res = self.run_cycle(self.img_obj_list[i])

            # do something with the response
            if res:
                self.logger.info(f'Launcher {name} done!')
            else:
                tools.ask_for_input("ERROR: It seems like the process failed for " + self.launcher_obj_list[i].icon_path + ". Let me know when you are ready to run on the same file [Enter]")
                i -= 1

        self.print_ln()

    def run_cycle(self, img_obj: ImgObj):

        out_file_name = fh.get_file_name_from_path(img_obj.output_path)

        # open vector assets
        btns_automation.hot_key(self.shortcut_keys_to_open_vector_asset)

        time.sleep(1)

        btns_automation.select_all()
        btns_automation.paste()

        time.sleep(0.5)
        btns_automation.press('enter')
        time.sleep(0.5)
        btns_automation.press('enter')

        # # navigate to name
        # time.sleep(1)
        # tools.copy_to_clipboard(launcher_name)
        # btns_automation.select_all()
        # btns_automation.press('enter')
        #
        # # navigate to path
        # self.logger.info('Setting Path...')
        # btns_automation.press('tab', 5, 0.1)
        # tools.copy_to_clipboard(launcher_obj.icon_path)
        # time.sleep(1)
        # btns_automation.select_all()
        # btns_automation.paste()
        #
        # self.logger.info('Disabling Trim...')
        # btns_automation.press('tab', 3, 0.1)
        # btns_automation.press('space')
        #
        # self.logger.info('Setting Resize...')
        # btns_automation.press('tab', 2, 0.1)
        # btns_automation.press('pagedown', presses=4, interval=0.1)
        # time.sleep(1)
        # btns_automation.press('right', presses=self.launcher_resize_percent, interval=0.1)
        #
        # time.sleep(2)
        # self.logger.info('Navigating to Background tab...')
        # btns_automation.press('tab', 9, 0.1)
        # btns_automation.press('right')
        #
        # # time.sleep(1)
        #
        # self.logger.info('Setting Background Color...')
        # btns_automation.press('tab', 3, 0.1)
        # btns_automation.press('space')
        #
        # self.logger.info('Clicking and setting the color...')
        # btns_automation.press('tab', 3, 0.1)
        # btns_automation.press('space')
        # color = self.launcher_background_color_hex.replace('#', '')
        # btns_automation.select_all()
        # btns_automation.write(color, interval=0.1)
        # time.sleep(2)
        # btns_automation.press('enter')
        #
        # self.logger.info('Clicking Next...')
        # btns_automation.press('enter')
        #
        # time.sleep(1)
        # self.logger.info('Clicking Finish...')
        # btns_automation.press('enter')
        #
        # self.logger.info('Gathering files...')
        # time.sleep(6)
        #
        # # launcher file continue....
        #
        # self.logger.info('Fixing xml files...')
        #
        # # fix xml files
        # fix_xml_files(launcher_made_files, random_suffix)

        # self.logger.info('Copying files...')
        # for launcher_file in launcher_made_files:
        #     rel_launcher_path = launcher_file.replace(f'{self.main_path}/', '')
        #     dst_launcher_file = os.path.join(launcher_obj.output_path, rel_launcher_path)
        #     dst_launcher_file = dst_launcher_file.replace(random_suffix, '')
        #     fh.copy_file(launcher_file, dst_launcher_file)
        #
        # self.logger.info('Removing temp files...')
        # fh.remove_files(launcher_made_files)

        self.logger.info('waiting for next cycle...')
        time.sleep(1.5)
        return True

    def print_ln(self):
        self.logger.info('--------------------------------------------------------------------------------')
