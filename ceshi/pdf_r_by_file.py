from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open


def readPDF(pdffile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdffile)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    return content


pdffile = open('./22222.pdf', "rb")
title = readPDF(pdffile)
print(title)
pdffile.close()
