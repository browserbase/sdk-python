const imageUrl = chrome.runtime.getURL("images/logo.png");
window
  .fetch(imageUrl)
  .then((response) => {
    if (response.ok) {
      console.log("browserbase test extension image loaded");
    }
  })
  .catch((error) => {
    console.log(error);
  });
