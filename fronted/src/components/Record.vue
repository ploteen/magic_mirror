<template>
  <div>
  </div>
</template>

<script>
import vueRecorder from 'vue-recorder'
import axios from 'axios'
export default {
  name: 'Record',
  data () {
    return {
      message: 0
    }
  },
  methods: {
    startRecording: function () {
      vueRecorder.startRecording()
      // console.log(vueRecorder)
    },
    stopRecording: function () {
      let self = this
      // console.log(vueRecorder)
      vueRecorder.stopRecording().then(audio => {
        self.resumeRecording()
        const fd = new FormData()
        fd.append('data', audio.blob)
        axios.post('./audio', fd)
      })
    },
    resumeRecording: function () {
      vueRecorder.resumeRecording()
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
</style>
