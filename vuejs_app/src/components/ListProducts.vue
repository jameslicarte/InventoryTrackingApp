<template>
  <div>
    <h1> Products </h1>  
    <button v-on:click="getProducts">Get Products</button>
    <b-table striped hover :items="items"></b-table>
    <table>
      <div v-bind:key="product.id" v-for="product in products">
        <tr>
          <td> {{product.id}}</td>
          <td> {{product.product_type}}</td>
          <td>{{product.color}}</td>
          <td>{{product.size}}</td>
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
      products: [
        {
          id: 1,
          product_type: 'T-Shirt',
          color: 'Red',
          size: 'Large',
          sleeve: 'Long'
        },
        {
          id: 2,
          product_type: 'T-Shirt',
          color: 'Red',
          size: 'Small', 
          sleeve: 'Long'
        },
        {
          id: 3,
          product_type: 'Car',
          make: 'Red',
          manufacturer: 'Large'
        }
      ],
      items: [
          { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
          { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
          { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
          { age: 38, first_name: 'Jami', last_name: 'Carney' }
        ]
    }
  },
  methods: {
    getProducts() {
      axios.get("http://127.0.0.1:8000/api/products/")
      .then(res => (this.products = res.data))
      .catch(err => console.log(err));
    }
  },
  // created() {
  //   this.getProducts()
  // }
}
</script>

<style scoped>

</style>

