
function runCheck() {
  const industry = document.getElementById("industry").value;
  const input = document.getElementById("input").value.toLowerCase();
  let result = "";

  const rules = {
    construction: ["helmet", "safety harness", "scaffolding"],
    manufacturing: ["machine guard", "noise protection", "emergency stop"],
    chemical: ["msds", "chemical labels", "ventilation"],
    warehouse: ["forklift training", "spill kit", "fire exit"]
  };

  const keywords = rules[industry];
  let missing = [];

  keywords.forEach(term => {
    if (!input.includes(term)) {
      missing.push(term);
    }
  });

  if (missing.length === 0) {
    result = "✅ All required safety protocols are mentioned. Fully Compliant.";
  } else {
    result = "❌ Non-Compliant. Missing: " + missing.join(", ");
  }

  document.getElementById("result").innerText = result;
}
