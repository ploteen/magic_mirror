<template>
  <div>
    <transition name='fade'>
      <p class='news' v-if='show'>{{news[idx]}}</p>
    </transition>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      news: [],
      show: true,
      idx: 0
    }
  },
  methods: {
    get_news: function () {
      let self = this
      axios.get('http://localhost:8000/news').then((resp) => {
        for (const key in resp.data) {
          self.news.push(resp.data[key])
        }
      })
    },
    change_news: function () {
      if (this.show === true) {
        this.show = false
      } else if (this.show === false) {
        this.show = true
        let self = this
        this.idx = Number(this.idx + 1) % Number(this.news.length)
        console.log(self.idx)
      }
    }
  },
  mounted () {
    this.get_news()
    setInterval(() => {
      this.get_news()
    }, 100000)
    setInterval(() => {
      this.change_news()
    }, 2000)
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
.fade-enter-active, .fade-leave-active {
  transition: opacity 1s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
.news {
  color: #aaa;
  font-family: 'Jua', sans-serif;
  font-size: 20px;
}
</style>
