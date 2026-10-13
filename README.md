
# Textile Quality Studio

A simple Streamlit web application for exploring fabric composition and textile quality data.

## Features

- Interactive textile quality dashboard
- Fabric strength charts
- Good and poor quality breakdown
- Editable fabric sample table
- Download sample data as CSV
- Textile-inspired color palette
- Textile terminology and project information

## Project Files

```text
textile_streamlit_app/
├── App.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- Streamlit
- Pandas
- Plotly

## Installation

Open a terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

## Run the Application

Run this command:

```bash
streamlit run App.py
```

The application will open in your browser, usually at:

http://localhost:8501

## Upload to GitHub

1. Create a new repository on GitHub.
2. Name it textile-quality-studio.
3. Upload App.py, requirements.txt, and README.md.
4. Commit your files.

Alternatively, use Git:

```bash
git init
git add App.py requirements.txt README.md
git commit -m "Create textile quality application"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace YOUR-USERNAME and YOUR-REPOSITORY with your GitHub details.

## Deploy Online

1. Open https://share.streamlit.io/
2. Sign in with your GitHub account.
3. Create a new app.
4. Select your repository and main branch.
5. Set the main file path to App.py.
6. Click Deploy.

## Important Notes

- The application uses demonstration fabric data.
- Table changes are temporary and are not stored in a permanent database.
- Use verified production data for real manufacturing decisions.

## Technologies

- Python
- Streamlit
- Pandas
- Plotly
