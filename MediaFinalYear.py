'''
    Name: (C) Diogo Santos
    Date: 22/01/2025
'''

SDAC = float(input("Enter the media you have in SDAC: "))
IMEI = float(input("Enter the media you have in IMEI: "))
ELF = float(input("Enter the media you have in ELF: "))
CD = float(input("Enter the media you have in CD: "))

Media = (SDAC + IMEI + ELF + CD) / 4 

if Media >= 9.5:
    print(f"Your media is", Media,", congratulations you have passed the year.")
else: 
    print(f"Your media is", Media,", unfortunately you did not passed the year :(")