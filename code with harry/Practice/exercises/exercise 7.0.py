import os
print(os.getcwd())

png_files=[png for png in os.listdir("clutter Ex.7") if png.endswith(".png")]
print(png_files)
i=1
for png in png_files:
    os.rename(f"clutter Ex.7/{png}",f"clutter Ex.7/{i+1}.png")
    i=i+1
    
