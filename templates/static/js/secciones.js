// Código JavaScript
document.addEventListener("DOMContentLoaded", function () {
  // Navbar
  var navbar = document.createElement("nav");
  navbar.className = "navbar navbar-expand-lg navbar-light bg-success";

  var container = document.createElement("div");
  container.className = "container bg-success";

  var brand = document.createElement("a");
  brand.className = "navbar-brand";
  brand.href = "#";

  var logo = document.createElement("img");
  logo.src = "https://www.servientrega.com.ec/images/logo.png";
  logo.alt = "";
  logo.width = "100px";

  brand.appendChild(logo);

  var collapse = document.createElement("div");
  collapse.className = "collapse navbar-collapse justify-content-end";
  collapse.id = "navbarSupportedContent";

  var ul = document.createElement("ul");
  ul.className = "navbar-nav";

  var items = [
    { href: "#", text: "Home" },
    { href: "/clientes", text: "Clientes" },
    { href: "/repartidores", text: "Repartidores" },
    { href: "/pagos", text: "Pagos" },
  ];

  items.forEach(function (item) {
    var li = document.createElement("li");
    li.className = "nav-item";

    var a = document.createElement("a");
    a.className = "nav-link navbar-link text-white";
    a.href = item.href;

    var b = document.createElement("b");
    b.textContent = item.text;

    a.appendChild(b);
    li.appendChild(a);
    ul.appendChild(li);
  });

  collapse.appendChild(ul);
  container.appendChild(brand);
  container.appendChild(collapse);
  navbar.appendChild(container);

  var body = document.getElementsByTagName("body")[0];
  body.insertBefore(navbar, body.firstChild);

  // Footer
  var footer = document.createElement("footer");
  footer.className = "bg-success py-4";

  var footerContainer = document.createElement("div");
  footerContainer.className = "container text-center";

  var footerHeading = document.createElement("h5");
  footerHeading.className = "text-white";
  footerHeading.textContent = "Síguenos en redes sociales:";

  var socialIcons = document.createElement("div");
  socialIcons.className = "mt-3";

  var socialLinks = [
    {
      href: "https://www.facebook.com/profile.php?id=100006290192633",
      iconClass: "fab fa-facebook-f",
    },
    { href: "https://twitter.com/?lang=es", iconClass: "fab fa-twitter" },
    {
      href: "https://www.instagram.com/sebas_lz1/",
      iconClass: "fab fa-instagram",
    },
  ];

  socialLinks.forEach(function (link) {
    var anchor = document.createElement("a");
    anchor.href = link.href;
    anchor.className = "social-icon mx-2";

    var icon = document.createElement("i");
    icon.className = link.iconClass;

    anchor.appendChild(icon);
    socialIcons.appendChild(anchor);
  });

  footerContainer.appendChild(footerHeading);
  footerContainer.appendChild(socialIcons);
  footer.appendChild(footerContainer);

  body.appendChild(footer);
});
