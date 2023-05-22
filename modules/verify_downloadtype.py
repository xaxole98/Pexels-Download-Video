from verify_parameters import params
import subprocess

    # Author information
print("╔═════════════════════════════════════════════════════════════╗")
print("║ Success:                                                    ║")
print("║ TypeDownload Success, Please wait a time <3                 ║")
print("║ Author: chesitavt in youtube & tiktok                       ║")
print("╚═════════════════════════════════════════════════════════════╝")
print("\n")
print("╔═════════════════════════════════════════════════════════════╗")
print("║ Please make sure the required variables are set correctly   ║")
print("║ in the 'Settings' folder for the script to work correctly.  ║")
print("╚═════════════════════════════════════════════════════════════╝")
print("\n")

def verify_downloadtype():
    typedownload = params.typedownload
    if typedownload == 'query':
        subprocess.call(["python", "modules/query_download.py"])
    else:
        print("Error: typedownload - 'query' or 'collection' is only what you can use")
        
verify_downloadtype()