import unittest, csv
from faker import Faker
from unittest.mock import MagicMock
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.Display.OutputConsole import OutputConsole


class TestReadCSVFile(unittest.TestCase):
    outputConsole = OutputConsole()
    readCSVFile = ReadCSVFile()
    fake = Faker()

    def test_mockFakeLastLinesFromFile(self):
        fakerLastLines = [self.fake.email(), self.fake.first_name(), self.fake.last_name(), self.fake.password()]

        self.readCSVFile.getLastLines = MagicMock(return_value=fakerLastLines)

        self.assertEqual(self.readCSVFile.getLastLines(), fakerLastLines)

    def test_MockPrint(self):
        mockSuccessMessage = 'Mock successfully run!'

        self.outputConsole.print = MagicMock(return_value=mockSuccessMessage)

        self.assertEqual(self.outputConsole.print(), mockSuccessMessage)

'''Attempted to mock excpetion and then catch it
    def test_MockSideEffects(self):
        self.readCSVFile.getLastLines = MagicMock(side_effect=ValueError)

        self.assertRaises(ValueError, self.readCSVFile.getLastLines())
'''

def main():
    unittest.main()


if __name__ == "__main__":
    unittest.main()
