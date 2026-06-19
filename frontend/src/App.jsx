import { useState } from 'react';
import './App.css';

function App() {
  const [image, setImage] = useState(null);

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
    </div>
  );
}

export default App;