<template>
  <div></div>
</template>

<script>
import io from 'socket.io-client'
import RecordRTC from 'recordrtc'
import axios from 'axios'
export default {
  name: 'Record',
  data () {
    return {
      socketio: undefined,
      socket: undefined,
      recordAudio: ''
    }
  },
  methods: {
    startRecording () {
      let self = this
      navigator.getUserMedia({
        audio: true
      }, function (stream) {
        self.recordAudio = RecordRTC(stream, {
          type: 'audio',
          recorderTyped: RecordRTC.StereoAudioRecorder,
          mimeType: 'audio/wav',
          numberOfAudioChannels: 2,
          timeSlice: 3000,
          ondataavailable: function (blob) {
            const fd = new FormData()
            fd.append('data', blob)
            axios.post('/audio', fd)
          }
        })
        console.log(RecordRTC.StereoAudioRecorder)
        self.recordAudio.startRecording()
      }, function (error) {
        console.error(JSON.stringify(error))
      })
    },
    socket_connect () {
      this.socketio = io('http://localhost:8000')
      console.log(this.socket)
      console.log(this.socketio)
    }
  },
  mounted () {
    this.socket_connect()
    this.startRecording()
    console.log(this.recordAudio)
  }
}
</script>

<style>
</style>
