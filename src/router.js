import Vue from 'vue';
import Router from 'vue-router';

import scanner from './views/scanner';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'scanner',
      component: scanner
    },

    {
      path: '/carlist',
      name: 'carlist',
      component: () => import('./views/carlist')
    },

    {
      path: '/carinfo',
      name: 'carinfo',
      component: () => import('./views/carinfo')
    },
  ],
});
