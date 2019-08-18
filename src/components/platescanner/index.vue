<template>
  <box :class="['platescanner']">
    <video class="video" ref="video"/>

    <div class="hint">
      <illustration fileName="ilustracao-placa.svg"/>

      <typography>
        Escaneie a placa de um veículo
      </typography>
    </div>
  </box>
</template>

<script>
import box from '@/components/box';
import typography from '@/components/typography';
import illustration from '@/components/illustration';

export default {
  name: 'platescanner',
  components: {
    box,
    typography,
    illustration
  },

  props: {
    variation: {
      type: String,
      default: ''
    }
  },

  methods: {
    initVideoStreaming () {
      navigator.mediaDevices.getUserMedia({video: {facingMode: {exact: "environment"}}})
        .then(stream => {
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

    background: rgba(0, 0, 0, 0.5);

    > .illustration {
      @include column(2);
      width: 100%;
    }

    > .typography {
      @include column(3);
      color: #fff;
    }
  }
}
</style>
