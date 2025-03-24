/* jshint esversion: 6 */

let wafflerankHeader = document.getElementById('wafflerank-header');
let userScore = wafflerankHeader.getAttribute('data-user_score');
let waffleRank = "";

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

document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        document.querySelectorAll('.alert').forEach(alert => {
            let instance = bootstrap.Alert.getOrCreateInstance(alert);
            instance.close();
        });
    }, 4000);
});
