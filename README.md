# Nutri-Ant

A minimal, fullstack webapp that helps users identify the most healthy options to eat at either Brandywine or the Anteatery

![GitHub Repo stars](https://img.shields.io/github/stars/elcosas/Nutri-Ant)
![GitHub forks](https://img.shields.io/github/forks/elcosas/Nutri-Ant)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/elcosas/Nutri-Ant)
![Vercel](https://vercelbadge.vercel.app/api/elcosas/Nutri-Ant)

**Link**: [nutri-ant.vercel.app](https://nutri-ant.vercel.app/)

## Description

The app makes use of the Zotmeal API to query menu data on a Flask-built backend based on user input. 
The app then calculates the bmr and dri levels given the users age, sex, height, and weight, finally returning 
a sorted list of menu items that most efficiently helps with reaching one's daily macro-nutrient goals.

## Usage

The project can be installed using git via:
```bash
git clone https://github.com/elcosas/Nutri-Ant.git
```
Then running either `setup.sh` (Unix) or `setup.bat` (Windows):
```bash
./setup.sh
```
```powershell
setup.bat
```
Then finally running the main app:
```bash
python api/index.py
```

## Sources

backend data: [EricPedley/zotmeal-backend](https://github.com/EricPedley/zotmeal-backend)
\
\
DRI information:
- [https://www.nal.usda.gov/human-nutrition-and-food-safety/dri-calculator](https://www.nal.usda.gov/human-nutrition-and-food-safety/dri-calculator)
- [https://www.omnicalculator.com/health/dri](https://www.omnicalculator.com/health/dri)
- [https://ods.od.nih.gov/HealthInformation/nutrientrecommendations.aspx](https://ods.od.nih.gov/HealthInformation/nutrientrecommendations.aspx)
