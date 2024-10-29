const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deletePostButtons = document.getElementsByClassName("delete-post-btn");
const confirmDelete = document.getElementById("confirmDelete");

const editButtons = document.getElementsByClassName("edit-button");
const updateButton = document.getElementById("editSubmit");
const editModal = new bootstrap.Modal(document.getElementById("editModal"));
const editForm = document.getElementById("editForm");


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

for (let button of deletePostButtons) {
    button.addEventListener('click', (e) => {
        let postId = e.target.getAttribute("post_id");
        confirmDelete.href = `delete_post/${postId}`;
        deleteModal.show();
    })
}

/**
 * Edit post functionality
 * Adds event listener to the edit button on the 'view_full_post.html' page
 * Changes the title of the modal to the title of the post
 * Then shows the editModal
 */

for (let button of editButtons) {
    button.addEventListener('click', (e) => {
        let title = document.getElementById("modalTitle");
        let titleContent = e.target.getAttribute("post_title");
        title.innerText = titleContent;
        editModal.show();
    })
}

