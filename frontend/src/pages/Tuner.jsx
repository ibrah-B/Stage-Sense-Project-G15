import React, { useState, useEffect } from 'react';

const Tuner = () => {
    //nos variablees
    const [frequency, setFrequency] = useState(0);
    const [note, setNote] = useState('-') ; 
    const [cents, setCents] = useState(0);
    
    useEffect(() => {
        //notre fonction de rafraichissement
        const interval = setInterval(async () => {
            try {
                const response = await fetch ('/analyse'); //appel du backend /analyse
                const data = await response.json();

                setFrequency(data.freq || 0);
                setNote(data.note || '-');
                setCents(data.cents || 0);
                
            } catch(error) {
                console.error('Error fetching analyse data:', error);

            }
            
        }, 300); // chaque 300 ms

        //cleanup
        return () => clearInterval(interval);

    }, []);

    return (
        <div>
            <h2>Stage Sense</h2>
            <p>Note: {note}</p>
            <p>Frequency: {frequency.toFixed(2)} Hz</p>
            <p>Cents: {cents > 0 ? "+" : ''}</p>
        </div>
    );
};

export default Tuner;