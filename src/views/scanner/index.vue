<template>
  <div id="scanner">
    <pageheader>
      <logo/>
    </pageheader>

    <div class="content">
      <platescanner/>
    </div>

  </div>
</template>

<script>
import platescanner from '@/components/platescanner';
import pageheader from '@/components/pageheader';
import logo from '@/components/logo';

export default {
  name: 'scanner',
  components: {
    platescanner,
    pageheader,
    logo
  }
};
</script>

<style lang="scss">
#scanner {
  display: flex;
  flex-direction: column;
  width: 100vw;
  height: 100vh;

  >.content {
    padding: $spacing-4;
    padding-top: 0;
    height: 100%;

    >.platescanner {
      height: 100%;
    }
  }
}
</style>
