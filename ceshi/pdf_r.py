from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open


def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdfFile)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    return content


# pdfFile = open('./22222.pdf', "rb")
pdfFile = urlopen("http://www.syepb.gov.cn/data2014-11/document/Table2019213132435.pdf")
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()
