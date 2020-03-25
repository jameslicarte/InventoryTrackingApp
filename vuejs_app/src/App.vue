<template>
  <div id="app">
    <b-nav tabs align="center">
      <b-nav-item>
        <router-link tag="li" to="/">Home</router-link>
      </b-nav-item>
      <b-nav-item>
        <router-link tag="li" to="/ship">Ship Products</router-link>
      </b-nav-item>
      <b-nav-item>
        <router-link tag="li" to="/receive">Receive Shipment</router-link>
      </b-nav-item>
    </b-nav>
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
