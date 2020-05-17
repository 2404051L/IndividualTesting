import unittest, csv
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.DataSource.DataSourceConstants import *


class TestReadStub(unittest.TestCase):
    readCSVFile = ReadCSVFile()

    def test_getDataFromStub(self):
        fileData = self.readCSVFile.getFileData(ENTITIES_FOLDER, "stub" + ".csv")
        self.assertEqual(fileData[1], ['test@test.com', 'TestFirstName', 'TestLastName', '123'])

    def test_getLastLinesFromStub(self):
        fileLines = self.readCSVFile.getLastLines(ENTITIES_FOLDER, "stub" + ".csv", 1)
        self.assertEqual(fileLines, ['test2@test.com', 'Test2', 'Test2', '456'])


def main():
    unittest.main()


if __name__ == "__main__":
    unittest.main()
