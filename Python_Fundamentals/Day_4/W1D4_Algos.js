/* 
Given in an alumni interview in 2021.
String Encode
You are given a string that may contain sequences of consecutive characters.
Create a function to shorten a string by including the character,
then the number of times it appears. 


If final result is not shorter (such as "bb" => "b2" ),
return the original string.
*/

const str1 = "aaaabbcddd";
const expected1 = "a4b2c1d3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs. Only encode strings
 * when the result yields a shorter length.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
 */
function encodeStr(str) {
    var expectedReturn = "";
    var count = 1;
    for (var i = 0; i < str.length; i++){
        count = 1;
        while (str[i] == str[i + 1]){
            count++;
            i++;
        }
        expectedReturn += str[i] + count;
    }
    if(expectedReturn.length < str.length){
        return expectedReturn;
    }
    else{
        return str;
    }
}

console.log(encodeStr(str1)); // "a4b2c1d3"
console.log(encodeStr(str2)); // ""
console.log(encodeStr(str3)); // "a"
console.log(encodeStr(str4)); // "bbcc"

/*****************************************************************************/


const strA = "a3b2c1d3";
const expectedA = "aaabbcddd";

const strB = "a3b2c12d10";
const expectedB = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
//helpful built-ins : isNaN() .repeat() parseInt() 
function decodeStr(str) {
    var result = "";
    for(var i = 0; i < str.length; i++){
        
    }
}

console.log(decodeStr(strA)) // Expected: aaabbcddd
console.log(decodeStr(strB)) // Expected: aaabbccccccccccccdddddddddd
