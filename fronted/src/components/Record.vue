<template>
  <div>{{message}}</div>
</template>

<script>
import vueRecorder from 'vue-recorder'
// import axios from 'axios'
export default {
  name: 'Record',
  data () {
    return {
      message: ''
    }
  },
  methods: {
    startRecording: function () {
      this.message = vueRecorder.startRecording()
      console.log(this.message)
    },
    stopRecording: function () {
    }
  },
  created () {
    this.startRecording()
    // this.stopRecording()
  }
}
</script>

<style>
</style>
