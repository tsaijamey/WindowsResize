import ctypes

# Loading a core Windows library 
user32 = ctypes.windll.user32 

# Example: Calling a Windows API function for a message box
result = user32.MessageBoxW(None, "Hello from ctypes!", "Greetings", 0x0) 
print(result)