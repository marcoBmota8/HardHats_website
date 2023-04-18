from flask import Flask, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Define the scope of the credentials
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

# Load the credentials from the JSON file
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'path/to/credentials.json', scope
)

# Authenticate the credentials and open the Google Sheet
client = gspread.authorize(creds)
sheet = client.open('Name of Google Sheet').sheet1

@app.route('/')
def index():
    # Fetch the data from the Google Sheet
    data = sheet.get_all_records()

    # Render the data in an HTML table
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
