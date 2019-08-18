<template>
  <img class="illustration" :src="require(`@/assets/${this.fileName}`)" alt="">
</template>

<script>
export default {
  name: 'illustration',
  props: {
    fileName: {
      type: String,
      required: true
    }
  }
}
</script>

