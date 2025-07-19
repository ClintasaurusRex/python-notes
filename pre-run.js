let billAmount = parseFloat(1000);
let tipPercentage = parseFloat(15);
let numPeople = 7;

let tipAmount = (tipPercentage / 100) * billAmount;
let totalAmount = billAmount + tipAmount;
let amountPerPerson = totalAmount / numPeople;

console.log(totalAmount);
console.log(amountPerPerson);

// let length = 5;
// let width = 3.2;

// let lengthFloat = parseFloat(length);
// let widthFloat = parseFloat(width);

// let area = lengthFloat * widthFloat;
// let perimeter = (lengthFloat + widthFloat) * 2;

// console.log(`The area is: ${area} and the perimeter is: ${perimeter}`);

/* You are given a user input, a number grade (0-100) stored in a variable.
Use a switch statement to determine the corresponding letter grade based on these ranges:
90-100: "A"
80-89: "B"
70-79: "C"
60-69: "D"
0-59: "F"
Print the letter grade.
Handle invalid input (numbers outside the 0-100 range) by printing "Invalid grade".

Tip: You can use parseInt() to convert the input to an integer. To check a range of numbers in a case statement, you can use case with a condition like this:

// Get the number grade from the user*/
// let numGrade = -2;

// // Convert input to a number
// numGrade = parseInt(numGrade);

// // Determine the letter grade using a switch statement
// let letterGrade;

// switch (true) {
//   // Write your code here
//   case numGrade >= 90 && numGrade <= 100:
//     letterGrade = "A";
//     break;
//   case numGrade >= 80 && numGrade <= 89:
//     letterGrade = "B";
//     break;
//   case numGrade >= 70 && numGrade <= 79:
//     letterGrade = "C";
//     break;
//   case numGrade >= 60 && numGrade <= 69:
//     letterGrade = "D";
//     break;
//   case numGrade < 60 && numGrade >= 0:
//     letterGrade = "F";
//     break;
//   default:
//     letterGrade = "Invalid grade";
// }

// // Print the letter grade
// console.log(`Letter grade: ${letterGrade}`);

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
