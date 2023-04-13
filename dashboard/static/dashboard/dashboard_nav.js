// select all side bar navigations links and toggle their active state
const links = document.querySelectorAll(".list-group-item");
links.forEach((link) => {
	link.classList.add("active");
	link.addEventListener("click", () => {
		links.forEach((link) => {
			link.classList.remove("active");
		});
		link.classList.add("active");
	});
});
