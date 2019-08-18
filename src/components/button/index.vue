<template>
  <div class="button">
    <typography>
      <slot />
    </typography>
  </div>
</template>

<script>
export default {
  components: {
    typography: () => import('@/components/typography'),
  }
}
</script>

<style lang="scss">
  .button {
    width: 190px;
    margin-left: auto;

    background: #FF5630;
    border-radius: 100px;

    padding: 10px 0 7px;

    >.typography {
      text-align: center;
      color: #fff;
    }
  }
</style>
