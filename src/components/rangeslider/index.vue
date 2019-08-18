<template>
  <div class="ranges-lider">

    <div class="labelwrapper">
      <div class="label">
        <typography variation="description">R$ {{ min }}</typography>
      </div>

      <div class="label">
        <typography variation="description">R$ {{ max }}</typography>
      </div>
    </div>
    
    <input class="slider" type="range" name="easteregg" id="" :min="min" :max="max" :step="step">
  </div>
</template>

<script>

export default {
  name: 'rangeslider',
  components: {
    typography: () => import('@/components/typography')
  },
  props: {
    min: {
      type: Number,
      default: 0
    },
    max: {
      type: Number,
      default: 1
    },
    step: {
      type: Number,
      default: 1
    },
  }
};
</script>

<style lang="scss">
.ranges-lider {
  display: flex;
  flex-direction: column;

  >.labelwrapper {
    display: flex;

    >.label {
      width: 50%;
      margin-bottom: $spacing-2;

      &:nth-child(2) {
        text-align: right;
      }
    }
  }

  >.slider {
    display: flex;
    -webkit-appearance: none;
    width: 100%;
    height: 10px;
    border-radius: 8px;
    margin: 8px 0;
    background: #00CC88;
    outline: none;
    transition: opacity .2s;

    &::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: #FFFFFF;
      box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.16), 0px 0px 2px rgba(0, 0, 0, 0.1);
      cursor: pointer;
    }
  }
}
</style>
