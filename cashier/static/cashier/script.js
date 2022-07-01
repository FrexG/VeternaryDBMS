window.onload = () => {
	const serviceBtns = document.querySelectorAll(".service-btn");
	const prescriptionBtns = document.querySelectorAll(".prescription-btn");
	const parasiteBtns = document.querySelectorAll(".parasite-btn");
	console.log(serviceBtns);

	serviceBtns.forEach((btn) => {
		btn.onclick = () => {
			deleteService(btn.id.split("_")[1]);
		};
	});

	prescriptionBtns.forEach((btn) => {
		btn.onclick = () => {
			deletePrescription(btn.id.split("_")[1]);
		};
	});

	parasiteBtns.forEach((btn) => {
		btn.onclick = () => {
			deleteParasitePrescription(btn.id.split("_")[1]);
		};
	});

	deleteService = (id) => {
		fetch(`delete_service/${id}/`, {
			method: "POST",
			headers: {
				"X-Requested-With": "XMLHttpRequest",
				"X-CSRFToken": csrftoken,
			},
		})
			.then((response) => {
				window.location.reload();
			})
			.catch((error) => {
				console.log(error);
			});
	};

	deletePrescription = (id) => {
		fetch(`delete_prescription/${id}/`, {
			method: "POST",
			headers: {
				"X-Requested-With": "XMLHttpRequest",
				"X-CSRFToken": csrftoken,
			},
		})
			.then((response) => {
				window.location.reload();
			})
			.catch((error) => {
				console.log(error);
			});
	};

	deleteParasitePrescription = (id) => {
		fetch(`delete_parasite_prescription/${id}/`, {
			method: "POST",
			headers: {
				"X-Requested-With": "XMLHttpRequest",
				"X-CSRFToken": csrftoken,
			},
		})
			.then((response) => {
				window.location.reload();
			})
			.catch((error) => {
				console.log(error);
			});
	};

	function getCookie(name) {
		let cookieValue = null;
		if (document.cookie && document.cookie !== "") {
			const cookies = document.cookie.split(";");
			for (let i = 0; i < cookies.length; i++) {
				const cookie = cookies[i].trim();
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) === name + "=") {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}
	const csrftoken = getCookie("csrftoken");
};
