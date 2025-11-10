import { useState } from "react";
import { getRecommendations } from "./api";

export default function App() {
  const [favorites, setFavorites] = useState([]);
  const [input, setInput] = useState("");
  const [recommendations, setRecommendations] = useState([]);

  const addFavorite = () => {
    if (input.trim() && !favorites.includes(input.trim())) {
      setFavorites([...favorites, input.trim()]);
      setInput("");
    }
  };

  const fetchRecommendations = async () => {
    const recs = await getRecommendations(favorites);
    setRecommendations(recs);
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center p-10">
      <h1 className="text-3xl font-bold mb-8 text-indigo-600">🎬 MovieMatch</h1>

      <div className="flex gap-2">
        <input
          className="border rounded px-3 py-2"
          placeholder="Enter favorite movie"
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button
          className="bg-green-600 text-white px-4 rounded"
          onClick={addFavorite}
        >
          Add
        </button>
      </div>

      <div className="mt-4 space-x-2">
        {favorites.map((movie, idx) => (
          <span
            key={idx}
            className="inline-block bg-indigo-200 px-3 py-1 rounded"
          >
            {movie}
          </span>
        ))}
      </div>

      <button
        className="mt-6 bg-blue-700 text-white px-6 py-2 rounded"
        onClick={fetchRecommendations}
      >
        Get Recommendations
      </button>

      <ul className="mt-6 list-disc list-inside w-1/2">
        {recommendations.map((rec, idx) => (
          <li key={idx}>{rec}</li>
        ))}
      </ul>
    </div>
  );
}
