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

results = service.spreadsheets().batchUpdate(
    spreadsheetId = spreadsheetId,
    body = {
        "requests": [
            {'mergeCells': {'range': {'sheetId': sheetId,
                          'startRowIndex': 0,
                          'endRowIndex': 1,
                          'startColumnIndex': 1,
                          'endColumnIndex': 4},
                'mergeType': 'MERGE_ALL'}}
        ]
    }).execute()
# Добавляем заголовок таблицы
results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheetId, body = {
    "valueInputOption": "USER_ENTERED",
# Данные воспринимаются, как вводимые пользователем (считается значение формул)
    "data": [
        {"range": "Лист номер один!B1",
         "majorDimension": "ROWS", # Сначала заполнять строки, затем столбцы
         "values": [["Заголовок таблицы" ] 
                   ]}
    ]
}).execute()
