const navButtons = {
  init: () => {
    //Nav buttons toggle elements
    const editToggle = document.querySelector('.switch[for="editToggle"]');
    const editToggleInpElem = document.querySelector('.switch[for="editToggle"] input');
    const deleteToggle = document.querySelector('.switch[for="deleteToggle"]');
    const deleteToggleInpElem = document.querySelector('.switch[for="deleteToggle"] input');

    //Inventory items' delete button
    const invItemDelButtons = document.querySelectorAll(".bookButtons .DelButton");

    //Inventory items' edit button
    const invItemEditButtons = document.querySelectorAll(".bookButtons .EditButton");

    //Edit & Delete switches from navigation
    const switchElems = document.querySelectorAll(".switch");

    const editToggleInputCheck = () => {
      if (editToggleInpElem.checked == true) {
        invItemEditButtons.forEach(button => {
          button.classList.remove("hidden");
        });
      } else {
        invItemEditButtons.forEach(button => {
          button.classList.add("hidden");
        });
      }
    };

    const deleteToggleInputCheck = () => {
      if (deleteToggleInpElem.checked == true) {
        //Reveal all inventory delete buttons
        invItemDelButtons.forEach(button => {
          button.classList.remove("hidden");
        });
      } else {
        //Hide all inventory delete buttons
        invItemDelButtons.forEach(button => {
          button.classList.add("hidden");
        });
      }
    };

    //Reveal/show the edit option
    editToggle.addEventListener("click", () => {
      editToggleInputCheck();
    });

    //Reveal/show the delete option
    deleteToggle.addEventListener("click", () => {
      deleteToggleInputCheck();
    });

    //Add keyboard event listener, toggle checkbox on enter
    switchElems.forEach(button => {
      button.addEventListener("keydown", event => {
        console.log(`clicked: ${event.key}, type: ${typeof event.key}`);
        //Event listener for enter key
        if (event.key == "Enter") {
          console.log(`target: ${event.target}`);
          if (event.target.getAttribute("for") == "editToggle") {
            //toggle edit button
            editToggleInpElem.toggleAttribute("checked");
            editToggleInputCheck();
          }
          if (event.target.getAttribute("for") == "deleteToggle") {
            //toggle edit button
            deleteToggleInpElem.toggleAttribute("checked");
            deleteToggleInputCheck();
          }
        }
      });
    });
  },
};

export default navButtons;
