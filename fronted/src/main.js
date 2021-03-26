// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueMoment from 'vue-momentjs'
import VueWeather from 'vue-weather-widget'
Vue.config.productionTip = false
Vue.use(VueMoment)
Vue.use(VueWeather)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
