<script>
  import Nav from '@reuters-graphics/graphics-svelte-components/Nav/index.svelte';
</script>

<Nav lightLogo="{false}" backgroundColour="#fff" />
<article>
  <section>
    <h1>Welcome to your app!</h1>
  </section>
</article>

<!-- svelte-ignore css-unused-selector -->
<style lang="scss">
  @import '@reuters-graphics/style-main/scss/fonts/font-faces';
  :global {
    @import '@reuters-graphics/style-theme-eisbaer/scss/main';
  }
</style>