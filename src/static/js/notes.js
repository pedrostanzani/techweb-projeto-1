const deleteNote = (noteId) => {
  const noteContainer = document.querySelector('.card-container');
  const notes = document.getElementsByClassName("card");

  const requestOptions = {
    method: "DELETE",
    redirect: "follow",
  };

  fetch(`http://0.0.0.0:8080/api/notes/${noteId}`, requestOptions)
    .then((response) => {
      const deletedNoteArr = Array.from(notes).filter(note => note.dataset.noteId === noteId.toString());
      if (deletedNoteArr.length === 0) {
        return;
      }

      const deletedNote = deletedNoteArr[0];
      noteContainer.removeChild(deletedNote)
    })
    .catch((error) => console.log("error", error));
};
