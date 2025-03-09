# Python to Flowchart Converter

This is a web-based tool that converts Python code into a flowchart.

## 🚀 Features
- Enter Python code or upload a `.py` file
- Generates a flowchart using `flowchart.js`
- Backend built with FastAPI
- Deployable via GitHub Pages (Frontend) & Render/Vercel (Backend)

## 🛠 Setup

### 1️⃣ Clone the repository
```sh
git clone https://github.com/your-username/python-to-flowchart.git
cd python-to-flowchart
```

### 2️⃣ Install dependencies
```sh
pip install -r backend/requirements.txt
```

### 3️⃣ Run the backend
```sh
bash run.sh
```

### 4️⃣ Deploy Frontend on GitHub Pages
```sh
git checkout --orphan gh-pages
git rm -rf .
cp -r frontend/* .
git add .
git commit -m "Deploy frontend"
git push origin gh-pages
```

### 5️⃣ Deploy Backend on Render
- Connect GitHub repo to Render  
- Use `backend/render.yaml` for setup

Enjoy! 🚀
