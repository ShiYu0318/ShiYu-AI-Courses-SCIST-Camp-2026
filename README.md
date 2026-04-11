# SCIST x SCAICT Camp 2026 聯合寒訓 - AI 系列課程

- [授課簡報](https://slides.com/shiyu/ai/)
- [學員共筆](https://hackmd.io/@SCIST/2026_camp_all_note/)

### I. AI 理論全攻略（ML/DL/RL）
> Day1 (2026/02/05) - 3 hr
此堂課程預設受眾為零基礎且對 AI 技術有興趣的同學，整體內容涵蓋經典機器學習模型、重要深度學習架構與現今技術應用，主要分為四大部分：基礎、加深、加廣、延伸，循序漸進著重講解原理，提供一個系統性的學習架構，讓學員對上百個相關名詞有初步認知，為後續實作打好基礎。

### II. 生成式 AI 應用實作 - LLM + DC BOT
> Day1 (2026/02/06) - 2 hr
此堂課程將帶領學員從將 LLM 接起來開始，以 Discord Bot 作為互動介面，結合 OpenRouter API，示範如何在真實應用情境中呼叫、管理並彈性切換多種大型語言模型；並進一步使用 Ollama 作為本地 LLM 執行環境，實際設計系統提示詞（System Prompt）與上下文工程（Context Engineering），深入理解模型推論參數對生成結果的影響，學員將能建構一個具備基本對話能力與高度擴充性的生成式 AI 應用。

### III. LLM 進階實作：RAG
> Day3 (2026/02/07) - 2.5 hr
此堂課程將聚焦於「RAG 檢索增強生成」，讓大型語言模型具備查資料能力，透過介紹 Embedding 的核心概念，建立可被語言模型即時查詢的知識庫，學員將學習如何設計檢索流程，並將取回的文件內容動態組裝成結構化 Prompt，有效降低模型幻覺並提升回覆準確性，建構出一個結合本地 LLM、向量資料庫與知識檢索機制的進階生成式 AI 應用，具備實際落地於客服、文件問答與內部知識系統的能力。

## 技術

| Layer         | Tech Stack                                 |
|--------------|---------------------------------------------|
| LLM（雲端）  | OpenRouter API（openai SDK）               |
| LLM（本地）  | Ollama + llama3.2:3b                       |
| Embedding    | google/embeddinggemma-300m（HuggingFace）  |
| 向量資料庫   | FAISS                                      |
| 文件處理     | LangChain text splitters + loaders         |
| Bot 框架     | py-cord（Discord）                         |
| 環境管理     | uv + python-dotenv                         |


## 專案結構

```
SCIST-Camp-2026/  # 專案根目錄
├── .env.example  # 環境變數檔範例
├── pyproject.toml  # Python 專案設定檔
└── src/
    ├── llm-api/  # 透過串接 API 實作 LLM 應用
    │   ├── free_models_crawler.py  # 抓取 OpenRouter 免費模型的爬蟲腳本
    │   ├── free_models.txt  # 免費模型清單
    │   └── llm_dcbot_api.py  # 透過串接 API 實作 LLM 結合 Discord Bot 應用
    ├── llm-ollama/  # 基於 Ollama 的 LLM 應用
    │   └── llm_dcbot_ollama.py  # 基於 Ollama 的 LLM 結合 Discord Bot 應用實作
    └── llm-rag/  # RAG 應用實作
        ├── build_vectordb.py  # 建構向量資料庫
        ├── embeddings.py  # 詞嵌入與查詢
        ├── llm_dcbot_ollama_rag.py  # 基於 Ollama 的 LLM 結合 Discord Bot 應用搭配 RAG 實作
        ├── faiss_db/
        │   └── index.faiss  # FAISS 向量資料庫
        └── uploads/  # 上傳 RAG 檔案的目錄
```