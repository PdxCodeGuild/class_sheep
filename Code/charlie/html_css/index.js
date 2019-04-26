<!DOCTYPE html>

let grade = parseInt(prompt("enter your grade."))

let lettergrade = null
if (grade < 60) {
  lettergrade = 'F';
} else if (grade < 70) {
  lettergrade = 'D';
} else if (grade < 80) {
  lettergrade = 'C';
} else if (grade < 90) {
  lettergrade = 'B';
} else if (grade <= 100) {
  lettergrade = 'A';
}

console.log(lettergrade)
