const Form = () => {
  const content = `<input
      class="form-card-title"
      type="text"
      name="titulo"
      placeholder="Título"
    />
    <textarea
      class="autoresize"
      name="detalhes"
      placeholder="Digite o conteúdo..."
    ></textarea>
    <button class="btn" type="submit">Editar</button>`

  const element = document.createElement('form');
  element.method = 'post';
  element.classList.add('form-card');
  element.classList.add('form-card-tight');
  element.innerHTML = content;

  return element
}

const fetchNote = (noteId) => {
  const formWrapper = document.querySelector('.form-wrapper');

  const requestOptions = {
    method: "GET",
    redirect: "follow",
  };

  fetch(`http://0.0.0.0:8080/api/notes/${noteId}`, requestOptions)
    .then((response) => response.json())
    .then((data) => {
      const { title, content } = data;

      formWrapper.appendChild(Form());
      const noteTitleInput = document.querySelector('.form-card-title');
      const noteContentInput = document.querySelector('.autoresize');
      noteTitleInput.value = title;
      noteContentInput.value = content;
    })
    .catch((error) => {
      window.location.replace("/404");
    });
};
