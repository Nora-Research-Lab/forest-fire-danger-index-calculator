![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Forest Fire Danger Index Calculator
 
*For land managers and fire risk analysts: enter temperature, humidity, wind speed, and drought factor to instantly compute the McArthur Forest Fire Danger Index and fire danger class.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Natural Resources & Land Management
 
The user provides four numeric inputs: Temperature ( -10 to 50°C ), Relative Humidity (0–100%), Wind Speed (0–200 km/h), and Drought Factor (0–10, dimensionless). All inputs are validated and accompanied by sliders for easy adjustment. The core calculation applies the standard McArthur Forest Fire Danger Index (FFDI) formula: FFDI = 2.0 * exp( -0.45 + 0.987 * ln(DF) - 0.0345 * RH + 0.0338 * T + 0.0234 * W ), where DF = drought factor, RH = relative humidity, T = temperature, W = wind speed. If DF == 0, a small epsilon (1e-6) is used to avoid log(0). The result is displayed as a numeric value rounded to 2 decimals and classified according to the Australian fire danger rating system: Low (0–11), Moderate (12–23), High (24–49), Very High (50–99), Extreme (≥100). The classification is shown with a color-coded badge (green, yellow, orange, red, dark red). The Gradio UI consists of a title, four labeled input fields with sliders (or number boxes), a 'Calculate Fire Danger' button, and two output elements: a number box for FFDI and a text label for classification. A small horizontal progress bar or gauge could optionally visualise the index relative to the thresholds. No AI/ML is used — only a deterministic empirical equation. The tool is intended for quick field assessments and planning purposes.
 
## Run it
 
```bash
docker build -t forest-fire-danger-index-calculator .
docker run -p 7860:7860 forest-fire-danger-index-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-27.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
