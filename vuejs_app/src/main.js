import Vue from 'vue'
import Router from "vue-router";
// import App from './App.vue'
import PortalVue from 'portal-vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import * as VeeValidate from 'vee-validate'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VeeValidate)
Vue.use(PortalVue)
Vue.config.productionTip = false


export default new Router({
  routes: [
    {
      path: "/",
      redirect: '/index'
    },
    {
      path: "/create",
      name: "create",
      component: () => import("./components/CreateProducts.vue")
    },
    {
      path: "/edit/:id",
      name: "edit",
      component: () => import("./components/EditProducts.vue")
    },
    {
      path: "/index",
      name: "index",
      component: () => import("./components/Index.vue")
    },
  ]
});

// new Vue({
//   render: h => h(App),
// }).$mount('#app')
