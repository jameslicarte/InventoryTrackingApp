<template>
  <div>
    <h1> Products </h1>  
    <button v-on:click="getProducts">Get Products</button>
  </div>  
</template>

<script>
import axios from 'axios';

export default {
  name: "Product",
  props: ["product"],
  data() {
    return {
      products : [],
    }
  },
  methods: {
    getProducts() {
      axios.get("http://127.0.0.1:8000/api/products/")
      .then(res => (this.products = res.data))
      .catch(err => console.log(err))

    }
  }
}
</script>

<style scoped>

</style>

