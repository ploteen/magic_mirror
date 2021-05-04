<template>
  <div>
    <SoundCloud v-if='on'
      track='194881641' ref='player' :mini='true' @ready='ready'></SoundCloud>
  </div>
</template>

<script>
import annyang from 'annyang'
import SoundCloud from 'vue-soundcloud-player'
export default {
  components: {
    SoundCloud
  },
  data () {
    return {
      on: false
    }
  },
  methods: {
    start () {
      var self = this
      if (annyang) {
        var commands = {
          '노래 실행': function () { self.music_on() },
          '노래 멈춰': function () { self.music_off() }
        }
      }
      annyang.addCommands(commands)
      annyang.setLanguage('ko-KR')
      annyang.start()
    },
    music_on () {
      console.log('켜줘')
      this.on = true
    },
    music_off () {
      console.log('꺼줘')
      this.on = false
    },
    ready () {
      setTimeout(SoundCloud.components.Buttons.components.PlayButton.methods.playPause(), 2000)
    }
  },
  mounted () {
    this.start()
  }
}
</script>

<style>

</style>
