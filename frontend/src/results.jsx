function ResultView({result, isloading, error}){
    if(isloading) {
        return( 
        <div className = "loading res">
            <div className="spinjustu"/>
            <p>Analyzing image...</p>
        </div>
        );
    }
    if (error){
        return(
            <div className = "e404">
                <p>Error loading Results</p>
            </div>
        );
    }
    if (!result) return null;
    
        return(
            <div className = "noRes">
                <h2>Results</h2>
                <div className="Display-View">
                    <span className= "volume-#"> {result.volume_cm3}</span>
                    <span className = "volume-unit">cm^3</span>
                </div>
                <div className="Display-View">
                    <span className="volume-#">{result.volume_in3}</span>
                    <span className="volume-unit">in^3</span>
                </div>
                <p className ="con-info">
                    {result.con_pts} contour points detected
                </p>
            </div>
        );

}

export default ResultView;