import { useState } from 'react';
import './App.css';
import UploadZone from './UploadZone';
import ScaleInput from './ScaleInput';
import ResultView from './results';
import axios from 'axios';

const API_URL = 'http://localhost:8000';

function App() {
  const [image, setImage] = useState(null);
  const [pixelpCm, setPixelpCm] = useState(48)
  const [result, setResult] = useState(null)
  const [isload, setIsLoad] = useState(false)
  const [error, setError] = useState(null)

  function handleImageUpload(file){
    setImage(file);
    setResult(null);
    setError(null);
  }

  async function handleScan(){
    if (!image) return;
    
    const formData = new FormData();
    formData.append('file', image);
    formData.append('pixels_per_cm', pixelpCm);

    setIsLoad(true);
    setError(null);

    try{
      const response = await axios.post(`${API_URL}/scan`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      console.log('API response:', response.data);
      setResult(response.data);
    } catch (err) {
      console.log('Full error:', err);
      console.log('Response:', err.response);
      console.log('Detail:', err.response?.data?.detail);
      setError(err.response?.data?.detail || 'Could not reach the API');
    } finally {
      setIsLoad(false);
    }
  }
  

  return(
  <div className="app">
    <h1>Smart-Sizer</h1>
    <p> Upload an image to start volume estimation</p>

    <UploadZone onImageSelected={handleImageUpload} />
    {image && (
      <p>Selected: {image.name}</p>
    )}
    <ScaleInput
    pixelpCm={pixelpCm}
    scaleChange={setPixelpCm}
    />

    <button
      className="scan-btn"
      onClick={handleScan}
      disabled={!image || isload}
      >
        {isload ? 'Scanning...' : 'Scan object'}
      </button>

      <ResultView
      result={result}
      isloading={isload}
      error={error}
      />
    </div>
  );
}

export default App;