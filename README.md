# AI-C-Suite

A C-Suite application built with LLM agents using Agno (Phidata), Streamlit, and Google Gemini.

## Features

- **Multi-Agent Chat**: Switch between CEO, CTO, and CMO agents
- **Persistent Memory**: Conversations are stored locally via SQLite
- **Local File Operations**: CTO can scaffold projects directly to your `./workspace` folder

## Getting Started

### Prerequisites

- Python 3.10+
- A Google AI Studio API key ([Get one here](https://aistudio.google.com/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/lucvankerkvoort/AI-C-Suite.git
   cd AI-C-Suite
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment**
   ```bash
   cp .env.example .env
   ```
   
   Then edit `.env` and add your Gemini API key:
   ```
   GOOGLE_API_KEY=your_google_ai_studio_key
   ```

4. **Verify setup** (optional)
   ```bash
   python verify_setup.py
   ```

### Running the App

```bash
streamlit run app.py
```

The app will open in your browser at **http://localhost:8501**

## Usage

1. Select an agent from the sidebar (CEO, CTO, or CMO)
2. Start chatting!

### Example: Scaffold a Project

1. Select **CTO** from the dropdown
2. Ask: *"Scaffold a FastAPI app"*
3. Check the `./workspace` folder for the generated files

## Project Structure

```
AI-C-Suite/
├── app.py              # Streamlit UI
├── agents/             # Agent definitions
│   ├── ceo.py          # CEO Agent
│   └── cto.py          # CTO Agent (with FileTools)
├── memory/             # Storage configuration
│   └── storage.py      # SQLite storage
├── utils/              # Utilities
│   └── config.py       # Environment config
├── workspace/          # CTO file output directory
├── data/               # SQLite database (auto-created)
└── requirements.txt    # Dependencies
```

## License

MIT
