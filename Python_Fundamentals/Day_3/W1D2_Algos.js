/* 
Given an arr and a separator string, output a string of every item in the array separated by the separator.

No trailing separator at the end
Default the separator to a comma with a space after it if no separator is provided
*/

const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @returns {string} The given array items as a string separated by the given separator.
 */
function join(arr, separator) {
    //your code here
}

console.log(join(arr1,separator1)) // "1, 2, 3"
console.log(join(arr2,separator2)) // "1-2-3"
console.log(join(arr3,separator3)) // "1 - 2 - 3"
console.log(join(arr4,separator4)) // "1"
console.log(join(arr5,separator5)) // ""
/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

const str1 = "object oriented programming";
const expectedA = "OOP";

// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expectedB = "APIE";

const str3 = "software development life cycle";
const expectedC = "SDLC";

// Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expectedD = "GIT";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @returns {string} The acronym.
 */
function acronymize(str) {
  var acro = "";
  var flag = false;
  for (var i = 0; i < str.length; i++) {
    if (str[i] != " " && flag == false) {
      acro += str[i]
      flag = true 
    }
  }
  var cap_acro = acro.toUpperCase()
  return cap_acro
}

acronymize("Sadie Boop");
// console.log(acronymize(str1)); // "OOP"
// console.log(acronymize(str2)); // "APIE"
// console.log(acronymize(str3)); // "SDLC"
// console.log(acronymize(str4)); // "GIT"




// function split(str) {

//   var lastIdx = 0;
//   var word = '';
//   var array = [];
//   for(var i = 0; i < str.length; i++) {
//     var char = str.charAt(i);
//     if (i == str.length - 1) {
//       word = str.substring(lastIdx, i);
//       array.push(word);
//     }
//     else if (char == " ") {
//       word = str.substring(lastIdx, i);
//       lastIdx = i + 1;
//       array.push(word);
//     }
//   }
//   return array;
// }