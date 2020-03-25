<template>
  <div>
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
          <td>
            <b-button variant="primary" v-on:click="promptAmount_receive(); putProduct_receive(product);">Receive</b-button>
            <b-button variant="primary" v-on:click="promptAmount_send(); putProduct_ship(product);" style="margin-left: 10px;" >Send</b-button>
          </td>
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
      ],
      events_data: [],
    }
  },
  methods: {
    getProducts() {
      axios.get("http://127.0.0.1:8000/api/products/")
      .then(res => (this.products = res.data))
      .catch(err => console.log(err));
    },
    putProduct_receive(product) {
      var total_amount = product.stock + this.events_data.amount_receive
      axios.patch("http://127.0.0.1:8000/api/products/"+product.id+"/", {
          stock: total_amount,
        },{
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(function (response) {
          console.log(response, this.events_data.amount_receive);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    putProduct_ship(product) {
      // Check first if product.stock > amount to send
      if(product.stock < this.events_data.amount_ship){
        console.log("ERROR! Stock cannot be less than 0");
      }
      else{
        var total_amount = product.stock - this.events_data.amount_ship;
        axios.patch("http://127.0.0.1:8000/api/products/"+product.id+"/", {
            stock: total_amount,
          },{
            headers: {
              'Content-Type': 'application/json'
            }
          })
          .then(function (response) {
            console.log(response, this.events_data.amount_ship);
          })
          .catch(function (error) {
            console.log(error);
          }); 
      }

    },
    promptAmount_receive() {
      var amount = parseInt(prompt("Please enter amount to receive", 0));
      if (amount != null) {
        this.events_data.amount_receive = amount;
        console.log(amount);
      }
    },
    promptAmount_send() {
      var amount = parseInt(prompt("Please enter amount to ship", 0));
      if (amount != null) {
        this.events_data.amount_ship = amount;
        console.log(amount);
      }
    },
  },
  created() {
    this.getProducts()
  }
}

</script>

<style scoped>

</style>

