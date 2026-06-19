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
    <p> Uplaod an image to start volume estimation</p>
    </div>
  );
}

export default App;