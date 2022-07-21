import os
import shutil
import time
import os.path
import shutil

def removeFolderRecursively(targetFolder):
    #checks if path is a file
    if(os.path.isfile(targetFolder)):
        #print(targetFolder + ' is a file')
        os.remove(targetFolder)
        return

    filesInCurrentFolder = os.listdir(targetFolder)
    
    if len(filesInCurrentFolder) == 0:
        #print(targetFolder + ' is a directory')
        os.removedirs(targetFolder)
        return
    
    for file in filesInCurrentFolder:
        #print(targetFolder + file)
        removeFolderRecursively(targetFolder + '/' + file)
        
def fileCounter(targetFolder):
    #checks if path is a file
    if(os.path.isfile(targetFolder)):
        #print(targetFolder + ' is a file')
        os.remove(targetFolder)
        return

    filesInCurrentFolder = os.listdir(targetFolder)
    
    if len(filesInCurrentFolder) == 0:
        #print(targetFolder + ' is a directory')
        os.removedirs(targetFolder)
        return
    
    for file in filesInCurrentFolder:
        print(targetFolder + file)
        removeFolderRecursively(targetFolder + '/' + file)

def move_target_file(targetDest, outputDes):
    print(targetDest + '\t' + outputDes)
    #shutil.move(targetDest, outputDes)

def make_pydeface(targetDest):
    print("pydeface file: " + targetDest + '\t')
    #os.system('pydeface ' + targetDest)
    
def convertDICOMtoNIFTI(sourceDest, targetDest):
    commandR = sourceDest + " " + targetDest
    os.system("dcm2niix -f '%f_%p_%t_%s' -p y -z y -o  " + commandR)
    
def main():
    desktopPath = '/home/aegean-river/Desktop/'
    nifti = 'nifti/'
    target = 'ENIGMA_REST_EXP/DICOM/'
    subjectPath = desktopPath + target
    startTime = time.perf_counter()

    subjects = os.listdir(subjectPath)
    
    removeFolderRecursively(desktopPath + nifti)

    os.mkdir(desktopPath + nifti)
    
    counter = 0

    for subject in subjects:
        if '.' in subject:
            os.remove(subjectPath + subject)
        else:
            targetDest = subjectPath + subject + '/'
            
            sourceDest = desktopPath + nifti + subject + '/'
            
            os.mkdir(sourceDest)
            
            #print(convertDICOMtoNIFTI(sourceDest, targetDest))

            counter += 1
    
    endOfTheTime = time.perf_counter()
    
    
def make_deface_and_move():
    desktopPath = '/home/aegean-river/Desktop/'
    nifti = 'nifti/'
    target = 'ENIGMA_REST_EXP/DICOM/'
    subjectPath = desktopPath + target
    startTime = time.perf_counter()

    subjects = os.listdir(subjectPath)
    
    removeFolderRecursively(desktopPath + nifti)

    os.mkdir(desktopPath + nifti)
    
    counter = 0

    #rename files
    for subject in subjects:
        targetDest = subjectPath + subject + '/'
        targetFiles = os.listdir(targetDest)
        for targetFile in targetFiles:
            if 'ep2d_pace' in targetFile:
                if '.json' in targetFile:
                    targetKeywords = targetFile.split('_')
                    outputDes = targetDest + 'anat/' + targetKeywords[0] + '_T1w.json'
                    move_target_file(targetDest, outputDes)
                    
                elif '.nii.gz' in targetFile:
                    targetKeywords = targetFile.split('_')
                    outputDes = targetDest + 'anat/' + targetKeywords[0] + '_T1w.nii.gz'
                    move_target_file(targetDest, outputDes)
            
            if 'mpr_sag_iso' in targetFile:
                if '.json' in targetFile:
                    targetKeywords = targetFile.split('_')
                    outputDes = targetDest + 'func/' + targetKeywords[0] + '_task-rest_bold.json'
                    move_target_file(targetDest, outputDes)
                    
                elif '.nii.gz' in targetFile:
                    targetKeywords = targetFile.split('_')
                    outputDes = targetDest + 'func/' + targetKeywords[0] + '_task-rest_bold.nii.gz'
                    move_target_file(targetDest, outputDes)
                

    #Make deface
    for subject in subjects:
        targetDest = subjectPath + subject + '/anat/'
        targetFiles = os.listdir(targetDest)
        for targetFile in targetFiles:
            if '_T1w.nii.gz' in targetFile and 'defaced' not in targetFile:
                make_pydeface(targetDest + targetFile)
                
                
    #Change names of defaced files
        
        #print(convertDICOMtoNIFTI(sourceDest, targetDest))

        counter += 1
    
    endOfTheTime = time.perf_counter()

