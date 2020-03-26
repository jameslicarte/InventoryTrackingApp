<template>
  <div id="app">
    <b-nav tabs align="center">
      <b-nav-item>
        <router-link tag="li" to="/">Products</router-link>
      </b-nav-item>
      <b-nav-item>
        <router-link tag="li" to="/create/product">Create Product</router-link>
      </b-nav-item>
      <b-nav-item>
        <router-link tag="li" to="/create/prodtype">Create Product Type</router-link>
      </b-nav-item>
      <b-nav-item>
        <router-link tag="li" to="/reports">Reports</router-link>
      </b-nav-item>
    </b-nav>
    <router-view :key="$route.fullPath"></router-view>
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
