const inventoryButtons = {
  init: () => {
    //Inventory item buttons function for edit & delete
    const dialog = document.querySelectorAll("dialog.deleteConfirm");
    const showButton = document.getElementsByClassName("DelButton");
    const closeButton = document.querySelectorAll("dialog .cancelAutofocus");

    // "Show the dialog" button opens the dialog modally
    for (let i = 0; i < showButton.length; i++) {
      showButton[i].addEventListener("click", () => {
        closeButton[i].toggleAttribute("autofocus");
        dialog[i].showModal();
      });

      // "Close" button closes the dialog
      closeButton[i].addEventListener("click", () => {
        dialog[i].close();
        closeButton[i].toggleAttribute("autofocus");
      });
    }
  },
};

export default inventoryButtons;
