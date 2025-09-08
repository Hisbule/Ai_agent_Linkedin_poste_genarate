LinkedIn Post Generator with Local Ollama + Embeddings

This project generates professional LinkedIn posts using Gemma 3 (via Ollama) and then creates embeddings locally with nomic-embed-text. Everything runs offline with Ollama — no API keys required.

🚀 Features

Generate engaging LinkedIn posts in any language.

Uses Gemma 3:4b model via Ollama.

Create local embeddings with nomic-embed-text (for semantic search or vector databases).

100% local execution — no external API calls.

⚙️ Prerequisites
1. Install Ollama

Download and install Ollama from:
👉 https://ollama.com/download

⚠️ Important Note for Windows users:
After installation, Ollama runs in the background as a taskbar app.
To avoid Python connection errors, right-click the Ollama icon in your taskbar and exit it before running this script.
The script itself will connect to Ollama in server mode (http://localhost:11434).
