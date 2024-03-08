const modules = import.meta.glob("./**.svelte");

let body: Array<{ title: string; link: string }> = [];
for (let path in modules) {
  let pathSanitized = path.replace(".svelte", "").replace("./", "/");
  body.push({
    title: pathSanitized.substring(pathSanitized.lastIndexOf("/") + 1),
    link: pathSanitized.includes("index")
      ? pathSanitized.replace("index", "")
      : pathSanitized,
  });
}

export const load = async () => {
  const menu = await Promise.all(body);
  return { routes: menu };
};
