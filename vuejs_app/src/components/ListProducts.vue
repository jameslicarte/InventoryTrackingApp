<template>
  <div>
    <h1> Products </h1>  
    <!-- <table>
      <div v-bind:key="product.id" v-for="product in products">
        <tr>
          <td> {{product.id}}</td>
          <td> {{product.prodType}}</td>
          <td> {{product.product_name}}</td>
          <td>{{product.field1}}</td>
          <td>{{product.field2}}</td>
          <td>{{product.field3}}</td>
          <td>{{product.sku}}</td>
          <td>{{product.stock}}</td>
        </tr>
      </div>
    </table> -->
    <table class="table table-hover">
      <thead>
        <tr >
          <th v-bind:key="field.id" v-for="field in fields"> 
            {{field.field}}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-bind:key="product.id" v-for="product in products">
          <td> {{product.prodType}}</td>
          <td> {{product.product_name}}</td>
          <td>{{product.field1}}</td>
          <td>{{product.field2}}</td>
          <td>{{product.field3}}</td>
          <td>{{product.sku}}</td>
          <td>{{product.stock}}</td>
        </tr>

      </tbody>
    </table>
    
  </div>  
</template>

<script>
import axios from 'axios';

export default {
  name: "listProduct",
  data() {
    return {
      products: [],
      fields: [
        {id:'1', field: 'Type'},
        {id:'2', field: 'Name'},
        {id:'3', field: 'Field1'},
        {id:'4', field: 'Field2'},
        {id:'5', field: 'Field3'},
        {id:'6', field: 'SKU'},
        {id:'7', field: 'Stock'},
        {id:'8', field: 'Action'},
      ]
    }
  },
  methods: {
    getProducts() {
      axios.get("http://127.0.0.1:8000/api/products/")
      .then(res => (this.products = res.data, console.log(this.products), console.log(this.items)))
      .catch(err => console.log(err));
    }
  },
  created() {
    this.getProducts()
  }
}

</script>

<style scoped>

</style>

