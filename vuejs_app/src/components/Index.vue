<template>
  <div>
    <h1> Products </h1>  
    <table>
      <div v-bind:key="product.id" v-for="product in products">
        <tr>
          <td> {{product.id}}</td>
          <td> {{product.prodType}}</td>
          <td> {{product.product_name}}</td>
          <td>{{product.field1}}</td>
          <td>{{product.field2}}</td>
          <td>{{product.field3}}</td>
          <td>{{product.sku}}</td>
          <button
              class="btn btn-danger btn-sm ml-1"
              v-on:click="deleteSubscription(subscription)">
              Delete
          </button>
          
        </tr>
      </div>
    </table>
    
  </div>  
</template>

<script>
import axios from 'axios';

export default {
  name: "Product",
  data() {
    return {
      products: []
    }
  },
  methods: {
    getProducts() {
      axios.get("http://127.0.0.1:8000/api/products/")
      .then(res => (this.products = res.data))
      .catch(err => console.log(err));
    },
  },
  created() {
    this.getProducts()
  }
}

</script>

<style scoped>

</style>

