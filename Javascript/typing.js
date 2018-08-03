let boxes = document.querySelectorAll('div')


boxes.forEach( box =>  {

  box.addEventListener('mouseover', e => {
  box.classList.add('spin')
  })

  box.addEventListener('mouseleave', e => {
  box.classList.remove('spin')
  })

});

window.addEventListener('keydown', e => {
  if (e.key =='g' || e.key == 'G'){
    boxes.forEach(box => {
      box.classList.remove('red');
      box.classList.remove('blue');
      box.classList.add('green');
    })
  }
})


window.addEventListener('keydown', e => {
  if (e.key =='b' || e.key == 'B'){
    boxes.forEach(box => {
      box.classList.remove('red');
      box.classList.remove('green');
      box.classList.add('blue');
    })
  }
})


window.addEventListener('keydown', e => {
  if (e.key =='r' || e.key == 'R'){
    boxes.forEach(box => {
      box.classList.remove('green');
      box.classList.remove('blue');
      box.classList.add('red');
    })
  }
})


// () are called parethesis

//arrays objects mouse events forEach
