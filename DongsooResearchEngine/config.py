from pathlib import Path

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "data"

DB_PATH = DATA_DIR / "database.db"

FAISS_PATH = DATA_DIR / "faiss.index"

EMBEDDING_MODEL = (
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

OLLAMA_MODEL = "qwen3:8b"

SUPPORTED_EXTENSIONS = {
    ".txt",
    ".md",
    ".pdf",
    ".docx",
    ".pptx",
    ".xlsx",
    ".csv",
    ".py",
    ".cpp",
    ".java"
}