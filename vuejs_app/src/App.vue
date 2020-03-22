<template>
  <div id="app">
    <ListProducts/>
    <AddProductType/>
  </div>
</template>

<script>
import ListProducts from './components/ListProducts.vue'
import AddProductType from './components/AddProductType.vue'

export default {
  name: 'App',
  components: {
    ListProducts,
    AddProductType
  },
  data() {
    return {
      msg: ""
    }
    
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
