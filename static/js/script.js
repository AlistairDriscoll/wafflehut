/* jshint esversion: 6 */

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deletePostButton = document.getElementById("delete-post-btn");
const confirmDelete = document.getElementById("confirmDelete");
const editButton = document.getElementById("edit-post-btn");
const editModal = new bootstrap.Modal(document.getElementById("editModal"));


/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated posts's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
* - Taken from Code Institute's 'I think therfore I blog' module
*/


deletePostButton.addEventListener('click', (e) => {
    let postId = e.target.getAttribute("post_id");
    confirmDelete.href = `delete_post/${postId}`;
    deleteModal.show();
});


/**
 * Edit post functionality
 * Adds event listener to the edit button on the 'view_full_post.html' page
 * Changes the title of the modal to the title of the post
 * Then shows the editModal
 */


editButton.addEventListener('click', (e) => {
    let title = document.getElementById("modalTitle");
    let titleContent = e.target.getAttribute("post_title");
    title.innerText = titleContent;
    editModal.show();
});


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

updateUserButton.addEventListener("click", (e) => {
    let fullName = e.target.getAttribute("full_name");
    let userBio = e.target.getAttribute("user_bio");
    let fullNameInput = document.getElementById("id_full_name");
    let bioInput = document.getElementById("id_bio");

    fullNameInput.innerText = fullName;
    bioInput.innerText = userBio;

    updateUserModal.show();
});


/**
 * Functionality to show the delete account modal
 */

let showDeleteUser = document.getElementById("deleteUser");


showDeleteUser.addEventListener("click", (e) => {
    let deleteAccountModal = new bootstrap.Modal(document.getElementById("deleteAccountModal"));
    deleteAccountModal.show();
});
