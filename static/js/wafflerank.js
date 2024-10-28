/**
 * Function to display the users wafflerank
 * gets their data on their wafflescore and puts what their rank is accordingly
 * builds the string to displayed as the header's inner text
 */

let wafflerankHeader = document.getElementById('wafflerankHeader');
let userScore = wafflerankHeader.getAttribute('user_score');
let waffleRank = "";

console.log(userScore)

if (userScore == 0) {
    waffleRank = "Yet to waffle!";
} else if (userScore >= 30) {
    waffleRank = "Certified Pro Waffler";
} else if (userScore >= 20) {
    waffleRank = "Proper waffler!";
} else if (userScore >= 10) {
    waffleRank = "Has waffle.";
} else if (userScore < 10) {
    waffleRank = "Entry level waffler...";
} 

wafflerankHeader.innerText = "User Rank: " + waffleRank;