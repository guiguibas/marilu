<template>
  <div class="page-header">
    <slot />
  </div>
</template>

<script>
import BancoPanLogo from '@/components/logo';

export default {
  name: 'pageheader'
};
</script>

<style lang="scss">
.page-header {
  padding: $spacing-4 $spacing-4 $spacing-5 $spacing-4;
  overflow: hidden;
  border-radius: 0px 0px 8px 8px;
  background: #fff;
}
</style>
