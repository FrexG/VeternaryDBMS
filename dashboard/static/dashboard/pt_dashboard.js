getSummary = async () => {
	let options = {
		method: "GET",
		headers: {
			"X-Requested-With": "XMLHttpRequest",
		},
	};
	let response = await fetch("/dashboard/parasite_treatment_types", options);
	let jsonData = await response.json();

	const treatment_label = jsonData.treatment_types;
	const treatment_count = jsonData.treatment_count;
	const disease_names = jsonData.disease_names;
	const disease_count = jsonData.disease_count;

	console.log(jsonData);
	const parasite_treatment_cntx = document.querySelector(
		"#cntx_parasite_treatment"
	);
	const disease_prevalence_cntx = document.querySelector(
		"#cntx_disease_prevalence"
	);
	drawChart(
		parasite_treatment_cntx,
		treatment_label,
		treatment_count,
		"doughnut",
		"# by type",
		{}
	);
	drawChart(
		disease_prevalence_cntx,
		disease_names,
		disease_count,
		"doughnut",
		"Disease Prevalence",
		{
			plugins:{
				legend:{
					display:false,
				},
			},	
		},
	);
};
getSummary();
drawChart = (canvas, labels, data, type, chart_label,options) => {
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
		options: options,
	});
};
