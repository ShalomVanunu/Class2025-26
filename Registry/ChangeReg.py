
import winreg as reg

key_path = reg.CreateKey(reg.HKEY_CURRENT_USER,"SOFTWARE\Policies\Microsoft\Windows\System")
reg.SetValueEx(key_path,"DisableCMD",0,reg.REG_DWORD,0)