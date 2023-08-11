import os

J_dir =  "E:\\test1\\thermal\\images_resized"

J_files = [f"{J_dir}/{fname.split('.')[0]}.{'tiff'}" for fname in os.listdir(J_dir) if fname.endswith(".JPG")]
print(J_files)
print(len(J_files))
print(len(J_files)//64)