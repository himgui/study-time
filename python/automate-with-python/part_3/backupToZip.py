#! python3
# BackuptoZip.y - Copies an entire folder and its content to a zip file.

import zipfile, os

def backupToZip(folder):
    # Backup all content from the folder to a zip file.

    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

        print('Creating %s...'% (zipFilename))
        backupZip = zipfile.ZipFile(zipFilename, 'w')

        for foldername, subfolders, filenames in os.walk(folder):
            print('Adding files in %s...' % (foldername))
            backupZip.write(foldername)

            for filename in filenames:
                newBase = os.path.basename(folder) + '_'
                if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue
                backup.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done')