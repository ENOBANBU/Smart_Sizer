import {useCallback} from 'react';
import {useDropzone} from 'react-dropzone';

function UploadZone({onImageSelected}) {
    const onDrop = useCallback(acceptedFiles => {
        const file = acceptedFiles[0];
        if (file) {
            onImageSelected(file);
        }
    }, [onImageSelected]);
    const { getRootProps, getInputProps, isDragActive} = useDropzone({ onDrop, accept:{ 'image/png': [],}, multiple: false,});
    return (
        <div {...getRootProps()} className={`upload-zone ${isDragActive ? 'active' : ''}`}>
            <input {...getInputProps()} />
            {isDragActive ? (<p>Drop the image here...</p> ):( <p>Drag and drop an image here, or click to select one</p>)}
            </div>
    );
}

export default UploadZone;