/* ##########################################################################
## Company: AgileStock
## Engineer(s): Robert Howell, Branson Addington
## 
## Create Date:    2/10/2023
## Project Name:    AgileStock
## Target Devices:    Web
## Tool versions:    JavaScript
## Description:   This javascript file calls the entrypoint app.main()
## Dependencies:
##   -module(s):
##      inventoryButtons
##      navButtons
##
##   -packages(s):
##
## Revision: 1.1 - Added hide/reveal edit/delete button event listeners
## Revision: 1.0 - File Created
## Additional Comments: The script loads via script tag in layout.html template.
##  The code is developed in module format, calling subsequent code from imported modules.
##
########################################################################## */
import inventoryButtons from "./inventoryButtons.js";
import navButtons from "./navButtons.js";

const app = {
  main: () => {
    //add inv init
    inventoryButtons.init();

    if (window.location.pathname == "/home" || window.location.pathname == "/") {
      //Reveal the Edit/Delete buttons in the navigation panel; they're hidden by default.
      const switches = document.querySelectorAll(".switch");
      switches.forEach(button => {
        button.style.display = "flex";
      });

      //Initialize the button toggle action in "navButtons" script
      navButtons.init();
    }
  },
};

app.main();
