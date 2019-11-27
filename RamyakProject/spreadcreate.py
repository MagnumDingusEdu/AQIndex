import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('gspread-april-2cd … ba4.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("Where is the money Lebowski?").sheet1