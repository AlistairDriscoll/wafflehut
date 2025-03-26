/* jshint esversion: 6 */
/* global bootstrap */


let wafflerankHeader = document.getElementById('wafflerank-header');

/** Checks to see there is a wafflerank-header
 * If so, calculates what to display as the waffle rank
 * and displays accordingly
 */
if (wafflerankHeader) {
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
    } else {
        waffleRank = "Entry level waffler...";
    }

    wafflerankHeader.innerText = "User Rank: " + waffleRank;
}

document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        document.querySelectorAll('.alert').forEach(alert => {
            let instance = bootstrap.Alert.getOrCreateInstance(alert);
            instance.close();
        });
    }, 4000);
});
