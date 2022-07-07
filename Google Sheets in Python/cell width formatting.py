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

results = service.spreadsheets().batchUpdate(spreadsheetId = spreadsheetId, body = {
  "requests": [

    # Задать ширину столбца A: 20 пикселей
    {
      "updateDimensionProperties": {
        "range": {
          "sheetId": sheetId,
          "dimension": "COLUMNS",  # Задаем ширину колонки
          "startIndex": 0, # Нумерация начинается с нуля
          "endIndex": 1 # Со столбца номер startIndex по endIndex - 1 (endIndex не входит!)
        },
        "properties": {
          "pixelSize": 20 # Ширина в пикселях
        },
        "fields": "pixelSize" # Указываем, что нужно использовать параметр pixelSize  
      }
    },

    # Задать ширину столбцов B и C: 150 пикселей
    {
      "updateDimensionProperties": {
        "range": {
          "sheetId": sheetId,
          "dimension": "COLUMNS",
          "startIndex": 1,
          "endIndex": 3
        },
        "properties": {
          "pixelSize": 150
        },
        "fields": "pixelSize"
      }
    },

    # Задать ширину столбца D: 200 пикселей
    {
      "updateDimensionProperties": {
        "range": {
          "sheetId": sheetId,
          "dimension": "COLUMNS",
          "startIndex": 3,
          "endIndex": 4
        },
        "properties": {
          "pixelSize": 200
        },
        "fields": "pixelSize"
      }
    }
  ]
}).execute()
