import { useState } from "react";
import "./App.css";

function App() {
  const [value, setValue] = useState("");
  const [summary, setSummary] = useState("");


// Detect backend URL automatically
const hostname = window.location.hostname;
let BackEndAPI;

if (hostname === "localhost" || hostname === "127.0.0.1") {
  BackEndAPI = "http://localhost:8000/info";
} else {
  BackEndAPI = `http://${hostname}:8000/info`;
}


  async function fetchInfo() {
    setSummary("Fetching info… please wait ✨");

    const response = await fetch(BackEndAPI, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: value }),
    });

    const data = await response.json();
    setSummary(data.summary || "Sorry, no information found.");
  }

  return (
    <div className="appContainer">
      <header className="appHeader">
        <h1>
          🎬 Movie & Series Insight Finder
        </h1>
        <p>
          Discover detailed insights about your favorite movie or show — powered by AI.
        </p>
      </header>

      <div className="inputSection">
        <input
          type="text"
          placeholder="Enter the name of a movie or TV series"
          value={value}
          onChange={(e) => setValue(e.target.value)}
        />
        <button onClick={fetchInfo}>Get Details</button>
      </div>

      <section className="summaryOutput">
        <h3>📘 Response</h3>
        <div className="summaryBox">
          {summary
            ? summary.split(/(?<=\.)\s+/).map((line, index) => (
                <p key={index}>{line}</p>
              ))
            : <p>Enter a title to begin!</p>}
        </div>
      </section>

      <footer>
        <p>Built with 💡 FastAPI + React by <strong>Subhasis Kalia</strong></p>
      </footer>
    </div>
  );
}

export default App;
