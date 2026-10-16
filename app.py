# pip install anthropic
import anthropic

client = anthropic.Anthropic()  # 環境変数 ANTHROPIC_API_KEY を使用

SYSTEM = "あなたは親しみやすく自然な話し方をするアシスタントです。簡潔に答えてください。"
history = []

while True:
    user = input("あなた: ").strip()
    if user in ("quit", "exit", ""):
        break

    history.append({"role": "user", "content": user})

    print("AI: ", end="", flush=True)
    reply = ""
    with client.messages.stream(
        model="claude-sonnet-5-5",
        max_tokens=1000,
        system=SYSTEM,
        messages=history,
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            reply += text
    print()

    history.append({"role": "assistant", "content": reply})
