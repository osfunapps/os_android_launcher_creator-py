from distutils.core import setup

setup(
    name='os_android_launcher_creator',
    packages=['os_android_launcher_creator', 'os_android_launcher_creator.bp'],
    version='1.12',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='This module will create an app launcher (logo) using Android Studio in all sizes and '
                'shapes (web, round) and in all dpi (mipmap-anydpi-v26, mipmap-hdpi, mipmap-mdpi, '
                'mipmap-xhdpi, mipmap-xxhdpi, mipmap-xxxhdpi, values)',  # Give a short description about your library
    author='Oz Shabat',  # Type in your name
    author_email='admin@os-apps.com',  # Type in your E-Mail
    url='https://github.com/osfunapps/os_android_launcher_creator-py',  # Provide either the link to your github or to your website
    keywords=['python', 'osfunapps', 'osapps', 'automation', 'logo', 'app launcher', 'os_file_stream_handler'],  # Keywords that define your package best
    install_requires=['os_tools', 'os_file_handler', 'os-btns-automation'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',  # Again, pick a license

        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9'
    ],
)

