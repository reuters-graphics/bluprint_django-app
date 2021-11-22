<script>
  import Nav from '@reuters-graphics/graphics-svelte-components/Nav/index.svelte';
</script>

<Nav lightLogo="{true}" monocolourLogo="{true}" backgroundColour="#4C566A" link="/" />
<article>
  <iframe title="rocket" src="https://embed.lottiefiles.com/animation/85393"></iframe>
  <section>
    <h1>Lift-off!</h1>
  </section>
</article>

<!-- svelte-ignore css-unused-selector -->
<style lang="scss">
  @import '@reuters-graphics/style-main/scss/fonts/font-faces';
  :global {
    @import '@reuters-graphics/style-theme-eisbaer/scss/main';
    nav.nav {
      box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
    }
  }

  h1 {
    font-weight: 200;
    text-align: center;
  }

  

  iframe {
    border: none;
    margin: 0 auto;
    display: block;
    pointer-events: none;
  }
</style>