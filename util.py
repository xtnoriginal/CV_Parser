import PyPDF2

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
    pdfFileObj.close()


if __name__ == '__main__':
    read_pdf('dataset/my_resume.pdf-')
