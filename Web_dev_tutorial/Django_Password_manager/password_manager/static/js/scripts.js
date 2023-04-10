const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const check = () => {
  if (document.getElementById("btn-check").checked) {
    document.getElementById("id_password").type = "text";
    document.getElementById("label-check").innerHTML = "Hide password";
  } else {
    document.getElementById("id_password").type = "password";
    document.getElementById("label-check").innerHTML = "Show password";
  }
};

const copy_login = async (id, text) => {
  navigator.clipboard.writeText(text);
  document.getElementById(id).innerHTML = "Copied to clipboard.";
  await sleep(2000)
  document.getElementById(id).innerHTML = "Copy Login";
};
