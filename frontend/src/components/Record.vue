<template>
  <div>
    <div class="video" v-if='is_washing'>
      <video width='450' controls autoplay>
        <source :src='video' type="video/mp4">
        this browser dosen't support video tag
      </video>
    </div>
    <div class="timer" v-if='is_washing'>
      <p>적정 손씻기 시간 {{timer}}초 남았습니다</p>
    </div>
  </div>
</template>

<script>
import vueRecorder from 'vue-recorder'
import axios from 'axios'
export default {
  name: 'Record',
  data () {
    return {
      is_washing: true,
      video: require('@/assets/washing_six.mp4'),
      count: 0,
      bool: undefined,
      timer: 30
    }
  },
  methods: {
    startRecording: function () {
      vueRecorder.startRecording()
      // console.log(vueRecorder)
    },
    stopRecording: function () {
      // console.log(vueRecorder)
      var self = this
      vueRecorder.stopRecording().then((audio) => {
        vueRecorder.resumeRecording()
        const fd = new FormData()
        fd.append('data', audio.blob)
        axios.post('./audio', fd).then((response) => {
          if (response.data === 'False') self.count += 1
          else if (response.data === 'True' && self.is_washing === false) {
            self.count = 0
            self.timer = 30
            self.is_washing = true
            self.start()
          }
          if (self.count >= 10) self.is_washing = false
          console.log(self.count)
        })
      })
    },
    start: function () {
      var self = this
      if (this.timer === 0) self.is_washing = 0
      else {
        self.timer -= 1
        setTimeout(self.start, 1000)
      }
    }
  },
  mounted () {
    this.startRecording()
    var temp = this
    setInterval(function () {
      temp.stopRecording()
    }, 1300)
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
.timer {
  color: #aaa;
  font-size: 30px;
  font-family: 'Jua', sans-serif;
}
</style>
