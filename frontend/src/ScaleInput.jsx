function ScaleInput({ pixelpCm, scaleChange}){
return (
    <div className="scale-input">
        <label htmlFor="scale">
            Reference scale (Picxels per cm)
        </label>
        <input
        id = "scale"
        type="number"
        min="1"
        value={pixelpCm}
        onChange={(e) => scaleChange(Number(e.target.value))}
        placeholder="e.g. 48"
        />
        <p className="scale-hint">
            Measure object in photo. 10cm per 1, Convert cm px.
        </p>
    </div>
);

}
export default ScaleInput