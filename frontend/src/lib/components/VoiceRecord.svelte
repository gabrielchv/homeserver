<script lang="ts">
  import { devlog } from "$lib/data/utils";
  import IconVideoPause from "$lib/icons/IconVideoPause.svelte";
  import IconVideoPlay from "$lib/icons/IconVideoPlay.svelte";
  import classnames from "classnames";
  import { onMount } from "svelte";

  export let audio: HTMLAudioElement;

  let mediaRecorder: MediaRecorder;
  let audioChunks: Array<Blob> = [];
  let recording = false;

  async function startRecording() {
    recording = true;
    audioChunks = [];
    devlog("before");
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    } catch (e) {
      devlog(e);
    }
    devlog("after");
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = (event) => {
      audioChunks.push(event.data);
    };

    mediaRecorder.onstop = () => {
      const audioBlob = new Blob(audioChunks);
      const audioUrl = URL.createObjectURL(audioBlob);
      audio = new Audio(audioUrl);
      audio.play();
    };

    mediaRecorder.start();
  }

  function stopRecording() {
    recording = false;
    mediaRecorder.stop();
  }
</script>

<button
  class={classnames("w-20 h-20 rounded-full", {
    "bg-red-400": !recording,
    "bg-red-800 scale-125 transition-all": recording,
  })}
  on:click={recording ? stopRecording : startRecording}
>
  {#if recording}
    <IconVideoPause class="h-20 w-20 text-white" />
  {:else}
    <IconVideoPlay class="h-20 w-20 text-gray-900" />
  {/if}
</button>
