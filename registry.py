# use winreg module 
from winreg import * 


# retrun address in mac format (FF::FF)
def addr_in_mac_format(val):
    addr = ''
    for byte in val:
        addr += ('%02x:' %byte)
    return addr.strip(":") 


def printNets():
    # use reg file who contains info about networks 
    net = "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\NetworkList\\Signatures\\Unmanaged"
    # open key 
    # HKEY_LOCAL_MACHINE - info about hardware, software and system settings
    # KEY_READ - open with read rights
    key = OpenKey(HKEY_LOCAL_MACHINE, net,0 ,KEY_READ )
    print("[∗] Networks You have Joined.")
    for i in range(100):
        try:
            # enum subkeys
            guid= EnumKey(key,i)
            netKey = OpenKey(key,str(guid))
            # Enumerates values of an open registry key, returning a tuple.
            (n,addr,t) = EnumValue(netKey,5)
            (n,name,t) = EnumValue(netKey,4)
            macAddr = addr_in_mac_format(addr)
            print(f"[+] {str(name)}, {macAddr}")
            # Closes a previously opened registry key
            CloseKey(netKey)
        except:
            break

# What programs starts when the machien is powered up
def get_startup_programs():
    
    locations = [r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Run"]

    for location in locations:
        try:
            key = OpenKey(HKEY_CURRENT_USER, location)
            print(f"[*] Startup Programs in {location}:")
            i = 0
            while True:
                try:
                    name, value, _ = EnumValue(key, i)
                    print(f"- {name}: {value}")
                    i += 1
                except OSError:
                    break
        except FileNotFoundError:
            continue

# What USB devices are connected 
def get_usb_devices():
    usb_path = r"SYSTEM\CurrentControlSet\Enum\USBSTOR" 
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, usb_path)
        print("[*] USB Devices:")
        i = 0
        while True:
            try:
                device = EnumKey(key, i)
                print(f"- {device}")
                i += 1
            except OSError:
                break
        CloseKey(key)
    except FileNotFoundError:
        print("No USB devices found.")

# What programs are installed on the system
def get_installed_programs():

    locations = [r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall"]
    
    programs = []
    for location in locations:
        try:
            key = OpenKey(HKEY_LOCAL_MACHINE, location)
            i = 0
            while True:
                try:
                    subkey_name = EnumKey(key, i)
                    subkey = OpenKey(key, subkey_name)
                    try:
                        name = QueryValueEx(subkey, "DisplayName")[0]
                        programs.append(name)
                    except FileNotFoundError:
                        pass
                    finally:
                        CloseKey(subkey)
                    i += 1
                except OSError:
                    break
        except FileNotFoundError:
            continue
    return programs

def main():
    printNets()
    get_startup_programs()
    get_usb_devices()
    print("[*] Installed Programs:")
    for program in get_installed_programs():
        print(f"- {program}")

if __name__ == "__main__":
    main()

