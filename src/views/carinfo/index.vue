<template>
  <div id="carinfo">
    <!-- HEADER -->
    <pageheader>
      <logo/>
    </pageheader>

    <box class="carfoto" />

    <typography variation="title" class="spacing-1"> CHEVROLET ONIX </typography>
    <typography variation="description" class="spacing-8"> 2019 - 16 Valvulas </typography>

    <typography variation="value" class="spacing-2"> R$ 40.000,00 </typography>
    <typography variation="description" class="spacing-1"> até 60 parcelas </typography>
    <typography variation="description" class="spacing-8"> de R$ 898,54 até R$ 1.071,97 </typography>

    <typography variation="label" class="spacing-1"> VENDIDO POR </typography>
    <typography variation="title" class="spacing-1"> CAOA - Av. Paulista </typography>
    <typography variation="description" class="spacing-8"> Av.Paulista 1615 - São Paulo </typography>

    <box class="simulacao">
      <div style="display: flex;">
        <illustration fileName="simulacao.svg" style="margin-right: 16px;"/>
        <typography variation="title2"> FAÇA UMA SIMULAÇÃO AGORA! </typography>
      </div>

      <buttonn @click.native="handleButtonClick"> SIMULAR </buttonn>
    </box>

  </div>
</template>

<script>

export default {
  name: 'carinfo',
  components: {
    box: () => import('@/components/box'),
    logo: () => import('@/components/logo'),
    buttonn: () => import('@/components/button'),
    pageheader: () => import('@/components/pageheader'),
    typography: () => import('@/components/typography'),
    rangeslider: () => import('@/components/rangeslider'),
    illustration: () => import('@/components/illustration')
  },
  methods: {
    handleButtonClick () {
      this.$router.push('/simulation')
    }
  }
};
</script>

<style lang="scss">
#carinfo {
  padding: 0 $spacing-4 $spacing-8;

  >.carfoto {
    height: 185px;
    margin-bottom: $spacing-8;
    background: #C4C4C4;
    background: url('~@/assets/car.png');
    background-position: initial;
  }

  >.simulacao {
    padding: 16px 16px 16px 20px;
    box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.16), 0px 0px 2px rgba(0, 0, 0, 0.1);
  }

  .spacing-1 {
    margin-bottom: $spacing-1;
  }

  .spacing-2 {
    margin-bottom: $spacing-2;
  }

  .spacing-8 {
    margin-bottom: $spacing-8;
  }
}
</style>
