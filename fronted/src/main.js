// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueWeather from 'vue-weather-widget'
import axios from 'axios'
// import annyang from 'annyang'
// import Recorder from 'recorderjs'
// import vueRecorder from 'vue-recorder'
Vue.config.productionTip = false
Vue.use(VueWeather)
// Vue.use(Recorder)
// Vue.use(vueRecorder)
Vue.prototype.$http = axios
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
