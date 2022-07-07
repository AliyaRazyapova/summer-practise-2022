import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials	

CREDENTIALS_FILE = 'mypython-355520-bc3bc36ec2c1.json'  # Имя файла с закрытым ключом, вы должны подставить свое

# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

spreadsheetId = '1cV5r6saSpKsiUG_Vtnc2Nl1Vx4VWz5HWsJy3XB_2zxg' # сохраняем идентификатор файла

{"range": "Лист номер один!B2:D5"}

spreadsheet = service.spreadsheets().get(spreadsheetId = spreadsheetId).execute()
sheetList = spreadsheet.get('sheets')
    
sheetId = sheetList[0]['properties']['sheetId']

# Установка формата ячеек
results = service.spreadsheets().batchUpdate(
    spreadsheetId = spreadsheetId,
    body = 
{
  "requests": 
  [
    {
      "repeatCell": 
      {
        "cell": 
        {
          "userEnteredFormat": 
          {
            "horizontalAlignment": 'CENTER',
            "backgroundColor": {
                "red": 0.8,
                "green": 0.8,
                "blue": 0.8,
                "alpha": 1
            },
            "textFormat":
             {
               "bold": True,
               "fontSize": 14
             }
          }
        },
        "range": 
        {
          "sheetId": sheetId,
          "startRowIndex": 1,
          "endRowIndex": 2,
          "startColumnIndex": 1,
          "endColumnIndex": 4
        },
        "fields": "userEnteredFormat"
      }
    }
  ]
}).execute()
