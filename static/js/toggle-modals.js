const registratiSection = document.getElementById("registrati");

registratiSection.style.setProperty("display", "none");

const toggleRegistrati = () => {
  const currentDisplay = registratiSection.style.display;
  if (currentDisplay === "none") {
    registratiSection.style.setProperty("display", "block");
  } else {
    registratiSection.style.setProperty("display", "none");
  }
};