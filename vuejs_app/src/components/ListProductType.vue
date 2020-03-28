<template>
  <div>
    <table class="table table-hover">
      <thead>
        <tr >
          <th>Product Type</th>
          <th>Field1 Name</th>
          <th>Field2 Name</th>
          <th>Field3 Name</th>
        </tr>
      </thead>
      <tbody>
        <tr v-bind:key="product_type.id" v-for="product_type in product_types">
          <td> {{product_type.prodType}}</td>
          <td>{{product_type.field1_name}}</td>
          <td>{{product_type.field2_name}}</td>
          <td>{{product_type.field3_name}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "ListProductType",
  data() {
    return {
      product_types: [],
    }
  },
  methods: {
    getProducts() {
      axios.get("http://127.0.0.1:8000/api/filtered-producttypes/?ordering=-id")
      .then(res => (this.product_types = res.data))
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