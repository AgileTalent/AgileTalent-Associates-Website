(() => {
  "use strict";
  const containers = document.querySelectorAll("[data-client-logo-marquee]");
  if (!containers.length) return;

  fetch("/logos/logos.json")
    .then(response => {
      if (!response.ok) throw new Error("Logo manifest could not be loaded");
      return response.json();
    })
    .then(items => {
      if (!Array.isArray(items) || !items.length) throw new Error("Logo manifest is empty");
      containers.forEach(container => {
        const track = container.querySelector(".marq-track");
        if (!track) return;
        track.replaceChildren();
        const makeList = (hidden) => {
          const list = document.createElement("ul");
          if (hidden) list.setAttribute("aria-hidden", "true");
          items.forEach(item => {
            if (!item || !item.name || !item.file) return;
            const li = document.createElement("li");
            const img = document.createElement("img");
            img.src = "/logos/" + item.file;
            img.alt = hidden ? "" : item.name;
            img.loading = "lazy";
            img.onerror = function () {
              if (!hidden) {
                const fallback = document.createElement("span");
                fallback.textContent = item.name;
                li.replaceChildren(fallback);
              } else {
                li.remove();
              }
            };
            li.appendChild(img);
            list.appendChild(li);
          });
          return list;
        };
        track.append(makeList(false), makeList(true));
        container.setAttribute("aria-label", "Organisations we have worked with: " + items.map(item => item.name).join(", "));
      });
    })
    .catch(error => {
      containers.forEach(container => {
        const track = container.querySelector(".marq-track");
        if (track) {
          const fallback = document.createElement("p");
          fallback.textContent = "Organisation logos are temporarily unavailable.";
          track.replaceChildren(fallback);
        }
      });
      console.error("Client logo marquee:", error);
    });
})();