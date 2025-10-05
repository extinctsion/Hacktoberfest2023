const display = document.getElementById('display');
const pads = document.querySelectorAll('.drum-pad');

pads.forEach(pad => {
  pad.addEventListener('click', () => playSound(pad));
});

document.addEventListener('keydown', (e) => {
  const key = e.key.toUpperCase();
  const pad = Array.from(pads).find(p => p.innerText === key);
  if (pad) playSound(pad);
});

function playSound(pad) {
  const audio = pad.querySelector('audio');
  audio.currentTime = 0;
  audio.play();
  display.innerText = pad.id;
}
