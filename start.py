import subprocess

subprocess.call(["python", "modules/verify_parameters.py"])

print("verify_downloadtype.py being called...")
subprocess.call(["python", "modules/verify_downloadtype.py"])
print("verify_downloadtype.py has finished execution")
