let has_license = true;
let has_insurance = false;
let has_experience = true;

let can_drive_car = (has_license && has_insurance) || (has_license && has_experience);
let can_drive_motorcycle = has_license && has_experience && has_insurance;
let cannot_drive_any = !(has_experience && has_license) && has_insurance;

// Don't delete the lines below
console.log("Can drive car:", can_drive_car);
console.log("Can drive motorcycle:", can_drive_motorcycle);
console.log("Cannot drive any:", cannot_drive_any);

// balance += 100;
// let percent = (balance *= 0.1);
// balance = percent + (100 - 50);

// // Don't change the line below
// console.log(`balance = ${Math.floor(balance)}`);

// for (let i = 1; i <= 100; i++) {
//   if (i % 3 === 0 && i % 5 === 0) {
//     console.log("Fizzbuzz");
//   } else if (i % 3 === 0) {
//     console.log("fizz");
//   } else if (i % 5 === 0) {
//     console.log("Buzz");
//   } else {
//     console.log(i);
//   }
// }
// let count = 0;
// count += 4 * 2 - 1;
// console.log(`Count = ${count}`);

// console.log(15 % 4);

// let x = 15;
// let y = 4;
// let z = x % y;
// console.log(z);

// let userScore;
// userScore = 200;
// console.log(userScore);

// console.log(17 % 5);

// let a = 9;
// let b = 2.6;
// let c = 11;
// let d = a % 2;
// let e = a % 3;
// let f = c % 10;

// console.log(`a = ${a}`);
// console.log(`b = ${b}`);
// console.log(`c = ${c}`);
// console.log(`d = ${d}`);
// console.log(`e = ${e}`);
// console.log(`f = ${f}`);
