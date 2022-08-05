getSummary = async () => {
	let options = {
		method: "GET",
		headers: {
			"X-Requested-With": "XMLHttpRequest",
		},
	};
	let response = await fetch("/dashboard/vaccination_types", options);
	let jsonData = await response.json();

	const vaccination_label = jsonData.vaccination_types;
	const vaccination_count = jsonData.vaccination_count;

	console.log(jsonData);
	const vaccination_cntx = document.querySelector("#cntx_vaccination");

	drawChart(
		vaccination_cntx,
		vaccination_label,
		vaccination_count,
		"bar",
		"Vaccinations"
	);
};
getSummary();
drawChart = (canvas, labels, data, type, chart_label) => {
	const myChart = new Chart(canvas, {
		type: type,
		data: {
			labels: labels,
			datasets: [
				{
					label: chart_label,
					data: data,
					backgroundColor: [
						"#fd7f6f",
						"#7eb0d5",
						"#b2e061",
						"#bd7ebe",
						"#ffb55a",
						"#ffee65",
						"#beb9db",
						"#fdcce5",
						"#8bd3c7",
					],
					borderColor: "rgba(255, 99, 132, 1)",
					borderWidth: 1,
				},
			],
		},
		options: {},
	});
};
