<script lang="ts">
  import IconVideoPause from "$lib/icons/IconVideoPause.svelte";
  import IconVideoPlay from "$lib/icons/IconVideoPlay.svelte";
  import classnames from "classnames";

  export let audio: HTMLAudioElement;

  let mediaRecorder: MediaRecorder;
  let audioChunks: Array<Blob> = [];
  let recording = false;
  let downloadUrl = ""; // Add a variable for the download URL
  let downloadLinkName = "recording.webm"; // Set a default download name

  async function startRecording() {
    recording = true;
    audioChunks = [];
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = (event) => {
      audioChunks.push(event.data);
    };

    mediaRecorder.onstop = () => {
      const audioBlob = new Blob(audioChunks, { type: "audio/webm" }); // Specify the MIME type
      const audioUrl = URL.createObjectURL(audioBlob);
      audio = new Audio(audioUrl);
      audio.play();
      downloadUrl = audioUrl; // Update the download URL
    };

    mediaRecorder.start();
  }

  function stopRecording() {
    recording = false;
    mediaRecorder.stop();
  }
</script>

<!-- Add a download link to your component's HTML -->
<a href={downloadUrl} download={downloadLinkName} class="button"
  >Download Recording</a
>

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
