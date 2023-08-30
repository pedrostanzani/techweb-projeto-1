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

// let currentColor = 0;
// const handleColorButtonClick = (buttonId) => {
//   // console.log(buttonId, currentColor);
//   const colorPickerButtons = document.querySelectorAll('.color-picker-btn');
//   colorPickerButtons[currentColor].classList.remove('color-picker-btn--selected');
//   colorPickerButtons[buttonId].classList.add('color-picker-btn--selected');
//   currentColor = buttonId;
// }


const main = () => {
}

main();