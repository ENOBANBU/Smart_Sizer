import { useState } from 'react';
import './App.css';
import UploadZone from './UploadZone';
import ScaleInput from './ScaleInput';

function App() {
  const [image, setImage] = useState(null);
  const [pixelpCm, setPixelpCm] = useState(48)

  function handleImageUpload(file){
    setImage(file);
    console.log('Image uploaded:', file.name);
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