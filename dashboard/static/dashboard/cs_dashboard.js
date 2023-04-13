getSummary = async () => {
	let options = {
		method: "GET",
		headers: {
			"X-Requested-With": "XMLHttpRequest",
		},
	};
	let response = await fetch("/dashboard/clinical_service_types", options);
	let jsonData = await response.json();

	const service_label = jsonData.service_types;
	const service_data = jsonData.counts;

	console.log(jsonData);
	const service_type_cntx = document.querySelector("#cntx_clinical_services");
	drawChart(
		service_type_cntx,
		service_label,
		service_data,
		"doughnut",
		"# by type"
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
		options: {
			plugins:{
				legend:{
					display:false,
				},
			},	
		},
	});
};
