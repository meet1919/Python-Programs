import shutil, os

os.mkdir('C:\\Users\\meetg\\OneDrive\\Desktop\\PNG')
os.chdir('D:\\Users\\Meet\\Downloads')
destination = 'C:\\Users\\meetg\\OneDrive\\Desktop\\PNG'

for images in os.listdir():
    if images.endswith('.png'):
        absWorkDir = os.path.abspath('.')
        images = os.path.join(absWorkDir, images)
        shutil.move(images, destination)