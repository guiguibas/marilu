<template>
  <div id="carlist">
    <!-- HEADER -->
    <pageheader>
      <logo/>
      <typography variation="title"> CHEVROLET ONIX </typography>
      <rangeslider :min="20000" :max="40000" :step="1000" />
      <div class="pills">
        <box variation="outline">
          <typography variation="description"> MANUAL </typography>
        </box>
        <box variation="outline">
          <typography variation="description"> AUTOMÁTICO </typography>
        </box>
      </div>
      <div class="pills">
        <box variation="outline">
          <typography variation="description"> SEM AR </typography>
        </box>
        <box variation="outline">
          <typography variation="description"> COM AR </typography>
        </box>
      </div>
    </pageheader>

    <!-- CARS -->
    <car @click.native="teste"/>

    <!-- FOOTER -->
    <!-- Num vai ter o footer :D -->

  </div>
</template>

<script>

export default {
  name: 'carlist',
  components: {
    car: () => import('./car'),
    box: () => import('@/components/box'),
    logo: () => import('@/components/logo'),
    pageheader: () => import('@/components/pageheader'),
    typography: () => import('@/components/typography'),
    rangeslider: () => import('@/components/rangeslider'),
  },
  methods: {
    teste () {
      this.$router.push('/carinfo')
    }
  }
};
</script>

<style lang="scss">
#carlist {
  display: flex;
  flex-direction: column;
  width: 100vw;
  min-height: 100vh;

  background: #F4F4F4;

  >.page-header {
    margin-bottom: $spacing-8;

    > svg {
      margin-bottom: $spacing-8;
    }
    
    >.typography {
      &.-title {
        margin-bottom: $spacing-8;
      }
    }

    >.ranges-lider {
      margin-bottom: $spacing-8;
    }

    >.pills {
      display: flex;
      margin-bottom: $spacing-2;

      &:last-child {
        margin-bottom: $spacing-4;
      }

      >.box {
        padding: $spacing-2 $spacing-4;
        margin-right: $spacing-2;
      }
    }
  }
}
</style>
