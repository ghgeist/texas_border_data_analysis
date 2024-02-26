Add A.I. generated image here

# To Do
- Figure out how to cite my work

# Trouble in Texas: Insights from the Texas Department of Public Safety’s Border Report

# Project Overview

Inspired by ProPublica’s [investigation](https://www.propublica.org/article/texas-governor-brags-about-his-border-initiative-the-data-doesnt-back-him-up) into the U.S./Mexico border crisis and controversies around Operation Lone Star, I decided to take a look at the Texas Department of Safety's (TDPS) Border Report [data](https://txucr.nibrs.com/Report/BorderReport) for the last six years, and answer the following questions:

  - How accessible is the data?
  - How complete is the data?
  - What are the trends within the data?

# Installation and Setup

## Codes and Resources Used
- **Editor:**  VSCode
- **Python Version:** 3.12.0

## Python Packages Used
- **General Purpose:** os, re, datetime
- **Data Manipulation:** pandas, geopandas, shapely
- **Data Visualization:** seaborn, matplotlib
- **Statistical Analysis:** scipy

# Data

## Source Data
### Technical notes
The TDPS's Border Report data can be found here: https://txucr.nibrs.com/Report/BorderReport. 
The report for each year needs to be downloaded individually. Each report is a .xlsx file with three tabs: By Agency, By Month, By Crime Statistic. For the purpose of this project, I analyzed the 'By Agency' data where there should be 85 law enforcement agencies and 11 crime categories in each report (2017 - 2023). 

### Context
Prior to 2023, crime reporting in Texas was _voluntary_. It was only in 2023 that the Texas Legislature mandated that local law enforcement agencies implement an incident-based reporting system and use it to report data and statistics to the Unified Crime Reporting (UCR) program. Currently, TDPS is transitioning between the FBI's legacy UCR, Summary Reporting System (SRS), to the new National Incident-Based Reporting System (NIBRS) which is more detailed. Although NIBRS has been approved for general use since March 1988 [source](https://www2.fbi.gov/ucr/faqs.htm), only 73% of the U.S.'s law enforcement agencies are participating as of the third quarter in 2023 [source](https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/explorer/crime/quarterly). The Marshall Project did some excellent reporting on the issues and consequences around this transition in July 2023: [link](https://www.themarshallproject.org/2023/07/13/fbi-crime-rates-data-gap-nibrs)

### Summary
There are 85 agencies in the border report covering 14 counties.
<img src="https://github.com/ghgeist/texas_border_data_analysis/assets/22363767/fe0a4b36-cca9-4cd5" alt="image" width="300" height="200">


## Data Preprocessing
- [01_consolidate_and_check_data](https://github.com/ghgeist/texas_border_data_analysis/blob/main/notebooks/01_consolidate_and_check_data.ipynb)
  - Combines the yearly reports (2017 - 2023)
  - Checks to make sure the agencies and crime categories are the same across each report
- [02_enrich_dataset.ipynb](https://github.com/ghgeist/texas_border_data_analysis/blob/main/notebooks/02_enrich_dataset.ipynb)
  - Identifies which agencies cover community colleges or universities
  - Calculates NIBRS contribution percentage per agency and report, adjusting for the eligible time period 

# Results
## Data Accessibility
Data from TDPS is hard to access and comprehend. Searching 'texas crime data' on Google will generate [Crime in Texas | Department of Public Safety](https://www.dps.texas.gov/section/crime-records/crime-texas) as the first link, but as of February 14, 2024, the most recent report is a 64 page PDF from 2022 that is difficult to read due to its preference for tables over graphs. The fourth result for 'texas crime data' will lead to the TDPS's Uniform Crime Reporting System (UCRS) [website](https://txucr.nibrs.com/Home/Index), but data can only be accessed via the 'Reports' option. Here users will find an option under 'Texas Reports' to download the 'Border Report' by year, but may have issues with the SQL server timing out. The data is only provided as a .xlsx file, and either programming or advance Excel skills are required to combine the yearly reports into a usuable format. 

## Data Completeness

TO DO -> Talk about NIBRS contributions here

## Trend Analysis

# Future work
Outline potential future work that can be done to extend the project or improve its functionality. This will help others understand the scope of your project and identify areas where they can contribute.


# License
[MIT License](https://opensource.org/license/mit/).
