<template>
  <div>
  </div>
</template>

<script>
import annyang from 'annyang'
export default {
  methods: {
    start () {
      if (annyang) {
        var commands = {
          '안녕하세요': function () { alert('Hello world!') }
        }
      }
      annyang.addCommands(commands)
      annyang.setLanguage('ko-KR')
      annyang.start()
    }
  },
  mounted () {
    this.start()
  }
}
</script>

<style>

</style>
