from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import os
from datetime import datetime
from seo_fetcher import fetch_seo_metrics
from ai_generator import generate_blog_post

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["GET"])
def generate():
    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400

    try:
        metrics = fetch_seo_metrics(keyword)
        blog_post = generate_blog_post(keyword, metrics)

        os.makedirs("posts", exist_ok=True)
        filename = f"posts/{keyword.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, "w") as f:
            f.write(jsonify({
                "keyword": keyword,
                "seo_metrics": metrics,
                "blog_post": blog_post
            }).get_data(as_text=True))

        return jsonify({
            "keyword": keyword,
            "seo_metrics": metrics,
            "blog_post": blog_post
        })
    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"error": "Internal Server Error"}), 500

@app.route("/posts/<filename>", methods=["GET"])
def serve_post(filename):
    return send_from_directory("posts", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
