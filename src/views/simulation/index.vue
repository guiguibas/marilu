<template>
  <div id="simulation">
    <!-- HEADER -->
    <pageheader>
      <logo/>
      <typography variation="title" class="spacing-1"> SIMULAÇÃO </typography>
    </pageheader>

    <typography variation="label" class="spacing-1"> VEÍCULO </typography>
    <typography variation="title" class="spacing-1"> CHEVROLET ONIX 1.5 </typography>
    <typography variation="description" class="spacing-8"> Av.Paulista 1615 - São Paulo </typography>

    <typography variation="label" class="spacing-1"> VALOR DO FINANCIAMENTO </typography>
    <typography variation="title" class="spacing-8"> R$ 40.000,00 </typography>

    <typography variation="label" class="spacing-2"> INFORMAÇÕES PESSOAIS </typography>

    <div class="inputswrapper spacing-8">
      <box class="input-field spacing-2" variation="outline">
        <typography variation="label"> CPF </typography>
        <typography editable> 428.623.868-71 </typography>
      </box>
      <box class="input-field spacing-2" variation="outline">
        <typography variation="label"> DATA DE NASCIMENTO </typography>
        <typography editable> 26/10/1996 </typography>
      </box>
      <box class="input-field spacing-2" variation="outline">
        <typography variation="label"> CEP </typography>
        <typography editable> 12947-320 </typography>
      </box>
    </div>

    <div class="rangerwrapper spacing-8">
      <typography variation="label" class="spacing-2"> ENTRADA </typography>
      <rangeslider :min="0" :max="40000" :step="1000" />
    </div>

    <div class="parcelawrapper spacing-8">
      <typography variation="label" class="spacing-2"> PARCELAS </typography>
      
      <div class="parcelas">
        <box variation="outline" class="parcela">
          <typography variation="value"> 12x </typography>
        </box>
        <box variation="outline" class="parcela">
          <typography variation="value"> 24x </typography>
        </box>
        <box variation="outline" class="parcela">
          <typography variation="value"> 36x </typography>
        </box>
        <box variation="outline" class="parcela">
          <typography variation="value"> 48x </typography>
        </box>
        <box variation="outline" class="parcela">
          <typography variation="value"> 60x </typography>
        </box>
      </div>
    </div>

    <div class="rangerwrapper spacing-8">
      <typography variation="label" class="spacing-2"> TOKEN DE IDENIFICAÇÃO </typography>
      <typography variation="title" class="spacing-1"> VFG-4579 </typography>
    </div>

  </div>
</template>

<script>

export default {
  name: 'simulation',
  components: {
    box: () => import('@/components/box'),
    logo: () => import('@/components/logo'),
    buttonn: () => import('@/components/button'),
    pageheader: () => import('@/components/pageheader'),
    typography: () => import('@/components/typography'),
    rangeslider: () => import('@/components/rangeslider'),
    illustration: () => import('@/components/illustration')
  }
};
</script>

<style lang="scss">
#simulation {
  >.page-header {
    background: #039BE5;
    margin-bottom: 32px;

    > svg {
      margin-bottom: 32px;
      color: white;
    }

    >.typography {
      color: white;
    }
  }

  >.typography {
    padding: 0 16px;
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

  >.inputswrapper {
    padding: 0 16px;
  }

  .input-field {
    padding: 8px 16px;
  }

  .parcelawrapper,
  .rangerwrapper {
    padding: 0 16px;
  }

  .parcelas {
    display: flex;
    flex-wrap: wrap;
  }

  .parcela {
    display: flex;
    height: 77px;
    width: calc((100vw / 3) - 16px);
    justify-content: center;
    align-items: center;
    margin-bottom: 8px;
    margin-right: 8px;

    &:nth-child(3) {
      margin-right: 0;
    }
  }
}
</style>
