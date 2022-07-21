import gspread

gc = gspread.service_account("creeds.json")

sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1C8ymDGJwUYXUSgd12-9TYjfCRmH85SI9BEsWv0UowR0/edit#gid=0')

