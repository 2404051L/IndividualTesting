import csv
import subprocess
import os

class ReadCSVFile :

    filePathPrefix = "../resource/"

    def getFileData(self, directory,  fileName):
        fileData = []
        with open(self.filePathPrefix + directory + fileName,'rt')as dataFile:
            fileReader = csv.reader(dataFile)
            for row in fileReader:
                fileData.append(row)
        return fileData

    def getLastLines(self,directory, fileName, numerOfLines):
        try:
            return self.getFileData(directory, fileName)[-1*numerOfLines]
        except IndexError:
            return 'File is empty'