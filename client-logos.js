(() => {
  "use strict";
  const scriptElement = document.currentScript;
  const scriptUrl = new URL(scriptElement ? scriptElement.src : "client-logos.js", document.baseURI);
  const manifestUrl = new URL("logos/logos.json", scriptUrl);
  const containers = document.querySelectorAll("[data-client-logo-marquee]");
  if (!containers.length) return;

  fetch(manifestUrl.href, { cache: "no-cache" })
    .then(response => {
      if (!response.ok) throw new Error("Logo manifest request failed: " + response.status);
      return response.json();
    })
    .then(items => {
      if (!Array.isArray(items)) throw new Error("Logo manifest is not a list");
      containers.forEach(container => {
        const track = container.querySelector(".marq-track");
        if (!track) return;
        const available = items.filter(item => item && item.name && item.file);
        track.replaceChildren();
        const makeList = hidden => {
          const list = document.createElement("ul");
          if (hidden) list.setAttribute("aria-hidden", "true");
          available.forEach(item => {
            const li = document.createElement("li");
            const img = document.createElement("img");
            img.src = new URL(item.file, manifestUrl).href;
            img.alt = hidden ? "" : item.name;
            img.loading = "eager";
            img.decoding = "async";
            img.addEventListener("error", () => {
              if (hidden) li.remove();
              else {
                const fallback = document.createElement("span");
                fallback.textContent = item.name;
                li.replaceChildren(fallback);
              }
            }, { once: true });
            li.appendChild(img);
            list.appendChild(li);
          });
          return list;
        };
        track.append(makeList(false), makeList(true));
        container.setAttribute("aria-label", "Organisations we have worked with: " + available.map(item => item.name).join(", "));
      });
    })
    .catch(error => {
      containers.forEach(container => {
        const track = container.querySelector(".marq-track");
        if (!track) return;
        const fallback = document.createElement("p");
        fallback.textContent = "Organisation logos are temporarily unavailable.";
        track.replaceChildren(fallback);
      });
      console.error("Client logo marquee:", error);
    });
})();
