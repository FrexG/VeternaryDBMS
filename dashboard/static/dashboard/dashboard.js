console.log("In");
getSummary = async () => {
	let options = {
		method: "GET",
		headers: {
			"X-Requested-With": "XMLHttpRequest",
		},
	};
	let response = await fetch("/dashboard/dashboard_data", options);
	let jsonData = await response.json();

	const kebele_labels = jsonData.kebele_names;
	const kebele_data = jsonData.kebele_count;

	const species_label = jsonData.species_names;
	const species_data = jsonData.species_count;

	const service_label = jsonData.service_names;
	const service_data = jsonData.service_count;

	const disease_label = jsonData.disease_names;
	const disease_data = jsonData.disease_count;

	console.log(jsonData);
	const kebele_cntx = document.querySelector("#cntx_kebele");
	const species_cntx = document.querySelector("#cntx_species");
	const services_cntx = document.querySelector("#cntx_services");
	const disease_cntx = document.querySelector("#cntx_disease");

	drawChart(services_cntx, service_label, service_data, "doughnut", "Services");

	drawChart(
		disease_cntx,
		disease_label,
		disease_data,
		"bar",
		"Disease Prevalence",
		{
			indexAxis: "x",
		}
	);

	drawChart(
		kebele_cntx,
		kebele_labels,
		kebele_data,
		"bar",
		"Kebele Contributions",
		{
			indexAxis: "y",
		}
	);
	drawChart(
		species_cntx,
		species_label,
		species_data,
		"doughnut",
		"Share of Species",
		{}
	);
};
getSummary();
const service_type_cntx = document.querySelector("#cntx_clinical_services");
console.log(service_type_cntx);
if (service_type_cntx != null) {
	getSummary = async () => {
		let options = {
			method: "GET",
			headers: {
				"X-Requested-With": "XMLHttpRequest",
			},
		};
		let response = await fetch("/dashboard/clinical_serive_types", options);
		let jsonData = await response.json();

		const service_label = jsonData.service_types;
		const service_data = jsonData.counts;

		console.log(jsonData);

		drawChart(
			service_type_cntx,
			service_label,
			service_data,
			"doughnut",
			"# by type"
		);
	};
}
drawChart = (canvas, labels, data, type, chart_label, option) => {
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
						"#b30000",
						"#7c1158",
						"#4421af",
						"#1a53ff",
						"#0d88e6",
						"#00b7c7",
						"#5ad45a",
						"#8be04e",
						"#ebdc78",
					],
					borderColor: "rgba(255, 99, 132, 1)",
					borderWidth: 1,
				},
			],
		},
		options: option,
	});
};
