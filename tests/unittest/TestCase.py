import unittest

from resume_parser import Parser
from  util import *


class ResumeParserTest(unittest.TestCase):


    def test_extract_email(self):


        x ='''John Doe
Lorem ipsum dolor sit amet, consectetuer adipiscing elit
123 Your Street
Your City, ST 12345
(123) 456-7890
no_reply@example.com
EXPERIENCE'''
        parser1 = Parser(x)
        self.assertEqual(parser1.extractEmail(),'no_reply@example.com')


        data = '''EDUCATION
School Name, Location — Degree
MONTH 20XX - MONTH 20XX
Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore.
School Name, Location — Degree
MONTH 20XX - MONTH 20XX
Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam
'''
        parser1 = Parser(data)
        self.assertEqual(parser1.extractEmail(), None)

    def test_phone_number(self):
        pass

    def test_extract_skills(self):
        pass

class ReadFileTest(unittest.TestCase):

    def test_reading_of_pdf(self):
        self.assertEqual(read_pdf('../../dataset/testcase/yes.pdf'),'yes', 'Cannot read pdf file')
        self.assertEqual(read_pdf('../../dataset/testcase/hello.pdf'), 'hello', 'Cannot read pdf file')
        self.assertEqual(read_pdf('../../dataset/testcase/ballpoint.pdf'), 'ballpoint', 'Cannot read pdf file')


    def test_reading_of_docx(self):
        self.assertEqual(read_docx('../../dataset/testcase/yes.docx'), 'yes', 'Cannot read docx file')
        self.assertEqual(read_docx('../../dataset/testcase/hello.docx'), 'hello', 'Cannot read docx file')
        self.assertEqual(read_docx('../../dataset/testcase/ballpoint.docx'), 'ballpoint', 'Cannot read docx file')




class TestCase(unittest.TestCase):

    def test_reading_of_pdf(self):
        self.assertEqual(0,0)
        self.assertEqual(0,0)
        self.assertEqual(0,0)


    def test_number_of_pages(self):
        self.assertEqual(0,0)
        self.assertEqual(0,0)
        self.assertEqual(0,0)



if __name__ == '__main__':
    unittest.main()

