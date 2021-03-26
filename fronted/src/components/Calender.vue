<template>
  <div class='calender'>
      <button type='button' class='btn btn-primary'  if='!authorized' @click='handleAuthClick'>Login</button>
      <button type='button' class='btn btn-primary' v-if='authorized' @click='handleSignOutClick'>Sign Out</button>
      <button type='button' class='btn btn-primary' v-if='authorized' @click='getEvents'>Get Events</button>
  </div>
</template>
<script>
import moment from 'moment'
import gpi from '../../static/javascript/gpi'
export default {
  name: 'Calender',
  data () {
    return {
      authorized: false,
      items: undefined,
      CLIENT_ID: '68207220336-kbh910d113vi9vgvaa947pqtvftg897f.apps.googleusercontent.com',
      API_KEY: 'AIzaSyBQE6TpX_Mtk9BbqT6zMmwtnvM2aw7Lk58',
      DISCOVERY_DOCS: ['https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest'],
      SCOPES: 'https://www.googleapis.com/auth/calendar.readonly'
    }
  },
  created () {
    this.api = gpi.gapi
    this.handleClientLoad()
  },
  methods: {
    handleClientLoad () {
      this.api.load('client:auth2', this.initClient)
    },
    initClient () {
      let vm = this
      vm.api.client.init({
        apiKey: this.API_KEY,
        clientId: this.CLIENT_ID,
        discoveryDocs: this.DISCOVERY_DOCS,
        scope: this.SCOPES
      }).then(_ => {
        vm.api.auth2.getAuthInstance().isSignedIn.listen(vm.authorized)
      })
    },

    handleAuthClick (event) {
      Promise.resolve(this.api.auth2.getAuthInstance().signIn())
        .then(_ => {
          this.authorized = true
        })
    },
    handleSignOutClick (event) {
      Promise.resolve(this.api.auth2.getAuthInstance().signOut())
        .then(_ => {
          this.authorized = false
        })
    },
    getEvents () {
      let vm = this
      vm.api.client.calendar.events.list({
        'calendarId': 'primary',
        'timeMin': (moment(this.filters.start).format('YYYY-MM-DDTHH:mm:ss.SZ')),
        'timeMax': (moment(this.filters.end).format('YYYY-MM-DDTHH:mm:ss.SZ')),
        'showDeleted': false,
        'singleEvents': true,
        'maxResults': 10,
        'orderBy': 'startTime'
      }).then(response => {
        this.items = response.result.items
      })
    }
  }
}
</script>
<style scoped>
</style>
