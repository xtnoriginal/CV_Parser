import PyPDF2
import docx2txt
import  json
from resume_parser import Parser


def read_docx(filename)->str:
    '''Reads the contents of a docx file'''
    text = docx2txt.process(filename)
    return text


def read_pdf(filename)->str:
    '''Reads the contents of a  pdf file'''
    # creating a pdf file object
    fileObj = open(filename, 'rb')
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(fileObj)

    data = ''

    for pageObj in  pdfReader.pages:
        # extracting text from page
        data += '\n'+ pageObj.extractText()

    # closing the pdf file object
    fileObj.close()
    return data


def  read_json(filename)-> str:
    '''Reads a json file and return the data'''
    file  = open(filename, encoding='utf-8')
    data  = json.load(file)
    file.close()

    return  data


if __name__ == '__main__':
    #print(read_docx('dataset/Resume.docx'))
    #resumeText = read_pdf('dataset/my_resume.pdf')
    resumeText = read_pdf('dataset/Resume.pdf')
    print(resumeText)
    parser = Parser(resumeText)
    print(parser.extractEmail())
    print(parser.extractPhoneNumber())
    print('----')

