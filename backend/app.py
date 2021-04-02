from flask import Flask, render_template, jsonify
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

#구글 인증
app = Flask(__name__)
#google oauth 
creds_filename = 'aouth_client.json'

SCOPES = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file(creds_filename, SCOPES)


creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'aouth_client.json', SCOPES)
        creds = flow.run_local_server(port=9000)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
service = build('calendar','v3',credentials=creds)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/google/calendar', methods=['GET','OPTIONS'])
def get_calendar():
    calendar_id = 'primary'
    today = datetime.date.today().isoformat()
    next_week = datetime.date.today() + datetime.timedelta(days=7)
    next_week = next_week.isoformat()
    time_min = today + 'T00:00:00+09:00'
    time_max = next_week + 'T23:59:59+09:00'
    max_results = 5
    is_single_events = True
    orderby = 'startTime'

    events_result = service.events().list(calendarId = calendar_id,
                                    timeMin = time_min,
                                    timeMax = time_max,
                                    maxResults = max_results,
                                    singleEvents = is_single_events,
                                    orderBy = orderby
                                    ).execute()
    #print(events_result)
    return jsonify(events_result.get('items',[]))
port_num = "8000"
host_addr = "0.0.0.0"

if __name__ == "__main__":
    app.run(host=host_addr,port=port_num,debug=True)