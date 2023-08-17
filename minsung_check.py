import os 
import os.path as osp
from PIL import Image
from PIL.ExifTags import TAGS


if __name__ == '__main__':
    path = 'E:\\test_minsung\\mapping_data\\thermal\\DJI_20230706172123_0001_T.JPG'
    DIR_NAME = 'E:\\test_minsung\\mapping_data\\converted'
    files = os.listdir(DIR_NAME)
    out = 'E:\\test_minsung\\mapping_data\\converted'

    for file in files:
        path = osp.join(DIR_NAME, file)
        image = Image.open(path)
        exif_data = image.getexif()
        exif_data[272] = "MAVIC2-ENTERPRISE-ADVANCED"
        image.save(osp.join(out, file), exif=exif_data)

