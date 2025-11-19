export async function getPitch() {
    try {
        const response = await fetch('http://172.20.10.8:8000/pitch');
        const data = await response.json();
        return data.frequency_hz;

    } catch (err) {
        console.error('Error fetching pitch:', err);
        return null;
    }
}
