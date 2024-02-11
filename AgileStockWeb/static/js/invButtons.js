import inventoryButtons from "./inventoryButtons.js";
import navButtons from "./navButtons.js";

const app = {
  main: () => {
    //add inv init
    inventoryButtons.init();

    if (window.location.pathname == "/home" || window.location.pathname == "/") {
      //Show Edit/Delete buttons
      const switches = document.querySelectorAll(".switch");
      switches.forEach(button => {
        button.style.display = "flex";
      });

      //add nav init
      navButtons.init();
    }
  },
};

app.main();
