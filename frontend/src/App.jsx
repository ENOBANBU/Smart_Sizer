import { useState } from 'react';
import './App.css';
import UploadZone from './UploadZone';
import ScaleInput from './ScaleInput';
import results from './results';

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
    if (!selectedImage) return;
    
    const formData = new FormData();
    formData.append('file', image);
    formData.append('pixel_cm', pixelpCm);

    setIsLoad(true);
    setError(null);
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
    </div>
  );
}

export default App;