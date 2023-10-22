import { useState } from 'react';
import './App.css';

function App() {

  const [Horiz, setHoriz] = useState(10)
  const [Vert, setVert] = useState(10)
  const [Blur, setBlur] = useState(10)
  const [Color, setColor] = useState('Black')
  const [Check, setCheck] = useState(false)


  return (
    <div className='container'>
      <h1 className='text-center mt-4'>Box Shadow Generator</h1>
      <p className='text-center text-secondary'>This is simple box shadow genrator developed to help front-end developers generate box shadows according to their needs.</p>
      <div className="App">
      <div className='row mt-5'>
      <div className='controls col-md-6 d-flex flex-row justify-content-around'>
        <div>
        <label for="horizDis" class="form-label">Horizontal Distance</label>
        <input type="range" class="form-range" id="horizDis" min="-200" max="200" value={Horiz} onChange={(e)=>setHoriz(e.target.value)}/>

        <label for="customRange1" class="form-label">Vertical Distance</label>
        <input type="range" class="form-range" id="customRange1" min="-200" max="200" value={Vert} onChange={(e)=>setVert(e.target.value)}/>

        <label for="customRange1" class="form-label">Blur</label>
        <input type="range" class="form-range" id="customRange1" value={Blur} onChange={(e)=>setBlur(e.target.value)}/>

        <label for="customRange1" class="form-label">Shadow Color</label>
        <input type="color" class="form-control" id="customRange1" value={Color} onChange={(e)=>setColor(e.target.value)}/>

        <div class="form-check form-switch mt-3">
          <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault" checked={Check} onChange={(e)=>setCheck(e.target.checked)} />
          <label class="form-check-label" for="flexSwitchCheckDefault">Inset</label>
        </div>
        </div>

      </div>
      <div className='output col-md-6'>
        <div className='box d-flex flex-column justify-content-around text-center' style={{boxShadow:`${Check ?"inset":""} ${Horiz}px ${Vert}px ${Blur}px ${Color}`}}>
          <p className='outputP'>box-shadow :{Check ?"inset":""} {Horiz}px {Vert}px {Blur}px {Color};</p>
        </div>
      </div>
      </div>
    </div>
    </div>
  );
}

export default App;
