export const devlog = (
  message: string | any,
  variableName: string | null = null
) => {
  try {
    if (window) {
      if (typeof message === "string" && !!variableName)
        message = `\x1b[36m${variableName}:\x1b[35m ${message}\x1b[0m`;

      return fetch("/api/log", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message }),
      });
    }
  } catch (e) {
    return 0;
  }
};
