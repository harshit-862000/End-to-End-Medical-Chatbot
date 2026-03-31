# 🏥 End-to-End Medical Chatbot

An intelligent medical chatbot built with RAG (Retrieval-Augmented Generation) architecture using LangChain, Pinecone, and OpenRouter. The chatbot provides accurate medical information by retrieving relevant context from medical documents and generating responses using advanced language models.

## 🌟 Features

- **RAG Architecture**: Combines document retrieval with language model generation for accurate responses
- **Medical Knowledge Base**: Uses PDF medical documents as knowledge source
- **Vector Search**: Leverages Pinecone for efficient similarity search
- **Modern UI**: Clean, responsive chat interface built with Bootstrap
- **Real-time Responses**: Fast response times with streaming capabilities
- **OpenRouter Integration**: Uses OpenRouter for accessing multiple LLM providers

## 🛠️ Tech Stack

- **Backend**: Flask (Python web framework)
- **LLM Framework**: LangChain
- **Vector Database**: Pinecone
- **Embeddings**: HuggingFace (sentence-transformers/all-MiniLM-L6-v2)
- **LLM Provider**: OpenRouter (GPT-3.5-turbo)
- **Frontend**: HTML, CSS, Bootstrap, jQuery
- **Environment Management**: python-dotenv

## 📋 Prerequisites

- Python 3.10 or higher
- Conda (recommended) or virtualenv
- OpenRouter API key
- Pinecone API key

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/End-to-End-Medical-Chatbot.git
cd End-to-End-Medical-Chatbot
```

### Step 2: Create a Conda Environment

```bash
conda create -n medibot python=3.10 -y
conda activate medibot
```

Alternatively, using venv:
```bash
python -m venv medibot
source medibot/bin/activate  # On Windows: medibot\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
# Create .env file
touch .env  # On Windows: type nul > .env
```

Add your API keys to the `.env` file:

```env
# OpenRouter API Key (get from https://openrouter.ai/)
OPENAI_API_KEY=your-openrouter-api-key-here

# Pinecone API Key (get from https://www.pinecone.io/)
PINECONE_API_KEY=your-pinecone-api-key-here
```

⚠️ **Important**: Never commit the `.env` file to version control!

### Step 5: Prepare Your Medical Documents

1. Create a `Data/` directory in the project root
2. Add your medical PDF documents to this folder
3. These documents will be used as the knowledge base

### Step 6: Create Pinecone Index and Store Embeddings

Run the following script to create embeddings and store them in Pinecone:

```bash
python store_index.py
```

This will:
- Load PDF files from the `Data/` folder
- Split documents into chunks
- Generate embeddings using HuggingFace
- Create a Pinecone index named "medicalbot"
- Upload embeddings to Pinecone

### Step 7: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:8000`

## 📁 Project Structure

```
End-to-End-Medical-Chatbot/
│
├── src/
│   ├── __init__.py
│   ├── helper.py           # Helper functions for PDF loading, text splitting, embeddings
│   └── prompt.py           # System prompts for the chatbot
│
├── template/
│   └── chat.html           # Frontend chat interface
│
├── static/
│   └── style.css           # CSS styling for chat interface
│
├── Data/                   # Medical PDF documents (not in repo)
│
├── research/
│   └── trials.ipynb        # Jupyter notebook for experimentation
│
├── app.py                  # Main Flask application
├── store_index.py          # Script to create and populate Pinecone index
├── template.py             # Project structure generator
├── setup.py                # Package setup configuration
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in repo)
├── .gitignore              # Git ignore rules
├── LICENSE                 # Project license
└── README.md               # This file
```

## 🔑 Getting API Keys

### OpenRouter API Key
1. Go to https://openrouter.ai/
2. Sign up for an account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key (starts with `sk-or-v1-`)

### Pinecone API Key
1. Go to https://www.pinecone.io/
2. Sign up for a free account
3. Create a new project
4. Go to API Keys section
5. Copy your API key

## 💡 Usage

1. Open your browser and navigate to `http://localhost:8000`
2. Type your medical question in the chat input
3. Press Enter or click the send button
4. The chatbot will retrieve relevant information and generate a response

### Example Queries

```
- What is diabetes?
- What are the symptoms of hypertension?
- How is pneumonia treated?
- What causes asthma?
- Explain the difference between Type 1 and Type 2 diabetes
```

## ⚙️ Configuration

### Changing the LLM Model

Edit `app.py` and modify the `llm` configuration:

```python
llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",  # Change this to any OpenRouter-supported model
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.4,
    max_tokens=500
)
```

### Available Models on OpenRouter

- `openai/gpt-3.5-turbo` (Paid - Recommended)
- `openai/gpt-4` (Paid - Higher quality)
- `meta-llama/llama-3.2-3b-instruct:free` (Free)
- `google/gemini-flash-1.5:free` (Free)
- `mistralai/mistral-7b-instruct:free` (Free)

### Adjusting Retrieval Parameters

In `app.py`, modify the retriever settings:

```python
retriever = docsearch.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}  # Number of documents to retrieve
)
```

## 🐛 Troubleshooting

### Error: "TemplateNotFound: chat.html"
- Ensure the `template/` folder exists
- Verify `chat.html` is inside the `template/` folder
- Check `app.py` has `template_folder="template"`

### Error: "Invalid API key"
- Verify your API keys in the `.env` file
- Ensure there are no extra spaces or quotes
- Check that the `.env` file is in the project root

### Error: "Index not found"
- Run `python store_index.py` to create the Pinecone index
- Verify your Pinecone API key is correct
- Check that the index name matches in both scripts

### Slow Response Times
- Reduce the number of retrieved documents (`k` parameter)
- Use a faster LLM model
- Check your internet connection

## 🔒 Security Notes

- **Never commit `.env` file** to version control
- **Never share your API keys** publicly
- **Rotate API keys** regularly
- The `.gitignore` file is configured to exclude sensitive files

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🎥 Walkthrough Video

Watch the complete walkthrough of the Medical Chatbot to get started:




https://github.com/user-attachments/assets/2789c645-239a-43a1-9721-3d7fcc78a374


**Made with ❤️ by Harshit**
