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
      path: '/scanner',
      name: 'scanner',
      component: () => import('./views/scanner')
    },
  ],
});
