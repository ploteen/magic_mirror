<template>
  <div class="home-component">
    <div class = "top left">
      <clock></clock>
      <calender></calender>
      <record></record>
    </div>
    <div class="top center">
      <corona></corona>
    </div>
    <div class ="top right">
      <weather></weather>
      <Speech></Speech>
    </div>
    <div class ="bottom center"><news></news></div>
  </div>
</template>

<script>
import Clock from './Clock'
import Calender from './Calender'
import Weather from './Weather'
import Record from './Record'
import news from './News'
import Speech from './Speech'
import Corona from './Corona'
export default {
  name: 'Main',
  components: {Clock, Calender, Weather, Record, news, Speech, Corona}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@300&display=swap');
body {
  font-family: "Roboto Condensed", sans-serif;
  background: #000000;
  overflow: hidden;
  cursor:none;
}
  /*
  Overscan for Mirror

  Top: 1.4rem
  Bottom: 2.2rem
  Left: 0rem
  Right: 2.3rem

  */

.home-component{
  position:absolute;
  padding:2.5rem;
  top:2rem;
  bottom:2rem;
  left:2rem;
  right:2rem;
}

.top,.bottom {
  position: absolute;
}

.top{
  top:1.4rem;
}
.bottom{
  bottom:2.2rem;
}
.left{
  left:0rem
}
.right{
  right:2.3rem
}
.center{
  left: 50%;
  transform: translate(-50%,0);
}
</style>
