<template>
  <div id="loading">
    loading...
  </div>
</template>

<script>
export default {
  name: 'loading'
};
</script>

<style lang="scss">
#loading {
  @include grid();

  height: 100%;
  width: 100%;

  padding: $spacing-4;
}
</style>
