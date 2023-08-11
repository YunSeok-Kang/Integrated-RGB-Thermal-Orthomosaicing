import os
import yaml
import sys
import shutil

def rename_file_extension(directory, old_extension, new_extension):
    for filename in os.listdir(directory):
        # print(filename)
        # if filename.endswith(old_extension):
        #     print(filename)
        #     old_file = os.path.join(directory, filename)
        #     new_file = os.path.join(directory, os.path.splitext(filename)[0] + new_extension)
        #     os.rename(old_file, new_file)
        old_file = directory + '/' + filename # os.path.join(directory, filename)
        new_file = directory + '/' + filename.split('.')[0] + '.TIFF'#os.path.join(directory, os.path.splitext(filename)[0] + new_extension)
        print(old_file + ', ' + new_file)
        os.rename(old_file, new_file)

def get_ODM_flags(ODM_params):
    flags = ''
    for key, value in ODM_params.items():
        flags += f'--{key} {value} '
    return flags

def run():
    cfg_path = 'C:/Users/ysck73/Documents/Integrated-RGB-Thermal-Orthomosaicing/configs/combined.yml'
    if not os.path.exists(cfg_path):
        print("Please specify a valid config path.")
        return

    with open(cfg_path, 'rb') as f:
        cfg = yaml.safe_load(f.read())
    print("\n\n------------ STAGE 4 ------------")

    project = 'E:/test1'
    output_dir = f"{project}/output"

    # 사용 예시
    directory = f'{project}/combined/opensfm/undistorted/images'  # 특정 디렉토리 경로
    old_extension = '.JPG.tif'  # 변경하려는 확장자
    new_extension = '.tiff'  # 변경될 확장자

    # rename_file_extension(directory, old_extension, new_extension)

    ## run ODM on thermal data from texturing step
    os.chdir("ODM")
    flags_dir = cfg["ODM"]
    flags_dir.pop('rerun-all')
    flags_dir["rerun-from mvs_texturing"] = ''

    flags = get_ODM_flags(flags_dir)
    # second_part = f"{ROOT_DIR}/{project}/combined" if ROOT_DIR not in project else f"{project}/combined"
    second_part = f"{project}/combined"
    call_2 = f".\\run.bat {flags} {second_part}"
    
    # with open('output_temp.txt', 'w') as file:
    #     file.write(call_2)
    #     file.close()

    f = open("C:/Users/ysck73/Documents/Integrated-RGB-Thermal-Orthomosaicing/새파일.txt", 'w')
    f.write(call_2)
    f.close()

    os.system(call_2)
    os.chdir("..")


    ## move orthophoto
    output_path = f'{output_dir}/orthophoto_combined_thermal.tif'
    shutil.move(f'{project}/combined/odm_orthophoto/odm_orthophoto.tif', output_path) 


if __name__=="__main__":
    run()

    # directory ='E:/test1/combined/opensfm/undistorted/images'  # 특정 디렉토리 경로
    # old_extension = '.JPG.tiff'  # 변경하려는 확장자
    # new_extension = '.tiff'  # 변경될 확장자

    # rename_file_extension(directory, old_extension, new_extension)
