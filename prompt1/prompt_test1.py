
from google import genai



client = genai.Client(api_key="GEMINI_API_KEY")


# Starting  with a "system" instruction
system_prompt = "You are an intelligent assistant. Make sure you stay within 10 words."

# Keeping every turn as a simple string in `history`
history = [f"System: {system_prompt}"]

# Interactive loop
print("Type your messages. Type 'bye' to exit.\n")

while True:
    user_msg = input("User: ").strip()
    if not user_msg:
        continue
    if user_msg.lower() == "bye":
        print("Gemini: Goodbye 👋")
        break

    # Saving the user input
    history.append(f"User: {user_msg}")

    # Joining  the transcript into one big text block
    prompt = "\n".join(history)

    try:
        # Sending the prompt
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,

        )

        # Getting the assistant’s text
        reply = response.text.strip()

        print(f"Gemini: {reply}\n")

        # Saving assistant reply for context in the next turn
        history.append(f"Assistant: {reply}")

    except Exception as e:
        print("Error:", e)
        break
