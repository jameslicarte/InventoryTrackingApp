<template>
  <div>
    <b-container class="bv-example-row">
      <b-row>
        <b-col>
          <div class="col-md-auto left">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">Create Product Type</h5>
                <form id="formProduct" @submit.prevent="checkForm">
                  <div class="form-group row">
                    <label class="col-sm-3 col-form-label" for="prodType">Product Type </label>
                    <div class="col-sm-8">
                      <input class="form-control" type="text" name="prodType" id="prodType" v-model="prodType" placeholder="Ex: TShirt">
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-sm-3 col-form-label" for="field1" >Field1 Name </label>
                    <div class="col-sm-8">
                      <input class="form-control" type="text" name="field1" id="field1" v-model="field1" placeholder="Ex: Size">
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-sm-3 col-form-label" for="field2" >Field2 Name</label>
                    <div class="col-sm-8">
                      <input class="form-control" type="text" name="field2" id="field2" v-model="field2" placeholder="Ex: Color">
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-sm-3 col-form-label" for="field3">Field3 Name</label>
                    <div class="col-sm-8">
                      <input class="form-control" type="text" name="field3" id="field3" v-model="field3" placeholder="Ex: Style">>
                    </div>
                  </div>
                  <div class="form-group row">
                    <input class="ml-2" type="submit" value="Submit">
                  </div>
                </form>
              </div>
            </div>
          </div> 
        </b-col>
        <b-col>
          <ListProductType :key="componentKey2"></ListProductType>
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
      componentKey2: 0,
      prodType: "",
      field1: "",
      field2: "",
      field3: ""
    }
  },
  methods: {
    checkForm() {
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
      .then(res => {
        console.log(res)
        this.forceUpdate()
      })
      .catch(res => console.log(res.data))
    },
    forceUpdate(){
      this.componentKey2 += 1  
    },
  },
  created() {
    
  }
}

</script>

<style scoped>

</style>

