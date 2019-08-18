<template>
  <component :is="as" :class="['box', variationClasses]">
    <slot />
  </component>
</template>

<script>

export default {
  name: 'box',

  props: {
    as: {
      type: String,
      default: 'div'
    },

    variation: {
      type: String,
      default: ''
    }
  },

  computed: {
    variationClasses () {
      return this.variation.length ? `-${this.variation}` : ''
    }
  }
};
</script>

<style lang="scss">
.box {
  border-radius: 5px;

  &.-shadow {
    box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.16), 0px 0px 2px rgba(0, 0, 0, 0.1);
  }

  &.-outline {
    border: 1px solid #BBBBBB;
  }
}
</style>
