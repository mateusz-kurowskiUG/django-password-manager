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

const copy = async (id, text, type) => {
  navigator.clipboard.writeText(text);
  document.getElementById(id).innerHTML = "Copied to clipboard.";
  await sleep(2000);
  if (type === "login") document.getElementById(id).innerHTML = "Copy Login";
  if (type === "generator") document.getElementById(id).innerHTML = "Generate";
  if (type === "password")
    document.getElementById(id).innerHTML = "Copy Password";
};

const reveal = async (id, text) => {
  document.getElementById(id).innerHTML = text;
  await sleep(5000);
  document.getElementById(id).innerHTML = "Reveal Password";
};

const showVal = (val, elemId) => {
  document.getElementById(elemId).innerHTML = val;
};

const generatePassword = (
  rangeVal,
  specialCharacters,
  capitals,
  numbers,
  passwdInput
) => {
  const len = document.getElementById(rangeVal).value;
  let chars = "abcdefghijklmnopqrstuvwxyz";
  if (document.getElementById(capitals).checked)
    chars = chars.concat(chars.toUpperCase());
  if (document.getElementById(specialCharacters).checked)
    chars = chars.concat("@#$%^&*.");
  if (document.getElementById(numbers).checked)
    chars = chars.concat("0123456789");

  const res = Array.from(crypto.getRandomValues(new Uint32Array(len)))
    .map((x) => chars[x % chars.length])
    .join("");

  const getInput = document.getElementById(passwdInput);
  getInput.innerHTML = res;
};
