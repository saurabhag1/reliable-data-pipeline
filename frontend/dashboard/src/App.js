import React, { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState([]);
  const [status, setStatus] = useState({});

  useEffect(() => {
    fetch("http://localhost:8000/crypto")
      .then(res => res.json())
      .then(setData);

    fetch("http://localhost:8000/status")
      .then(res => res.json())
      .then(setStatus);
  }, []);

  const avgPrice =
    data.length > 0
      ? (data.reduce((sum, item) => sum + item[3], 0) / data.length).toFixed(2)
      : 0;

  return (
    <div style={{ padding: "20px" }}>
      <h2>Crypto Dashboard</h2>
      <p><b>Pipeline Status:</b> {status.status}</p>
      <p><b>Last Run:</b> {status.last_run}</p>
      <p><b>Total Coins:</b> {data.length}</p>
      <p><b>Average Price (USD):</b> ${avgPrice}</p>

      <table border="1" cellPadding="5">
        <thead>
          <tr>
            <th>Name</th>
            <th>Symbol</th>
            <th>USD</th>
            <th>INR</th>
          </tr>
        </thead>
        <tbody>
          {data.map(row => (
            <tr key={row[0]}>
              <td>{row[1]}</td>
              <td>{row[2]}</td>
              <td>${row[3]}</td>
              <td>₹{row[4]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
