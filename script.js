async function processVideo() {
  const videoUrl = document.getElementById("videoUrl").value;
  const status = document.getElementById("status");

  if (!videoUrl) {
    status.innerText = "Please paste a video URL first.";
    return;
  }

  status.innerText = "Processing… This may take a few minutes.";

  try {
    const response = await fetch("https://YOUR-BACKEND-URL.onrender.com/process", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ video_url: videoUrl })
    });

    const data = await response.json();

    status.innerHTML = "";

    if (!data.clips || data.clips.length === 0) {
      status.innerText = "No clips generated.";
      return;
    }

    data.clips.forEach((link, index) => {
      const a = document.createElement("a");
      a.href = link;
      a.innerText = `Download Clip ${index + 1}`;
      a.target = "_blank";
      a.style.display = "block";
      a.style.marginTop = "10px";
      status.appendChild(a);
    });

  } catch (err) {
    status.innerText = "Something went wrong. Please try again later.";
  }
}
