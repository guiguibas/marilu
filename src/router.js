import Vue from 'vue';
import Router from 'vue-router';

import loading from './views/loading';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'loading',
      component: loading
    },
    {
      path: '/scanner',
      name: 'scanner',
      component: () => import('./views/scanner')
    },
  ],
});
