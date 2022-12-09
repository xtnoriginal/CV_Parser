import PyPDF2
import docx2txt

def read_docx(filename):
    '''Reads the contents of a docx file'''
    text = docx2txt.process(filename)
    return text


def read_pdf(filename):
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


if __name__ == '__main__':
    print(read_pdf('dataset/Resume.pdf'))
    print(read_docx('dataset/Resume.docx'))
