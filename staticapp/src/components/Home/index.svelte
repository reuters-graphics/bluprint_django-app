<script>
  import { Article, Block, ToolsHeader, Theme } from '@reuters-graphics/graphics-components';
</script>

<Theme theme={{ colour: { background: 'transparent' } }}>
  <ToolsHeader borderBottom={''} />
  <Article>
    <Block>
      <iframe title="rocket" src="https://embed.lottiefiles.com/animation/85393"
      ></iframe>
      <section>
        <h1>Lift off!</h1>
      </section>
    </Block>
  </Article>
</Theme>

<style lang="scss">
  @import "@reuters-graphics/graphics-components/dist/scss/fonts/_mixins.scss";

  h1 {
    font-weight: 200;
    text-align: center;
    @include font-display;
    font-size: 2rem;
    font-weight: bold;
  }

  iframe {
    border: none;
    margin: 0 auto;
    display: block;
    pointer-events: none;
  }
</style>
