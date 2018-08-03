let rightButton = document.querySelector('#right');
let leftButton = document.querySelector('#left')
let upButton = document.querySelector('#up')
let downButton = document.querySelector('#bottom')
let box = document.querySelector('#box');


rightButton.addEventListener('click', e => {
  let currentLeft = box.style.left;
  console.log('currentLeft = ' + currentLeft);
  let newLeft = parseInt(currentLeft) + 10;
  box.style.left = newLeft + 'px';

})

leftButton.addEventListener('click', e => {
  let currentRight = box.style.left;
  console.log('currentRight = ' + currentRight);
  let newRight = parseInt(currentRight) - 10;
  box.style.left = newRight + 'px';
})

upButton.addEventListener('click', e => {
  let currentUp = box.style.top;
  console.log('currentUp = ' + currentUp);
  let newUp = parseInt(currentUp)- 10;
  box.style.top = newUp +'px';
})

downButton.addEventListener('click', e => {
let currentDown = box.style.top;
console.log('currentDown =' + currentDown);
let newDown = parseInt(currentDown) + 10;
box.style.top = newDown + 'px';
})
