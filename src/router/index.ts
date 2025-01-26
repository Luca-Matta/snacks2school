import { createRouter, createWebHistory } from "@ionic/vue-router";
import { RouteRecordRaw } from "vue-router";
import index from "../../pages/index.vue";
import login from "../../pages/login.vue";
import groupChoice from "../../pages/group-choice.vue";
import signupCustomer from "../../pages/signup-customer.vue";
import signupSchoolStaff from "../../pages/signup-school-staff.vue";
import store from "../../pages/stores/[username].vue";
import profile from "../../pages/profile.vue";
import ordersRetrieve from "../../pages/orders/retrieve.vue";
import ordersReceipts from "../../pages/orders/receipts.vue";
import ordersManagement from "../../pages/orders/index.vue";

const routes: Array<RouteRecordRaw> = [
  { path: "/", name: "Home", component: index },
  { path: "/login", name: "Login", component: login },
  { path: "/group-choice", name: "GroupChoice", component: groupChoice },
  {
    path: "/signup-customer",
    name: "SignupCustomer",
    component: signupCustomer,
  },
  {
    path: "/signup-school-staff",
    name: "SignupSchoolStaff",
    component: signupSchoolStaff,
  },
  { path: "/profile", name: "Profile", component: profile },
  {
    path: "/store/:username",
    name: "Store",
    component: store,
    props: (route) => ({
      first_name: route.query.first_name,
      last_name: route.query.last_name,
      profile_picture: route.query.profile_picture,
      location: route.query.location,
      address: route.query.address,
      bio: route.query.bio,
    }),
  },
  { path: "/orders", name: "OrdersManagement", component: ordersManagement },
  {
    path: "/orders-retrieve",
    name: "OrdersRetrieve",
    component: ordersRetrieve,
  },
  {
    path: "/orders-receipts",
    name: "OrdersReceipts",
    component: ordersReceipts,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
