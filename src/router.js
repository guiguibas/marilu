import Vue from 'vue';
import Router from 'vue-router';

import Loading from './views/loading';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Loading',
      component: Loading
    },
    {
      path: '/scanner',
      name: 'Scanner',
      component: () => import('./views/scanner')
    },
  ],
});
