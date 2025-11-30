import React, { useState, useEffect } from "react";


const Tuner = () => {
  // nos variables
  const [frequency, setFrequency] = useState(0);
  const [note, setNote] = useState("-");
  const [cents, setCents] = useState(0);
  const [isRecording, setIsRecording] = useState(false);

  useEffect(() => {
    // fonction de rafraichissement 
    const interval = setInterval(async () => {
      try {
        const response = await fetch("/analyse"); // appel de /analyse
        const data = await response.json();

        setFrequency(data.freq || 0);
        setNote(data.note || "-");
        setCents(data.cents || 0);
        setIsRecording(data.recording || false);
      } catch (error) {
        console.error("Error fetching analyse data:", error);
      }
    }, 300); // chaque 300ms

    // cleanup
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h2>Instrument Tuner</h2>
      <p>Note: {note}</p>
      <p>Frequency: {frequency.toFixed(2)} Hz</p>
      <p>Cents: {cents > 0 ? "+" : ""}{cents}</p>
      <p>Recording: {isRecording ? "YES" : "NO"}</p>
    </div>
  );
};

export default Tuner;
