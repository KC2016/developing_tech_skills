import os
import shutil

for folderName, subfolders, filenames in os.walk('/Tutorials'):  # <folder>
    # print('The folder is ' + folderName)
    # print('The subfolder in ' + folderName + ' are: ' + str(subfolders))
    # print('The filenames in ' + folderName + ' are: ' + str(filenames))
    # print()

    for subfolder in subfolders:
        # os.unlink(subfolder)
        if 'fish'in subfolder:
            # os.rmdir(subfolder)   # DANGEROUS
            print('rmdir on '+ subfolder)

    # for file in filenames:
    #     if file.endswith('.py'):
    #         shutil.copy(os.join(file, file + '.backup'))
    #         shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))
