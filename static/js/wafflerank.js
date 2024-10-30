/**
 * Function to display the users wafflerank
 * gets their data on their wafflescore and puts what their rank is accordingly
 * builds the string to displayed as the header's inner text
 */

let wafflerankHeader = document.getElementById('wafflerankHeader');
let userScore = wafflerankHeader.getAttribute('user_score');
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


/**
 * Functionality for updateUserDetails modal and form within
 * adds event listener to button to show the modal
 */

let updateUserButton = document.getElementById("updateUser");
let updateUserModal = new bootstrap.Modal(document.getElementById("updateUserModal"));
let userForm = document.getElementById("userForm")

updateUserButton.addEventListener("click", (e) => {
    let fullName = e.target.getAttribute("full_name");
    let userBio = e.target.getAttribute("user_bio");
    let fullNameInput = document.getElementById("id_full_name");
    let bioInput = document.getElementById("id_bio");

    fullNameInput.innerText = fullName;
    bioInput.innerText = userBio;

    updateUserModal.show();
})


/**
 * Functionality to show the delete account modal
 */

let showDeleteUser = document.getElementById("deleteUser");


showDeleteUser.addEventListener("click", (e) => {
    let deleteAccountModal = new bootstrap.Modal(document.getElementById("deleteAccountModal"));
    deleteAccountModal.show()
})


