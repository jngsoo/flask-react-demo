import React from "react";
import "./App.css";
import axios from "axios";

function App() {
  const apiCall = () => {
    axios.get("/api/data").then(data => {
      console.log(data);
    });
  };
  return (
    <div className="App">
      <button onClick={apiCall}>hi</button>
    </div>
  );
}

export default App;
