import datetime
import urllib.request

dateString = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y%m%d')

ctnWeb = "https://www.chp.gov.hk/files/pdf/ctn_" + \
         dateString + \
         ".pdf"

response = urllib.request.urlopen(ctnWeb)
print(response)
file = open('file_ctn', 'wb')
file.write(response.read())
file.close()
