name = input("Provide me with the full name of your file")
P1, ext = name.split(".")

if ext == "gif":
    print("Image/Gif")
elif ext == "jpg" or ext == "jpeg":
    print("Image/Jpeg")
elif ext == "png":
    print("Image/png")
elif ext == "pdf":
    print("application/pdf")
elif ext == "txt":
    print("Text")
elif ext == "zip":
    print("Zip")
else: 
    print("application/octet-stream")                    