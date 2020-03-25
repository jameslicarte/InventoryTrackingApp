<template>
  <div>
    <div class="col-md-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">CreAAAAA Type</h5>
          <form id="formProduct" @submit.prevent="checkForm">
            <p>
              <label for="prodType">Product Type: </label>
              <select class="ml-2" name="prodType" id="prodType" v-model="prodType">
                <option>--Select--</option>
                <option>T-Shirt</option>
                <option>Shoe</option>
                <option>Car</option>

              </select>
            </p>
            <p>
              <label for="product_name">Product Type </label>
              <input class="ml-2" type="text" name="product_name" id="product_name" v-model="product_name">
            </p>
            <p>
              <label for="field1">Field1 </label>
              <input class="ml-2" type="text" name="field1" id="field1" v-model="field1">
            </p>
            <p>
              <label for="field2">Field2 </label>
              <input class="ml-2" type="text" name="field2" id="field2" v-model="field2">
            </p>
            <p>
              <label for="field3">Field3 </label>
              <input class="ml-2" type="text" name="field3" id="field3" v-model="field3">
            </p>
            <p>
              <input class="ml-2" type="submit" value="Submit">
            </p>
          </form>
        </div>
      </div>
    </div>
  </div>  
</template>

<script>
import axios from 'axios';

export default {
  name: "createProdType",
  data() {
    return {
      prodType: "",
      product_name: "",
      field1: "",
      field2: "",
      field3: ""

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
    }
  },
  created() {
    
  }
}

</script>

<style scoped>

</style>

