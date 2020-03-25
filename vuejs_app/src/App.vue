<template>
  <div id="app">
    <h1><router-link to="/">Home</router-link></h1>
    <h1><router-link to="/ship">Ship Products</router-link></h1>
    <h1><router-link to="/receive">Receive Shipment</router-link></h1>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
