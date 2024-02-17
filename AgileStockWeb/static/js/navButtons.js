/* ##########################################################################
## Company: AgileStock
## Engineer(s): Robert Howell, Branson Addington
## 
## Create Date:    2/10/2023
## Project Name:    AgileStock
## Target Devices:    Web
## Tool versions:    JavaScript
## Description:   This module holds nav buttons code
## Dependencies:
##   -module(s):
##
##   -packages(s):
##
## Revision: 1.1 - Updated for table column add/remove based on input selection
## Revision: 1.0 - File Created
## Additional Comments: When the edit or delete nav button is toggled, the
##  matching edit or delete buttons are removed from the markup dynamically.
##
########################################################################## */
const navButtons = {
  init: () => {
    //Nav buttons toggle elements
    const editToggle = document.querySelector('.switch[for="editToggle"]');
    const editToggleInpElem = document.querySelector('.switch[for="editToggle"] input');
    const deleteToggle = document.querySelector('.switch[for="deleteToggle"]');
    const deleteToggleInpElem = document.querySelector('.switch[for="deleteToggle"] input');

    //Inventory items' delete button
    const invItemDelButtons = document.querySelectorAll("button.DelButton");

    //Inventory items' edit button
    const invItemEditButtons = document.querySelectorAll("button.EditButton");

    //Edit & Delete switches from navigation
    const switchElems = document.querySelectorAll(".switch");

    //Edit &  Delete table columns + elements
    const editColumn = document.getElementById("editColumn");
    const editColumnRows = document.querySelectorAll(".editColumnCell");
    const deleteColumn = document.getElementById("deleteColumn");
    const deleteColumnRows = document.querySelectorAll(".deleteColumnCell");

    const editToggleInputCheck = () => {
      if (editToggleInpElem.checked == true) {
        //Reveal edit column for the table view
        if (editColumn != null) {
          editColumn.style.display = "table-cell";
          editColumnRows.forEach(row => {
            //Reveal each edit cell
            row.classList.remove("hidden");
          });
        }

        //Reveal all inventory edit buttons
        invItemEditButtons.forEach(button => {
          button.classList.remove("hidden");
        });
      } else {
        //Hide edit column for the table view
        if (editColumn != null) {
          editColumn.style.removeProperty("display");
          editColumnRows.forEach(row => {
            //Hide each edit cell
            row.classList.add("hidden");
          });
        }
        //Hide all inventory edit buttons
        invItemEditButtons.forEach(button => {
          button.classList.add("hidden");
        });
      }
    };

    const deleteToggleInputCheck = () => {
      if (deleteToggleInpElem.checked == true) {
        //Reveal delete column for the table view
        if (deleteColumn != null) {
          deleteColumn.style.display = "table-cell";
          deleteColumnRows.forEach(row => {
            //Reveal each edit cell
            row.classList.remove("hidden");
          });
        }
        //Reveal all inventory delete buttons
        invItemDelButtons.forEach(button => {
          button.classList.remove("hidden");
        });
      } else {
        //Hide edit column for the table view
        if (deleteColumn != null) {
          deleteColumn.style.removeProperty("display");
          deleteColumnRows.forEach(row => {
            //Hide each edit cell
            row.classList.add("hidden");
          });
        }
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
