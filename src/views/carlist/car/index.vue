<template>
  <div class="car">
    <box as="img" src=""/>

    <div class="contentwrapper">
      <div class="namewrapper">
        <typography variation="title2"> CHEVROLET ONIX 1.5 </typography>
        <illustration fileName="seta.svg"/>
      </div>

      <typography variation="description"> R$ 40,000.00 </typography>
      <typography variation="description"> CAOA - Av. Paulista </typography>
    </div>
  </div>
</template>

<script>

export default {
  name: 'car',
  components: {
    typography: () => import('@/components/typography'),
    illustration: () => import('@/components/illustration'),
    box: () => import('@/components/box')
  }
};
</script>

<style lang="scss">
.car {
  @include grid;

  padding: 0 $spacing-4;

  > .box {
    @include column(2);
    background: gray;
    height: 128px;
  }

  > .contentwrapper {
    @include column(3);
    margin-top: $spacing-4;

    >.namewrapper {
      display: flex;
      margin-bottom: $spacing-1;

      >.typography {
        &.-title2 {
          margin-right: $spacing-4;
        }
      }

      > .illustration {
        width: 24px;
        height: 24px;
        margin: 9px calc(9px + 16px) 9px 0;
      }
    }

    >.typography {
      margin-bottom: $spacing-1;
    }
  }
}
</style>
