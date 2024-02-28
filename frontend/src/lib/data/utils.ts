export const devlog = <T>(message: T) => {
  try {
    if (window)
      return fetch("/api/log", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message }),
      });
  } catch (e) {
    return 0;
  }
};
