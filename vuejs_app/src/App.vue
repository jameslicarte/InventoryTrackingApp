<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <h2>
          <router-link to="/index">Products</router-link>
        </h2>
        <router-link to="/create" class="btn btn-sm btn-primary">Add Product</router-link>
      </div>
    </div>
  </div>
</template>

<script>
// import ListProducts from './components/ListProducts.vue'
// import CreateProducts from './components/CreateProducts.vue'
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
