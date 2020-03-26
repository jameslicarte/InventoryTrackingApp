import Vue from 'vue'
import App from './App.vue'
import PortalVue from 'portal-vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import * as VeeValidate from "vee-validate";
import VueRouter from 'vue-router'


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
      component: () => import("./components/Products.vue")
    },
    {
      path: "/create/product",
      component: () => import("./components/CreateProduct.vue")
    },
    {
      path: "/create/prodtype",
      component: () => import("./components/CreateProductType.vue")
    },
    {
      path: "/reports",
      component: () => import("./components/Reports.vue")
    },
  ],
  mode: 'history'
});

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
