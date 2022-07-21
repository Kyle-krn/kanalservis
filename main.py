import gspread
import config

gc = gspread.service_account("creeds.json")
sh = gc.open_by_url(config.SHEETS_URL)

