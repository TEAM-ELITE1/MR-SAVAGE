import platform,os
os.system("git pull")
bit = platform.architecture()[0]
if bit == '64bit':
    import new_64
elif bit == '32bit':
    import new_32
