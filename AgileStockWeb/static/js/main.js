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
