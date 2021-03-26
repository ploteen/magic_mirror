<template>
  <div>
    <vue-weather api-key='04ff2c2d0631957fff669067314d0595' units='uk' />
  </div>
</template>

<script>
import VueWeather from 'vue-weather-widget'

export default {
  components: {
    VueWeather
  }
}
</script>
<style scoped>
.vww__widget{
    color: white;
}
</style>
