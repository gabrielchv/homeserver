<script lang="ts">
  import type { PageData } from "./$types";

  export let data: PageData;

  $: console.log(data);
</script>

<div class="w-full h-screen bg-slate-900 flex justify-center items-center">
  {#if data.routes}
    {#each data.routes as route}
      <a
        href={route.link}
        class="text-indigo-50 hover:text-indigo-100 hover:scale-110 transition ease-in-out font-bold"
        >{route.title}</a
      >
    {/each}
  {/if}
</div>
