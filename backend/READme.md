# AI-Powered Blog Post Generator with Daily Automation (Gemini Edition)

A Python Flask application that generates SEO-friendly blog posts using **Google Gemini** and saves a new post automatically each day for a predefined keyword.

---

## 🚀 Features

- REST API endpoint: `GET /generate?keyword=your_topic`
- Mocked SEO metrics (search volume, difficulty, CPC)
- Blog content generated with Google Gemini (Markdown format)
- Blog posts saved to the `/posts/` directory
- Daily post automation using a shell script + cron job

---

## 🧰 Technologies Used

- Python 3.13
- Flask
- Flask-CORS
- Google Gemini API (via `google-generativeai`)
- Cron + Bash script (for daily scheduling)

---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-blog-generator-interview-yourname.git
cd backend
