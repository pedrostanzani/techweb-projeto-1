const fetchNote = (noteId) => {
  const noteTitleInput = document.querySelector('.form-card-title');
  const noteContentInput = document.querySelector('.autoresize');

  const requestOptions = {
    method: "GET",
    redirect: "follow",
  };

  fetch(`http://0.0.0.0:8080/api/notes/${noteId}`, requestOptions)
    .then((response) => response.json())
    .then((data) => {
      const { title, content } = data;
      noteTitleInput.value = title;
      noteContentInput.value = content;
    })
    .catch((error) => console.log("error", error));
};
