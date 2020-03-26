<template>
  <div>
    <b-container class="bv-example-row">
      <b-row>
        <b-col>
          <div class="col-md-auto left">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">Create Product</h5>
                <form id="formProduct" @submit.prevent="checkForm">
                  <p>
                    <label for="prodType">Product Type: </label>
                    <select class="ml-2" name="prodType" id="prodType" @change="prodType_onChange($event)" v-model="prodType" >
                      <option selected="true" disabled="disabled">--Select--</option>  
                      <option v-bind:key="prodType_field.id" v-for="prodType_field in prodType_fields" v-bind:value="prodType_field.id">{{prodType_field.prodType}}</option>
                    </select>
                  </p>
                  <p>
                    <label for="product_name">Name </label>
                    <input class="ml-2" type="text" name="product_name" id="product_name" v-model="product_name">
                  </p>
                  <p>
                    <label for="field1">{{data.field1_name}} </label>
                    <input class="ml-2" type="text" name="field1" id="field1" v-model="field1">
                  </p>
                  <p>
                    <label for="field2">{{data.field2_name}} </label>
                    <input class="ml-2" type="text" name="field2" id="field2" v-model="field2">
                  </p>
                  <p>
                    <label for="field3">{{data.field3_name}} </label>
                    <input class="ml-2" v-bind:type="data.field3_type" name="field3" id="field3" v-model="field3">
                  </p>
                  <p>
                    <input class="ml-2" type="submit" value="Submit">
                  </p>
                </form>
              </div>
            </div>
          </div> 
        </b-col>
        <b-col>
          <ListProduct></ListProduct>
        </b-col>
      </b-row>
    </b-container>

    
  </div>  
</template>

<script>
import axios from 'axios';
import ListProduct from './ListProduct.vue'

export default {
  name: "createProdType",
  components:{
    ListProduct,
  },
  data() {
    return {
      prodType: "",
      product_name: "",
      field1: "",
      field2: "",
      field3: "",
      prodType_fields: [],
      myField1: "ThisField",
      data: {
        field1_name: 'Field1',
        field2_name: 'Field2',
        field3_name: 'Field3',
      },
      field1_type: 'text',
      field2_type: 'text',
      field3_type: 'text',

    }
  },
  methods: {
    checkForm() {
      // console.log(this.prodType)
      // console.log(this.product_name)
      axios.post("http://127.0.0.1:8000/api/products/",{
        prodType: this.prodType,
        product_name: this.product_name,
        field1: this.field1,
        field2: this.field2,
        field3: this.field3
      },{
        headers: {
            'Content-Type': 'application/json'
        }
      })
      .then(res => console.log(res))
      .catch(res => console.log(res.data))
    },
    getProdType() {
      axios.get("http://127.0.0.1:8000/api/producttypes/")
      .then(res => (this.prodType_fields = res.data))
      .catch(err => console.log(err));
    },
    getProdType_det(id) {
      axios.get("http://127.0.0.1:8000/api/producttypes/"+id+"/")
      .then(res => (this.data = res.data))
      .catch(err => console.log(err));
    },
    prodType_onChange(event) {
      console.log((event.target.value));
      this.getProdType_det(event.target.value);
      console.log(this.data);
    },
  },
  created() {
    this.getProdType();
  }
}

</script>

<style scoped>

</style>

