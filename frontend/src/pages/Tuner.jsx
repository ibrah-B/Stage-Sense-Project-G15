import {useEffect, useState } from "react";
import {getPitch} from "../services/api";

export default function Tuner() {
    const [frequency, setFrequency] = unesState(0);

    useEffect(() => {
        const interval = setInterval(async () => {
            const freq = await getPitch();
            if (freq) setFrequency(freq);
        }, 200); // reinitialiser (poll) toutes les 200ms pour avoir un site internet LIVE

        return () => clearInterval(interval);
    }, []);

    return (
        <div>
            <h1>STAGE SENSE</h1>
            <p>Frequency: {frequency.toFixed(2)} Hz</p>
            </div>
    );
}