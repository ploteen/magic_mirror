<template>
  <div>
    <vue-weather api-key='305cf867acd95098efcf3daf2c07b38e' units='uk' v-bind:updateInterval='update'/>
  </div>
</template>

<script>
import VueWeather from 'vue-weather-widget'
export default {
  components: {
    VueWeather
  },
  data () {
    return {
      update: 1000000
    }
  }
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed&display=swap');
.vww__widget{
    color: white;
}
vue-weather{
  font-family: 'Roboto Condensed', Arial, Helvetica, sans-serif;
}
</style>
