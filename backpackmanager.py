# Add shebang
import platform
import os


usr_os = platform.system()

if os.path.exists("app_installed"):
    if usr_os == "Windows":
        import win_install
        win_install.install()
    elif usr_os == "Linux":
        import linux_install
        linux_install.install()
    else:
        print("OS not fully supported. Some OS specific features will not be available")