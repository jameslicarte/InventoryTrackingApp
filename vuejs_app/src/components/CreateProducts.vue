<template>
  <div>
    <div class="col-md-6">
      <div class="card">
        <div class="card-body">
          <form id="formProduct">
            <p>
              <label for="prodType">Product Type: </label>
              <select class="ml-2"  name="prodType" id="prodType">
                <option value="KEY">--Select--</option>
                <option value="KEY">T-Shirt</option>
                <option value="KEY">Shoe</option>
                <option value="KEY">Car</option>

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
          </form>
        </div>
      </div>
    </div>
  </div>  
</template>

<script>
import axios from 'axios';

export default {
  name: "CreateProduct",
  data() {
    return {
      products: []
    }
  },
  methods: {
    postProducts() {
      axios.post("http://127.0.0.1:8000/api/products/")
      .then(res => (this.products = res.data))
      .catch(err => console.log(err));
    }
  },
  created() {
    
  }
}

</script>

<style scoped>

</style>

