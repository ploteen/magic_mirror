<template>
  <div class='corona'>
    <p>전체 확진자 {{total}} 오늘의 확진자 {{today}}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      total: 0,
      today: 0
    }
  },
  methods: {
    get_corona: function () {
      let self = this
      axios.get('/corona').then((resp) => {
        self.total = resp.data[0]
        self.today = resp.data[1]
      })
    }
  },
  mounted () {
    this.get_corona()
    setInterval(() => {
      this.get_corona()
    }, 10000000)
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
.corona {
  color: #aaa;
  font-family: 'Jua', sans-serif;
  font-size: 20px;
}
</style>
