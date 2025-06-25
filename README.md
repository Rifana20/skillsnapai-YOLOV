

---

````markdown
# 📊 SkillSnap AI

**SkillSnap AI** is an AI-powered LinkedIn profile optimizer that helps professionals enhance their profile with:
- ✅ Optimized LinkedIn headlines
- 📝 Polished "About Me" sections
- 📸 Profile picture face detection using YOLOv8
- 💬 AI-generated networking/connection messages

---

## 🚀 Features

- **LinkedIn PDF Parser** – Extract and improve your current headline and about section.
- **AI-Powered Rewriting** – Uses Cohere LLMs to rewrite sections professionally.
- **Face Detection** – Upload your profile image and detect how many people are in frame.
- **Networking Assistant** – Get a tailored LinkedIn connection message based on your target role.

---

## 🛠️ Tech Stack

- `Streamlit` – Frontend UI
- `Cohere` – Large Language Model API
- `YOLOv8` (Ultralytics) – Face detection
- `pdfminer.six` – PDF text extraction
- `Python-dotenv` – Key management

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/skillsnapai.git
cd skillsnapai
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
````

---

## 🔑 Setup API Keys

Create a `.env` file:

```env
COHERE_API_KEY=your_real_key_here
```

Place it in the root of the project. This keeps your keys secure and hidden from version control.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
skillsnapai/
│
├── app.py                     # Main Streamlit app
├── llm_module.py              # Cohere integration for rewriting
├── networking_assistant.py    # AI connection message assistant
├── image_analyzer.py          # YOLOv8 face detection
├── pdf_parser.py              # PDF to text parsing
├── requirements.txt           # Required packages
├── .env                       # (Not committed) API key
├── .gitignore
└── yolov8s.pt                 # YOLO model file
```

---

## 🤝 Contributing

Pull requests and suggestions are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is under the [MIT License](LICENSE).

---

## 📬 Contact

Built with ❤️ by **Rifana Sherin**
Feel free to connect on [LinkedIn](https://www.linkedin.com/in/rifanasherin)

```

---

## ✅ Next Steps (Optional but Great):

- ✅ Add a `LICENSE` file (MIT is good for open-source).
- ✅ Add a `demo.gif` or short screen recording in `README`.
- ✅ Add error handling for file formats and long inputs.
- ✅ Optionally replace `YOLOv8s.pt` with `YOLOv8n.pt` (nano version) for faster inference.

---

Let me know if you'd like help creating a logo, adding themes to Streamlit, or deploying this on the cloud (like **Streamlit Community Cloud**, **Render**, or **Railway**).
```
