import nltk
import re


class Parser:
    def __init__(self, resume_text):
        self.resumeText = resume_text

    def extractEmail(self):
        emails = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", self.resumeText)

        if len(emails)>0:
            return emails[0]

        return None

    def extractPhoneNumber(self):
        phoneNumber = re.findall()


    def extractSkills(self):
        pass

    def title(self):
        pass
