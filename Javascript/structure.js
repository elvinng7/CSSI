console.log('something');

let score1 = 97;
let score2 = 92;
let score3 = 90;


let scores = [97, 92, 90, 87, 88, 100, 99];

let max = scores[0];

for (let i = 0; i < scores.length; i++) {
  //console.log(scores[i]);
  if (scores[i] > max) {
    max = scores[i];

  }

}

//console.log('The max scores is ' + max)

//write a loop that calculates the total.
let total = 0

for (let i = 0; i < scores.length; i++ ) {
  total += scores[i];
//total = total + scores[i]
}

//console.log('The total value is ' + total)

let names = ['Savion', 'Jenny', 'Olivia', 'Joshua']
names.forEach(name => {
  //console.log('Welcome, ' + name)
})


//let matthew = ['Mathew', 'Levine', 'Darthmouth', 'Harry Potter']

//console.log(matthew[2])


//let yojairo = ['Yojairo', 'Morales', 'USC', 'Kendrick Lamar']


let matthew = {
  'firstName': 'Matthew',
  'lastName' : 'Levine',
  'University': 'Darthmouth',
  'culture'   : 'Harry Potter',
};
console.log(matthew.University);
console.log(matthew['University']);


let Yojairo = {
  'firstName': 'Yojairo',
  'lastName' : 'Morales',
  'University': 'USC',
  'culture'   : 'Kendrick Lamar',


let people = [matthew, Yojairo];

people.forEach(person => {
console.log(person.firstName + ' really likes ' person.culture);
} )

let style
