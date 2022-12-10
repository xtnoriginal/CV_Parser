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
        phone = re.findall(re.compile(
            r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'),
                           self.resumeText)


    def extractSkills(self):
        pass

    def title(self):
        pass
