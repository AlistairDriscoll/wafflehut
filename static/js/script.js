const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deletePostButtons = document.getElementsByClassName("delete-post-btn");
const confirmDelete = document.getElementById("confirmDelete");

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
        let postSlug = e.target.getAttribute("post_slug");
        console.log(postId)
        confirmDelete.href = `delete_post/${postId}`;
        deleteModal.show();
    })
}