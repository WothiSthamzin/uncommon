Static Files Documentation
==========================

This file documents the static files used in the Uncommon Store application.

Static files are typically used for CSS, JavaScript, and images that are required by the front-end of the application.

**Directory Structure:**
- **static/**
    - Contains all the static files for the project.

**Contents:**
- **css/**
    - **style.css**: Main stylesheet for the application, responsible for the overall layout and design.

- **js/**
    - **scripts.js**: JavaScript file for handling interactive features and AJAX calls in the application.

- **images/**
    - Contains images used throughout the site, including product images, logos, and icons.

**Usage:**
- All static files are served using Django's static files framework. Make sure to run the `collectstatic` command to gather all static files in the correct location for production.
