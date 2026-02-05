# Code Institute navbar close

From the [Boardwalk Games walkthrough project](https://stillprocrastinating.github.io/UDP5WA4CF-TU_boardwalk_games/) by Code Institute.

```html
<nav>
    ...
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        ...
    </button>
    ...
</nav>
```

```js
document
    .querySelectorAll(".narbar-collapse .nav-link")
    .forEach((link) => {
        link.addEventListener("click", function (e) {
            let section = document.querySelector(e.target.getAttribute("href"));
            if (section) {
                e.preventDefault();     // Prevent default anchor click behaviour
                let navbarHeight = document.querySelector(".navbar-toggler").offsetHeight;
                window.scroll({
                    top: section.offsetTop - navbarHeight,     // Adjust for navbar height
                    behavior: "smooth",
                });
                document
                    .querySelector(".navbar-collapse")
                    .classList.remove("show");     // Collapse navbar
            }
        })
})
```
