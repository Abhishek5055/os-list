import os

files =os.listdir("abc1")
i=1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"abc1/{file}",f'abc1/{i}.png')
        i=i+1