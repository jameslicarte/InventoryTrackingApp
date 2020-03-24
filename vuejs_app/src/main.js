import Vue from 'vue'
import App from './App.vue'
import PortalVue from 'portal-vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import * as VeeValidate from "vee-validate";

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VeeValidate)
Vue.use(PortalVue)
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
