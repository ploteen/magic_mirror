<template>
  <div class="calendar">
    <table class="list">
        <tbody>
        <tr v-for="sche in list" :key="sche.summary">
          <td class="icon"><img src="../../static/img/calendar.png" alt="aa"></td>
          <td class="summary">{{sche.summary}}</td>
          <td class="date">{{sche.start.date}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'Calender',
  data () {
    return {
      src: '@../../static/img/calendar_icon.svg',
      list: undefined
    }
  },
  methods: {
    get_calendar: function () {
      axios.get('http://localhost:8000/google/calendar').then((resp) => {
        this.list = resp.data
      }).catch((error) => {
        console.error(error)
      })
    }
  },
  created () {
    this.get_calendar()
  }
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed&display=swap');
.calendar{
  font-family: 'Roboto Condensed', Arial, Helvetica, sans-serif;
}
div{
  color: #aaa
}
img, .icon{
  height: 16px;
  width: 16px;
}
.date{
  text-align: end;
}
.summary{
  text-align: left;
}
table{
  width: 370px;
}
</style>
