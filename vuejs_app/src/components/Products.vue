<template>
  <div>
    <table class="table table-hover">
      <thead>
        <tr >
          <th v-bind:key="field.id" v-for="field in fields" v-bind:value='field.db_field'> 
            <b-button squared variant="outline-secondary" style="border-style: none;" v-on:click="getProducts_sort(field.db_field)">
              {{field.field}}
            </b-button>
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
            <b-button variant="danger" v-on:click="prompt_delete(); deleteProduct(product);" style="margin-left: 10px;">Delete</b-button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>  
</template>

<script>
import axios from 'axios';

export default {
  name: "Products",
  data() {
    return {
      products: [],
      fields: [
        {id:'1', field: 'Type', db_field: 'prodType'},
        {id:'2', field: 'Name', db_field: 'product_name'},
        {id:'3', field: 'Field1', db_field: 'field1'},
        {id:'4', field: 'Field2', db_field: 'field2'},
        {id:'5', field: 'Field3', db_field: 'field3'},
        {id:'6', field: 'SKU', db_field: 'sku'},
        {id:'7', field: 'Stock', db_field: 'stock'},
        {id:'8', field: 'Action'},
      ],
      events_data: [],
    }
  },
  methods: {
    getProducts() {
      axios.get("http://127.0.0.1:8000/api/filtered-products/?ordering=-stock")
      .then(res => (this.products = res.data))
      .catch(err => console.log(err));
    },
    getProducts_sort(db_field) {
      var new_dbfield = db_field;
      var new_orderType = '';
      //NOTE:
      // '' = ascending
      // '-' = descending
      if(this.events_data.old_orderType == '-'){
        //if this ordertype is descending
        //assign next order type to be ascending
        console.log("SORT BY DESC")
        new_orderType = ''
      }
      else{
        //if this ordertype is ascending
        //assign next order type to be descending
        console.log("SORT BY ASC")
        new_orderType = '-'
      }

      if(new_dbfield != this.events_data.old_dbfield){
        //if new column is clicked 
        //override this ordertype to ascending
        console.log("OVERIDE: New Column, SORT BY ASC")
        this.events_data.old_orderType = ''
        new_orderType = '-'
      }

      axios.get("http://127.0.0.1:8000/api/filtered-products/?ordering="+this.events_data.old_orderType+new_dbfield)
      .then(res => (this.products = res.data))
      .catch(err => console.log(err));
      console.log("--------Seperator---------")

      this.events_data.old_dbfield = db_field;
      this.events_data.old_orderType = new_orderType;
    },
    putProduct_receive(product) {
      var total_amount = product.stock + this.events_data.amount_receive
      console.log('selected_product',product)
      axios.patch("http://127.0.0.1:8000/api/products/"+product.id+"/", {
          stock: total_amount,
        },{
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(response => {
          console.log(response)
          let index = 0
          this.products.forEach((datum,idx) => {
            if (product.id == datum.id) {
              index = idx
            }
          })
          console.log('indx', index)
          this.products[index].stock = total_amount
        })
        .catch(function (error) {
          console.log(error);
        });
        
    },
    putProduct_ship(product) {
      // Check first if product.stock > amount to send
      if(product.stock < this.events_data.amount_ship){
        alert("ERROR: Stock cannot be less than 0");
      }
      else{
        var total_amount = product.stock - this.events_data.amount_ship
        // var product_id = product.id
        axios.patch("http://127.0.0.1:8000/api/products/"+product.id+"/", {
            stock: total_amount,
          },{
            headers: {
              'Content-Type': 'application/json'
            }
          })
          .then(response =>  {
            console.log(response)
            let index = 0
            this.products.forEach((datum,idx) => {
              if (product.id == datum.id) {
                index = idx
              }
            })
            console.log('indx', index)
            this.products[index].stock = total_amount
          })
          .catch(function (error) {
            console.log(error);
          }); 
      }
    },
    deleteProduct(product) {
      // Check if del_button is true, check if stock is not less than 0
      if(this.events_data.del_button){
        if(product.stock <= 0){
          axios.delete("http://127.0.0.1:8000/api/products/"+product.id+"/", {},{
              headers: {
                'Content-Type': 'application/json'
              }
            })
            .then(response => {
              console.log(response)
              let index = 0
              this.products.forEach((datum,idx) => {
                if (product.id == datum.id) {
                  index = idx
                }
              })
              console.log('indx', index)
              this.products.splice(index,1)
            })
            .catch(function (error) {
              console.log(error);
            }); 
        }
        else{
          alert("ERROR: Product with stocks cannot be deleted");
        }
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
    prompt_delete() {
      var del_button = confirm("Are you sure you want to delete this product?");
      this.events_data.del_button = del_button;
    },
  },
  created() {
    this.getProducts()
  }
}

</script>

<style scoped>

</style>

