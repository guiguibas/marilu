<template>
  <component :is="as" :class="['typography', variationClasses]">
    <slot />
  </component>
</template>

<script>

export default {
  name: 'typography',

  props: {
    as: {
      type: String,
      default: 'p'
    },

    variation: {
      type: String,
      default: ''
    }
  },

  computed: {
    variationClasses () {
      return this.variation.length ? this.variation.split(' ').map(className => `-${className}`) : ''
    }
  }
};
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Montserrat:600,700&display=swap');

.typography {
  font-family: 'Montserrat', sans-serif;
  font-weight: 600;
  font-size: 16px;
  line-height: 20px;
  color: #414141;

  &.-label,
  &.-description {
    color: #65656E;
  }

  &.-label {
    font-size: 12px;
    line-height: 15px;
  }

  &.-description {
    font-size: 14px;
    line-height: 17px;
  }

  &.-value,
  &.-title {
    color: #414141;
  }

  &.-value {
    font-size: 20px;
    line-height: 24px;
  }

  &.-title {
    font-weight: 700;
    font-size: 24px;
    line-height: 29px;
  }

}
</style>
