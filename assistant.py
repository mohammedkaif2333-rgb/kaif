import os
from openai import OpenAI

def main():
    # Ensure the API key is set
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not found.")
        print("Please set it using: export OPENAI_API_KEY='your-api-key'")
        return

    client = OpenAI(api_key=api_key)

    print("AI Assistant is ready! (Type 'quit' or 'exit' to stop)")
    print("-" * 50)

    # System prompt to set the behavior of the assistant
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

    while True:
        try:
            # Get user input
            user_input = input("You: ")

            # Check for exit commands
            if user_input.lower() in ['quit', 'exit']:
                print("Assistant: Goodbye!")
                break

            if not user_input.strip():
                continue

            # Add user message to conversation history
            messages.append({"role": "user", "content": user_input})

            # Get response from OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            # Extract and print assistant's reply
            assistant_reply = response.choices[0].message.content
            print(f"Assistant: {assistant_reply}")

            # Add assistant message to conversation history
            messages.append({"role": "assistant", "content": assistant_reply})

        except KeyboardInterrupt:
            print("\nAssistant: Goodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
