<script lang="ts">
  let value: string;

  const sendValue = () => {
    fetch("/api/getinfo", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ value }),
    }).then((res) => console.log(res));
  };
</script>

<div class="w-full h-screen bg-red-300 flex justify-center items-center">
  <input on:change={sendValue} type="text" bind:value />
  <a
    href="/fontes"
    class="text-rose-100 hover:text-rose-50 hover:scale-110 transition ease-in-out font-bold"
    >fontes</a
  >
</div>
