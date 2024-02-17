/* ##########################################################################
## Company: AgileStock
## Engineer(s): Robert Howell, Branson Addington
## 
## Create Date:    2/10/2023
## Project Name:    AgileStock
## Target Devices:    Web
## Tool versions:    JavaScript
## Description:   This module holds frontend JS needed for inventory buttons' function
## Dependencies:
##   -module(s):
##
##   -packages(s):
##
## Revision: 1.1 - Edit/delete buttons code update to handle null elements
## Revision: 1.0 - File Created
## Additional Comments: 
##
########################################################################## */
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
