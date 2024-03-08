<script lang="ts">
  import HandTrack from "$lib/components/HandTrack.svelte";
  let isHandClosed: boolean;
  let isHandDetected: boolean;

  let counter = 0;
  setInterval(() => {
    counter += 0.1;
  }, 100);
</script>

<span class="text-2xl font-bold">{counter.toFixed(1)}</span>
<HandTrack
  bind:isHandClosed
  bind:isHandDetected
  on:handPoint={() => (counter = -2)}
/>
