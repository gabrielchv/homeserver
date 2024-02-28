import { json } from "@sveltejs/kit";
import type { RequestHandler } from "./$types";

export const POST: RequestHandler = async ({ request }) => {
  const { message }: { message: string | undefined } = await request.json();
  console.log(message);
  return json({ message: message || "error" });
};
