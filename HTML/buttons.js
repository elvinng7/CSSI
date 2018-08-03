console.log("Hello");



let likeButton = document.querySelector('#like')
console.log(likeButton);

likeButton.addEventListener ('click', e => {
  likeButton.innerText = 'Liked';
  likedButton.disabled = true;
});


let growButton = document.querySelector('#grow')
growButton.addEventListener('click', e => { console.log('click');

let currentSize = growButton.style.fontSize;
let newSize = parseInt(currentSize) + 10;
console.log(newSize);
growButton.style.fontSize = newSize + 'px';

})

let keys = ['name', 'school', 'hometown']

let students = {
Name: ‘Julia’
School: ‘USC’
Hometown: ‘san bruno’
         }


for (let i = 0; i< keys.length; i++)
let key = keys[i]

console.log
