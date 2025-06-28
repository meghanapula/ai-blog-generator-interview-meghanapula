import { useState } from "react";
import { useRouter } from "next/router";

export default function BlogForm() {
  const [keyword, setKeyword] = useState("");
  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch(`http://localhost:5001/generate?keyword=${encodeURIComponent(keyword)}`);
    const data = await res.json();

    if (data.blog_post) {
      const id = `${keyword.replace(/\\s+/g, '_')}_${Date.now()}.json`;
      localStorage.setItem(id, JSON.stringify(data));
      router.push(`/blog?id=${id}`);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-xl mx-auto mt-20">
      <input
        type="text"
        value={keyword}
        onChange={(e) => setKeyword(e.target.value)}
        placeholder="Enter a blog topic..."
        className="w-full border p-3 rounded mb-4"
      />
      <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">
        Generate Blog
      </button>
    </form>
  );
}
