<template>
  <box :class="['platescanner']">
    <video class="video" ref="video"/>

    <div class="hint">
      <div class="illustration">a</div>

      <div class="text">
        Escaneie a placa de um veículo
      </div>
    </div>
  </box>
</template>

<script>
import box from '@/components/box';

export default {
  name: 'platescanner',
  components: {
    box
  },
  props: {
    variation: {
      type: String,
      default: ''
    }
  },
  methods: {
    initVideoStreaming () {
      navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
          console.log(stream)
          this.$refs.video.srcObject = stream;
          this.$refs.video.play()
        })
        .catch(error => {
          console.log(error, "Something went wrong!");
        });
    }
  },
  mounted () {
    this.initVideoStreaming()
  }
};
</script>

<style lang="scss">
.platescanner {
  position: relative;
  background: #000;
  overflow: hidden;

  >.video {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  >.hint {
    @include grid();

    position: absolute;
    bottom: 0;
    padding: $spacing-4;

    color: #fff;
    background: rgba(0, 0, 0, 0.5);

    > .illustration {
      @include column(2)
    }

    > .text {
      @include column(3)
    }
  }
}
</style>
