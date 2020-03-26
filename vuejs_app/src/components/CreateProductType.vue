<template>
  <div>
    <b-container class="bv-example-row">
      <b-row>
        <b-col>
          <div class="col-md-auto left">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">Create Product Type</h5>
                <form id="formProduct" @submit="checkForm">
                  <!-- <p>
                    <label for="prodType">Product Type: </label>
                    <select class="ml-2" name="prodType" id="prodType" v-model="prodType">
                      <option>--Select--</option>
                      <option>T-Shirt</option>
                      <option>Shoe</option>
                      <option>Car</option>

                    </select>
                  </p> -->
                  <p>
                    <label for="prodType">Product Type </label>
                    <input class="ml-2" type="text" name="prodType" id="prodType" v-model="prodType">
                  </p>
                  <p>
                    <label for="field1">Field1 Name </label>
                    <input class="ml-2" type="text" name="field1" id="field1" v-model="field1">
                  </p>
                  <p>
                    <label for="field2">Field2 Name</label>
                    <input class="ml-2" type="text" name="field2" id="field2" v-model="field2">
                  </p>
                  <p>
                    <label for="field3">Field3 Name</label>
                    <input class="ml-2" type="text" name="field3" id="field3" v-model="field3">
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
          <ListProductType></ListProductType>
        </b-col>
      </b-row>
    </b-container>

    
  </div>  
</template>

<script>
import axios from 'axios';
import ListProductType from './ListProductType.vue'

export default {
  name: "createProdType",
  components:{
    ListProductType
  },
  data() {
    return {
      prodType: "",
      field1: "",
      field2: "",
      field3: ""
    }
  },
  methods: {
    checkForm() {
      console.log(this.prodType)
      console.log(this.field1)
      console.log(this.field2)
      console.log(this.field3)
      // console.log(this.product_name)
      axios.post("http://127.0.0.1:8000/api/producttypes/",{
        prodType: this.prodType,
        field1_name: this.field1,
        field2_name: this.field2,
        field3_name: this.field3
      },{
        headers: {
            'Content-Type': 'application/json'
        }
      })
      .then(res => console.log(res), this.$forceUpdate)
      .catch(res => console.log(res.data))
    }
  },
  created() {
    
  }
}

</script>

<style scoped>

</style>

