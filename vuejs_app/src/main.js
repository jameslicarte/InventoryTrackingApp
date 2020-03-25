import Vue from 'vue'
import App from './App.vue'
import PortalVue from 'portal-vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import * as VeeValidate from "vee-validate";
import VueRouter from 'vue-router'

// import HelloWorld from './components/HelloWorld.vue'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VeeValidate)
Vue.use(PortalVue)
Vue.use(VueRouter)
Vue.config.productionTip = false

const router = new VueRouter({
  routes: [
    {
      path: "/",
      component: () => import("./components/ListProducts.vue")
    },
    {
      path: "/receive",
      component: () => import("./components/ReceiveShipment.vue")
    },
    {
      path: "/create",
      component: () => import("./components/CreateProductType.vue")
    },
    {
      path: "/ship",
      component: () => import("./components/ShipProduct.vue")
    },
  ],
  mode: 'history'
});

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
