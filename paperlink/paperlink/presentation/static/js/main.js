deleteBtn = document.querySelectorAll(".delete-btn");
if (deleteBtn.length > 0) {
    deleteForm = document.getElementById("deleteForm");
    deleteBtn.forEach(function(element) {
        element.addEventListener('click', function () {
            actionStr = deleteForm.action
            console.log(actionStr)
            actionStr = actionStr.substring(0, actionStr.length - 1)
            console.log(actionStr)
            deleteForm.action = actionStr + this.value
        });
    });
}

editBtn = document.querySelectorAll(".edit-btn");
if (editBtn.length > 0) {
    editForm = document.getElementById("editForm");
    editBtn.forEach(function(element) {
        element.addEventListener('click', function () {
            actionStr = editForm.action
            console.log(actionStr)
            actionStr = actionStr.substring(0, actionStr.length - 1)
            console.log(actionStr)
            editForm.action = actionStr + this.value
        });
    });
}