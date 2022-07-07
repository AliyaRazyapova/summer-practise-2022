import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials	

CREDENTIALS_FILE = 'mypython-355520-bc3bc36ec2c1.json'  # Имя файла с закрытым ключом, вы должны подставить свое

# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

spreadsheetId = '1cV5r6saSpKsiUG_Vtnc2Nl1Vx4VWz5HWsJy3XB_2zxg' # сохраняем идентификатор файла

ranges = ["Лист номер один!C2:C2"] 
          
results = service.spreadsheets().get(spreadsheetId = spreadsheetId, 
                                     ranges = ranges, includeGridData = True).execute()
print('Основные данные')
print(results['properties'])
print('\nЗначения и раскраска')
print(results['sheets'][0]['data'][0]['rowData'] )
print('\nВысота ячейки')
print(results['sheets'][0]['data'][0]['rowMetadata'])
print('\nШирина ячейки')
print(results['sheets'][0]['data'][0]['columnMetadata'])
