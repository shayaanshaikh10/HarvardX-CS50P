name=input("Enter the file name: ").lower().strip()
if "." in name:
    file,ext=name.rsplit(".",1)
    if ext=="gif" or ext=="png":
        print(f"image/{ext}")
    elif ext=="jpg" or ext=="jpeg":
        print("image/jpeg")
    elif ext=="pdf" or ext=="zip" :
        print(f"application/{ext}")
    elif ext=="txt":
        print("text/plain")
    else:
        print("application/octet-stream")
else:
    print("application/octet-stream")