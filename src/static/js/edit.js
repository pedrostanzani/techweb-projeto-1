const Form = (checkedColor) => {
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
    <div class="color-picker-container">
      <fieldset>
          <input class="color-picker-radio card-color-4" type="radio" name="color" value="yellow" ${checkedColor === "yellow" ? "checked" : null} />
          <input class="color-picker-radio card-color-1" type="radio" name="color" value="brown"  ${checkedColor === "brown" ? "checked" : null} />
          <input class="color-picker-radio card-color-2" type="radio" name="color" value="blue"   ${checkedColor === "blue" ? "checked" : null} />
          <input class="color-picker-radio card-color-3" type="radio" name="color" value="pink"   ${checkedColor === "pink" ? "checked" : null} />
          <input class="color-picker-radio card-color-5" type="radio" name="color" value="green"  ${checkedColor === "green" ? "checked" : null} />
      </fieldset>
    </div>
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
      console.log(data);
      const { title, content, color } = data;

      formWrapper.appendChild(Form(color));
      const noteTitleInput = document.querySelector('.form-card-title');
      const noteContentInput = document.querySelector('.autoresize');
      noteTitleInput.value = title;
      noteContentInput.value = content;
    })
    .catch((error) => {
      window.location.replace("/404");
    });
};
