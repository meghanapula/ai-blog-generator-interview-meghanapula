import { useEffect, useState } from "react";
import { useRouter } from "next/router";

export default function BlogDetail() {
  const router = useRouter();
  const { id } = router.query;
  const [post, setPost] = useState(null);

  useEffect(() => {
    if (!id) return;

    const local = localStorage.getItem(id);
    if (local) {
      setPost(JSON.parse(local));
    } else {
      fetch(`http://localhost:5001/posts/${id}`)
        .then((res) => res.json())
        .then((data) => setPost(data))
        .catch((err) => console.error("Error loading blog:", err));
    }
  }, [id]);

  if (!post) return <p className="text-center mt-10">Loading blog...</p>;

  return (
    <div className="max-w-3xl mx-auto p-6 bg-white mt-10 shadow-lg rounded-xl">
      <h1 className="text-3xl font-bold mb-4 capitalize">{post.keyword}</h1>
      <pre className="whitespace-pre-wrap text-gray-800">{post.blog_post}</pre>
    </div>
  );
}
