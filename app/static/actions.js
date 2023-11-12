// Add event listner after DOM content loaded
window.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("loginForm");

  // Let's listen to submit event
  loginForm.addEventListener("submit", (e) => {
    // remove the default action
    e.preventDefault();

    // Clear the rank text
    const rankDiv = document.getElementById("rank");
    rankDiv.innerHTML = "";

    const parents = document.getElementById("parents").value;
    const childsNursery = document.getElementById("has_nurs").value;
    const familyForm = document.getElementById("form").value;
    const children = document.getElementById("children").value;
    const housing = document.getElementById("housing").value;
    const finance = document.getElementById("finance").value;
    const familySocial = document.getElementById("social").value;
    const familyHealth = document.getElementById("health").value;

    const requestBody = {
      parents,
      childsNursery,
      familyForm,
      children,
      housing,
      finance,
      familySocial,
      familyHealth,
    };

    console.log(requestBody);
    // call the async post Request
    (async () => {
      const { rank } = await postRequest("/rank", requestBody);
      rankDiv.innerHTML = `Rank: ${rank}`;
    })();
  });
});

const postRequest = async (url, body) => {
  const response = await fetch(url, {
    method: "POST",
    body: JSON.stringify(body),
    headers: {
      "Content-Type": "application/json",
    },
  });

  const json = await response.json();
  return json;
};
