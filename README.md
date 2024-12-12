# RegistryExplorer


  Recently, I learned how Windows registries work and the impact they can have in the field of defense. I want to improve my Python skills and integrate it more into my tasks in the field of cybersecurity. I've decided to use Python to read registries and return interesting information about the system.<br>

  The Registry contains information that Windows continually references during operation, such as profiles for each user, the applications installed on the computer and the types of documents that each can create, property sheet settings for folders and application icons, what hardware exists on the system, and the ports that are being used.[1]

### Windows Registry Analyzer in Python
This Python script is designed to read and extract valuable information from the Windows registry using the winreg module.[2]<br>

- The script uses `OpenKey`, `EnumKey`, and `EnumValue` from the winreg module to navigate and read the registry.
- Helper Functions
    - `addr_in_mac_format(val)`: Converts raw byte data into a human-readable MAC address format (e.g., FF:FF:FF:FF:FF:FF).
    - `printNets()`: Finds networks and their MAC addresses in the registry.
    - `get_startup_programs()`: Checks for startup programs in predefined registry locations.
    - `get_usb_devices()`: Lists USB devices by accessing the registry path where their data is stored.
    - `get_installed_programs()`: Gathers installed program names from specific registry paths.
- Main Function
combines all the functionality into a single flow:

    - Lists networks.
    - Lists startup programs.
    - Lists connected USB devices.
    - Prints installed programs.
  
> **Note:** This script focuses on applying a concept to address a few tasks, but there is much more potential for improvement and expansion with additional ideas.<br>
-----------------------------------------------
### References
[1] [Microsoft Documentation](https://learn.microsoft.com/en-us/troubleshoot/windows-server/performance/windows-registry-advanced-users)<br>
[2] [Winreg - Windows Registry Access](https://docs.python.org/3/library/winreg.html#winreg.EnumValue)<br>
[3] https://www.lifewire.com/windows-registry-2625992<br>
[4] https://www.geeksforgeeks.org/windows-registry/<br>
[5] O'Connor, T. (2012). Violent Python: A Cookbook for Hackers, Forensic Analysts, Penetration Testers and Security Engineers. 
