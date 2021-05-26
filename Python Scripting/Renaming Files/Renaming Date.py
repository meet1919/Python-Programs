import os, shutil, re

os.chdir('C:\\Users\\meetg\\PycharmProjects\\untitled\\Random Projects\\Renaming Files\\Folder')

for files in os.listdir():
    change_date = re.compile(r'([0-1][0-9])-([0-3][0-9])-(\d{4})')
    mo = change_date.search(files)
    month_part = mo.group(1)
    date_part = mo.group(2)
    year_part = mo.group(3)

    euroFilename = date_part + '-' + month_part + '-' + year_part
    absWorkingDir = os.path.abspath('.')
    files = os.path.join(absWorkingDir, files)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    shutil.move(files, euroFilename)