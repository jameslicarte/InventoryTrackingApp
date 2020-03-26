<template>
  <div>
    <table class="table table-hover">
      <thead>
        <tr >
          <th>Product Type</th>
          <th>Product Name</th>
          <th>Field1</th>
          <th>Field2</th>
          <th>Field3</th>
        </tr>
      </thead>
      <tbody>
        <tr v-bind:key="product.id" v-for="product in products">
          <td> {{product.prodType}}</td>
          <td> {{product.product_name}}</td>
          <td>{{product.field1}}</td>
          <td>{{product.field2}}</td>
          <td>{{product.field3}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "ListProducts",
  data() {
    return {
      products: [],
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