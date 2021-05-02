from flask import Flask, render_template, jsonify,request
import datetime
import os.path
from flask_socketio import SocketIO, emit
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from flask_cors import CORS
from modules.news import news_crawl
#구글 인증
app = Flask(__name__)
#한글을 위한 인코딩 변경 
app.config['JSON_AS_ASCII'] = False
socketio = SocketIO(app, cors_allowed_origins='*')
#google oauth 
creds_filename = 'aouth_client.json'
CORS(app)
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

#google calendar fetch and send
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

@app.route('/audio', methods=['POST'])
def get_audio():
  now = str(datetime.datetime.now())
  str1 = str(now)[:10]
  str2 = str(now)[11:13]+now[14:16]+now[17:19]
  filename = str1+'-'+str2
  filename.replace('','-')
  request.files['data'].save("./audio/"+filename+".wav")
  return ''
#마지막에 js return 방식으로 바꾸기
@app.route('/recorderWorker.js')
def ret_recordworker():
    return """var recLength = 0,
  recBuffersL = [],
  recBuffersR = [],
  sampleRate;
self.onmessage = function(e) {
  switch(e.data.command){
    case 'init':
      init(e.data.config);
      break;
    case 'record':
      record(e.data.buffer);
      break;
    case 'exportWAV':
      exportWAV(e.data.type);
      break;
    case 'getBuffer':
      getBuffer();
      break;
    case 'clear':
      clear();
      break;
  }
};
function init(config){
  sampleRate = config.sampleRate;
}
function record(inputBuffer){
  recBuffersL.push(inputBuffer[0]);
  recBuffersR.push(inputBuffer[1]);
  recLength += inputBuffer[0].length;
}
function exportWAV(type){
  var bufferL = mergeBuffers(recBuffersL, recLength);
  var bufferR = mergeBuffers(recBuffersR, recLength);
  var interleaved = interleave(bufferL, bufferR);
  var dataview = encodeWAV(interleaved);
  var audioBlob = new Blob([dataview], { type: type });
  self.postMessage(audioBlob);
}
function getBuffer() {
  var buffers = [];
  buffers.push( mergeBuffers(recBuffersL, recLength) );
  buffers.push( mergeBuffers(recBuffersR, recLength) );
  self.postMessage(buffers);
}
function clear(){
  recLength = 0;
  recBuffersL = [];
  recBuffersR = [];
}
function mergeBuffers(recBuffers, recLength){
  var result = new Float32Array(recLength);
  var offset = 0;
  for (var i = 0; i < recBuffers.length; i++){
    result.set(recBuffers[i], offset);
    offset += recBuffers[i].length;
  }
  return result;
}
function interleave(inputL, inputR){
  var length = inputL.length + inputR.length;
  var result = new Float32Array(length);
  var index = 0,
    inputIndex = 0;
  while (index < length){
    result[index++] = inputL[inputIndex];
    result[index++] = inputR[inputIndex];
    inputIndex++;
  }
  return result;
}
function floatTo16BitPCM(output, offset, input){
  for (var i = 0; i < input.length; i++, offset+=2){
    var s = Math.max(-1, Math.min(1, input[i]));
    output.setInt16(offset, s < 0 ? s * 0x8000 : s * 0x7FFF, true);
  }
}
function writeString(view, offset, string){
  for (var i = 0; i < string.length; i++){
    view.setUint8(offset + i, string.charCodeAt(i));
  }
}
function encodeWAV(samples){
  var buffer = new ArrayBuffer(44 + samples.length * 2);
  var view = new DataView(buffer);
  /* RIFF identifier */
  writeString(view, 0, 'RIFF');
  /* RIFF chunk length */
  view.setUint32(4, 36 + samples.length * 2, true);
  /* RIFF type */
  writeString(view, 8, 'WAVE');
  /* format chunk identifier */
  writeString(view, 12, 'fmt ');
  /* format chunk length */
  view.setUint32(16, 16, true);
  /* sample format (raw) */
  view.setUint16(20, 1, true);
  /* channel count */
  view.setUint16(22, 2, true);
  /* sample rate */
  view.setUint32(24, sampleRate, true);
  /* byte rate (sample rate * block align) */
  view.setUint32(28, sampleRate * 4, true);
  /* block align (channel count * bytes per sample) */
  view.setUint16(32, 4, true);
  /* bits per sample */
  view.setUint16(34, 16, true);
  /* data chunk identifier */
  writeString(view, 36, 'data');
  /* data chunk length */
  view.setUint32(40, samples.length * 2, true);
  floatTo16BitPCM(view, 44, samples);
  return view;
}
"""
@app.route('/news')
def news():
    nnews = news_crawl()
    dict_nnews = {i: string for i,string in enumerate(nnews)}
    # print(dict_nnews)
    return jsonify(dict_nnews)
    
    
port_num = "8000"
host_addr = "0.0.0.0"
if __name__ == "__main__":
  app.run(host=host_addr, port=port_num,debug=True)