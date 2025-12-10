import React, { useState, useEffect } from "react";

// Utility: interpolate between two colors
function interpolateColor(color1, color2, factor) {
  const result = color1.slice();
  for (let i = 0; i < 3; i++) {
    result[i] = Math.round(result[i] + factor * (color2[i] - color1[i]));
  }
  return result;
}

function rgbToCss(rgbArray) {
  return `rgb(${rgbArray[0]}, ${rgbArray[1]}, ${rgbArray[2]})`;
}

// Map cents to color smoothly
function getBackgroundColor(cents) {
  const absCents = Math.min(Math.abs(cents), 100); // cap at 100
  // Define gradient stops: red -> orange -> yellow -> green
  const stops = [
    [255, 0, 0],    // red
    [255, 165, 0],  // orange
    [255, 255, 0],  // yellow
    [0, 255, 0],    // green
  ];

  if (absCents < 5) return rgbToCss(stops[3]); // green
  if (absCents < 50) {
    const factor = (absCents - 5) / (50 - 5);
    return rgbToCss(interpolateColor(stops[2], stops[3], factor));
  } else {
    const factor = (absCents - 50) / (100 - 50);
    return rgbToCss(interpolateColor(stops[1], stops[2], factor));
  }
}

const Tuner = () => {
  const [frequency, setFrequency] = useState(0);
  const [note, setNote] = useState("-");
  const [cents, setCents] = useState(0);
  const [isRecording, setIsRecording] = useState(false);

  useEffect(() => {
    const interval = setInterval(async () => {
      try {
        const response = await fetch("/analyse");
        const data = await response.json();

        setFrequency(data.freq || 0);
        setNote(data.note || "-");
        setCents(data.cents || 0);
        setIsRecording(data.recording || false);
      } catch (error) {
        console.error("Error fetching analyse data:", error);
      }
    }, 300);

    return () => clearInterval(interval);
  }, []);

  const rectangleStyle = {
    width: "50%",
    height: "50vh",
    margin: "50px auto",
    padding: "20px",
    borderRadius: "15px",
    backgroundColor: getBackgroundColor(cents),
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-around",
    alignItems: "center",
    textAlign: "center",
    transition: "background-color 0.3s",
  };

  const pageStyle = {
    backgroundImage: "url('https://t3.ftcdn.net/jpg/17/74/54/14/360_F_1774541465_KGu4ylM0JNdAo7iOvWr4N8bOOiomM6O8.jpg')",
    backgroundSize: "cover",
    color: "#f5f5f5",
    minHeight: "100vh",
    fontFamily: "sans-serif",
    display: "flex",
    flexDirection: "column",
  };

  return (
    <div style={pageStyle}>
      <h1 style={{ fontFamily: "uncial antiqua", textAlign: "center", marginTop: "20px" }}>
        STAGE - SENSE TUNER (v1.0)
      </h1>
      <div style={rectangleStyle}>
        <div style={{ fontSize: "2rem" }}>
          {frequency.toFixed(2)} Hz &nbsp; ±{cents.toFixed(1)}c
        </div>
        <div style={{  fontSize: "4rem", fontWeight: "bold" }}>{note}</div>
        <div
          style={{
            width: "15px",
            height: "15px",
            borderRadius: "50%",
            backgroundColor: isRecording ? "red" : "grey",
            marginTop: "10px",
          }}
        />
      </div>
      <div style={{ fontSize: "0.8rem", textAlign: "center", marginTop: "auto", marginBottom: "10px", opacity: 0.7 }}>
        Need help? ⇒ send an email to jules.decorps@gmail.com
      </div>
    </div>
  );
};

export default Tuner;