import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from config.config import Config

def write_google_sheets(flattened_data, st):
    df = pd.DataFrame(flattened_data)

    creds = Credentials.from_service_account_file(Config.GOOGLE_SHEETS_CREDENTIALS_FILE, scopes=["https://spreadsheets.google.com/feeds"])
    client = gspread.authorize(creds)
    sheet = client.open_by_key(Config.GOOGLE_SHEETS_ID).worksheet("Sheet1")

    # Replace problematic values
    df = df.replace({pd.NA: None, float("nan"): None, float("inf"): None, -float("inf"): None})

    # Find next available row
    col_values = sheet.col_values(1)
    next_row = len(col_values) + 1

    # Add headers if first write
    if next_row == 1:
        sheet.append_row(df.columns.tolist(), value_input_option="RAW")

    # Append data
    sheet.append_rows(df.values.tolist(), value_input_option="RAW")

    st.success("data is inserted in sheet")

    # Google Sheets link
    sheet_link = f"https://docs.google.com/spreadsheets/d/{Config.GOOGLE_SHEETS_ID}"

    return sheet_link