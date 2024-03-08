<script lang="ts">
  import { classnames } from "$lib/data/utils";
  import { onMount } from "svelte";
  import { createEventDispatcher } from "svelte";

  export let isHandClosed: boolean = false;
  export let isHandPoint: boolean = false;
  export let isHandDetected: boolean = false;

  let video: HTMLVideoElement;
  let canvas: HTMLCanvasElement;
  let model: any;
  let error: boolean = false;

  const dispatch = createEventDispatcher();

  onMount(async () => {
    const handTrack = await import("handtrackjs" as any);
    model = await handTrack.load();

    // Attempt to start video
    try {
      await handTrack.startVideo(video);
      runDetection();
    } catch (error) {
      error = true;
      console.error("Error starting video:", error);
    }
  });

  async function runDetection() {
    if (!model) return;

    // Run detection
    const predictions = await model.detect(video);

    if (predictions && predictions.length > 0) {
      // Log predictions for debugging; remove or modify as needed
      // console.log(predictions);

      const oldClosed = isHandClosed;
      isHandClosed = predictions.some(
        (prediction: any) =>
          prediction.label === "closed" && prediction.score > 0.8
      );
      if (isHandClosed && oldClosed !== isHandClosed) {
        dispatch("handClose");
      }
      const oldPoint = isHandPoint;
      isHandPoint = predictions.some(
        (prediction: any) => prediction.label === "point"
      );
      isHandPoint = predictions.some(
        (prediction: any) =>
          prediction.label === "point" && prediction.score > 0.8
      );
      if (isHandPoint && oldPoint !== isHandPoint) {
        dispatch("handPoint");
      }
      isHandDetected = predictions.some(
        (prediction: any) =>
          prediction.label === "open" || prediction.label === "closed"
      );
    }

    // Continue detection loop
    if (!error) requestAnimationFrame(runDetection);

    model.renderPredictions(
      predictions,
      canvas,
      canvas.getContext("2d"),
      video
    );
    /* 
      canvas: reference to html canvas element where predictions are rendered.
      context: canvas 2D context
      mediasource: prediction input (img/video/canvas element) 
      */
  }

  $: if (isHandClosed && isHandDetected) {
  }
</script>

{#if !error}
  <video
    class={classnames(
      "!w-[800px] !h-[600px] border-4 rounded border-red-500 scale-y-100 -scale-x-100",
      { "border-green-500": isHandClosed && isHandDetected }
    )}
    autoplay
    bind:this={video}
    hidden
  >
    <track kind="captions" />
  </video>
{:else}
  <div
    class="w-[800px] h-[600px] bg-red-500 text-white font-bold flex items-center justify-center"
  >
    ERROR STARTING VIDEO
  </div>
{/if}
<canvas bind:this={canvas} class="w-[800px] h-[600px]" />
