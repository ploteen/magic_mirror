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
      list: [
        {
          'created': '2021-04-02T09:54:27.000Z',
          'creator': {
            'email': 'khw74074565@gmail.com',
            'self': true
          },
          'end': {
            'date': '2021-04-03'
          },
          'etag': '\'3234714535368000\'',
          'eventType': 'default',
          'htmlLink': 'https://www.google.com/calendar/event?eid=NDRmb3M1NGZnbzZ1a3JwdGIxbm0xZzNqYXYga2h3NzQwNzQ1NjVAbQ',
          'iCalUID': '44fos54fgo6ukrptb1nm1g3jav@google.com',
          'id': '44fos54fgo6ukrptb1nm1g3jav',
          'kind': 'calendar#event',
          'organizer': {
            'email': 'khw74074565@gmail.com',
            'self': true
          },
          'reminders': {
            'useDefault': false
          },
          'sequence': 0,
          'start': {
            'date': '2021-04-02'
          },
          'status': 'confirmed',
          'summary': 'test',
          'transparency': 'transparent',
          'updated': '2021-04-02T09:54:27.684Z'
        },
        {
          'created': '2021-04-02T10:40:42.000Z',
          'creator': {
            'email': 'khw74074565@gmail.com',
            'self': true
          },
          'end': {
            'date': '2021-04-04'
          },
          'etag': '\'3234720085072000\'',
          'eventType': 'default',
          'htmlLink': 'https://www.google.com/calendar/event?eid=MG0xMTZtYnViZXNjN20xbHNnYXJxNWNpYWIga2h3NzQwNzQ1NjVAbQ',
          'iCalUID': '0m116mbubesc7m1lsgarq5ciab@google.com',
          'id': '0m116mbubesc7m1lsgarq5ciab',
          'kind': 'calendar#event',
          'organizer': {
            'email': 'khw74074565@gmail.com',
            'self': true
          },
          'reminders': {
            'useDefault': false
          },
          'sequence': 0,
          'start': {
            'date': '2021-04-03'
          },
          'status': 'confirmed',
          'summary': 'test2',
          'transparency': 'transparent',
          'updated': '2021-04-02T10:40:42.536Z'
        }
      ]
    }
  },
  methods: {
    get_calendar: function () {
      axios.get('http://localhost:8000/google/calendar').then((resp) => {
        this.list = resp.data
      }).catch((error) => {
        console.error(error)
      })
    },
    parsing: function () {
      console.log(this.list[0].summary)
    }
  },
  created () {
    this.parsing()
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
