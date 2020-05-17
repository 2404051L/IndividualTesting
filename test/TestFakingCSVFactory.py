import os
import unittest

from src.DataSource.DataSourceConstants import *
from src.DataSource.FakerFactory import fakeCSVFile
from src.DataSource.ReadCSVFile import ReadCSVFile


class TestFakingCSVFactory(unittest.TestCase):
    readCSVFile = ReadCSVFile()
    fakeFilePath = '../resource/Entities/FakerGeneratedData.csv'

    def removeExistingFakerFile(self):
        if os.path.exists(self.fakeFilePath):
            os.remove(self.fakeFilePath)

    def test_checkFakerFileIsCreated(self):
        self.removeExistingFakerFile()

        fakeCSVFile(100, ["emailAddress", "firstName", "lastName", "password"])

        self.assertEqual(os.path.exists(self.fakeFilePath), True)

    def test_ExpectedRowCountCreated(self):
        self.removeExistingFakerFile()

        actualRows = 100
        columns = ["emailAddress", "firstName", "lastName", "password"]

        fakeCSVFile(actualRows, columns)
        fileRows = self.readCSVFile.getFileData(ENTITIES_FOLDER, "FakerGeneratedData" + ".csv")

        expectedRows = len(fileRows)-1

        self.assertEqual(expectedRows, actualRows)


def main():
    unittest.main()


if __name__ == "__main__":
    unittest.main()
