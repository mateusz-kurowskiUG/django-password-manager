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

const copy = async (id, text,type) => {
  navigator.clipboard.writeText(text);
  document.getElementById(id).innerHTML = "Copied to clipboard.";
  await sleep(2000)
  if (type==='login') document.getElementById(id).innerHTML = "Copy Login";
  if (type==='password') document.getElementById(id).innerHTML = "Copy Password";
};


const reveal = async (id,text) => {
  document.getElementById(id).innerHTML = text
  await sleep(5000)
  document.getElementById(id).innerHTML = "Reveal Password"

}




