import os
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


OPERATING_SYSTEM_OPTIONS = [
	"Windows",
	"Linux",
	"Mac",
]

IDE_OPTIONS = [
	"windsurf",
	"cursor",
]


def is_valid_choice(choice: str, allowed: list[str]) -> bool:
	if choice is None:
		return False
	return choice in allowed


@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		operating_system = request.form.get("operating_system", "").strip()
		ide = request.form.get("ide", "").strip()
		policies = request.form.get("policies", "").strip()

		errors: dict[str, str] = {}
		if not is_valid_choice(operating_system, OPERATING_SYSTEM_OPTIONS):
			errors["operating_system"] = "Please choose Windows, Linux, or Mac."
		if not is_valid_choice(ide, IDE_OPTIONS):
			errors["ide"] = "Please choose windsurf or cursor."
		if not policies:
			errors["policies"] = "Please describe the policy types you need."

		if errors:
			return render_template(
				"index.html",
				operating_system_options=OPERATING_SYSTEM_OPTIONS,
				ide_options=IDE_OPTIONS,
				errors=errors,
				form_data={
					"operating_system": operating_system,
					"ide": ide,
					"policies": policies,
				},
			)

		return render_template(
			"result.html",
			operating_system=operating_system,
			ide=ide,
			policies=policies,
		)

	return render_template(
		"index.html",
		operating_system_options=OPERATING_SYSTEM_OPTIONS,
		ide_options=IDE_OPTIONS,
		errors={},
		form_data={"operating_system": "", "ide": "", "policies": ""},
	)


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port, debug=False)