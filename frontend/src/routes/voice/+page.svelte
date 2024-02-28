<script lang="ts">
  import VoiceRecord from "$lib/components/VoiceRecord.svelte";
  import { devlog } from "$lib/data/utils";
  import { onMount } from "svelte";

  let audio: HTMLAudioElement;

  onMount(() => {
    devlog("teste", "var");
  });
</script>

<div
  class="h-[calc(100dvh)] flex flex-col gap-2 items-center justify-center w-full bg-cyan-50"
>
  <VoiceRecord bind:audio />
</div>
