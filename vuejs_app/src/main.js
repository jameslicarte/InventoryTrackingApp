import Vue from 'vue'
import App from './App.vue'
import PortalVue from 'portal-vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import bootstrapvue from 'bootstrap-vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(bootstrapvue)
Vue.use(PortalVue)
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
