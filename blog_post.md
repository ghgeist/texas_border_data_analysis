<p align="center">
  <img width="400" height="400" src="https://github.com/ghgeist/texas_border_data_analysis/assets/22363767/a05d4b89-346d-40b6-aa02-aa60f538b11e">
</p>

# Trouble in Texas: Insights from the Texas Department of Public Safety’s Border Report

# Introduction
Inspired by ProPublica’s [investigation](https://www.propublica.org/article/texas-governor-brags-about-his-border-initiative-the-data-doesnt-back-him-up) into the U.S./Mexico border crisis and controversies around Operation Lone Star, I decided to take a look at the Texas Department of Public Safety's (TDPS) Border Report [data](https://txucr.nibrs.com/Report/BorderReport) for the last six years, and answer the following questions:

  - How accessible is the data?
  - How complete is the data?
  - What can I understand about the border crisis given the trends in the data?

# Background
Prior to 2023, crime reporting in Texas was _voluntary_. It was only in 2023 that the Texas Legislature mandated that local law enforcement agencies implement an incident-based reporting system and use it to report data and statistics to the Unified Crime Reporting (UCR) program[^1]. Currently, TDPS is transitioning between the FBI's legacy UCR, Summary Reporting System (SRS), to the new National Incident-Based Reporting System (NIBRS). The best way to understand the difference between the two reporting methods is that SRS typically aggregates crime data into broad categories and totals while records detailed information about each individual crime incident (i.e. characteristics of victims and offenders, location and time of the incident, weapons used, and relationship between victim and offender). Despite the additional details in the NIBRS, the reports _do not_ contain any information about the immigration status of either the victims or offenders, and although NIBRS has been approved for general use since March 1988 [^2], only 73% of the U.S.'s law enforcement agencies are participating as of the third quarter in 2023[^3].

# The Data
The report covers 85 law enforcement agencies, 6 law enforcement agency types 14 counties and 11 NIBRS crime types.

![image](https://github.com/ghgeist/texas_border_data_analysis/assets/22363767/6c896ad8-3317-4b37-a097-ca0cd4207bda)


In 2023, there were approximately 2.6 million people living in the border counties. On average over the last six years, the population decreased by -4.65%, but Hidalgo (McAllen), El Paso (El Paso) and Starr County are growing:
| County         |   Latest Population |   Numerical Change |   Percent Change |
|:---------------|--------------------:|-------------------:|-----------------:|
| Hidalgo County |              888,934 |              33,597 |             3.93 |
| El Paso County |              875,027 |              32,122 |             3.81 |
| Starr County   |               66,662 |               2,102 |             3.26 |

El Paso and McAllen are both critical border towns, and the growth in Starr County appears to be due to its lower housing costs and proximity to McAllen.

# Results
## Data Accessibility
Data from TDPS is hard to access and comprehend. Searching 'texas crime data' on Google will generate [Crime in Texas | Department of Public Safety](https://www.dps.texas.gov/section/crime-records/crime-texas) as the first link, but as of February 14, 2024, the most recent report is a 64 page PDF from 2022 that is difficult to read due to its preference for tables over graphs. The fourth result for 'texas crime data' will lead to the TDPS's Uniform Crime Reporting System (UCRS) [website](https://txucr.nibrs.com/Home/Index), but data can only be accessed via the 'Reports' option. Here users will find an option under 'Texas Reports' to download the 'Border Report' by year, but may have issues with the SQL server timing out. The data is only provided as a .xlsx file, and either programming or advanced Excel skills are required to combine the yearly reports into a usable format. 

## Data Completeness
In 2021, the FBI stopped accepting SRS data and only accepted NIBRS data in order to fully modernize its crime reporting system[^4]. Based upon the reported NIBRS start dates in the TDPS border reports, 88.23% of law enforcement agencies in the border counties had either transitioned or were in the process of transition in 2021, but it seems like the remaining agencies are still struggling to submit data.
| Adoption Status   |   Count of Agencies |   Percent of Agencies |   Avg. NIBRS Contribution Percentage |
|:------------------|--------------------:|-------------------------:|------------------------------------:|
| early             |                  47 |                    55.29 |                               83.72 |
| on time           |                  28 |                    32.94 |                               90.24 |
| late              |                  10 |                    11.76 |                               43.16 |

As a result, the overall data completeness for the entire dataset is 49.31 %, and only two agencies (Roma PD and San Juan PD) submitted data for every month between 2017 and 2023. 

## Trend Analysis
Given the NIBRS data completeness issues, I normalized the data by adjusting the crime counts on the weighted contribution of active agencies reporting the crimes per year. This makes the data comparable across years regardless of the number of reporting agencies or their reporting intensity. 

![normalized_crime_trends](https://github.com/ghgeist/texas_border_data_analysis/assets/22363767/bf4b1ca3-07a6-45ad-a2c1-894582cf2027)

From this graph, we can see that larency-theft and assault are the two most commonly record crimes. However, it seems that the border counties are rarely reporting human trafficking:
| report_year   |   eligible_agencies |   Human Trafficking Commercial Sex Acts |   Human Trafficking Involuntary Servitude |
|:--------------|--------------------:|----------------------------------------:|------------------------------------------:|
| 2017          |                   7 |                                       0 |                                         0 |
| 2018          |                  18 |                                       1 |                                         0 |
| 2019          |                  32 |                                       6 |                                        51 |
| 2020          |                  47 |                                       3 |                                        21 |
| 2021          |                  75 |                                       4 |                                        64 |
| 2022          |                  79 |                                      11 |                                       103 |
| 2023          |                  85 |                                      12 |                                        71 |
| **Total**     |                     |                                  **37** |                                    **310**| 

In six years, there has only been 37 reports of human trafficking-commerical sex acts and 310 reports of human trafficking-involuntary servitude. These numbers likely misrepresent the reality considering the severity of human trafficking on the US-Mexico border. Both large criminal organizations and smaller local groups target migrants for commercial sexual or labor exploitation[^5].

# Conclusion and Recommendations
Given the inaccessibility and incompleteness of the TDPS's border report data, it is difficult to draw any conclusions about the border crisis. In addition, subject matter expertise is required to understand what the different crime types represent, and how they may or may not be indicative of the current situation on the boarder. To make this data more accessible to the public, TDPS should provide clear documentation on what the report is designed to do as well as a data dictionary.

# Future Directions
* Scrape news sources for allegations of corruption and incompetence within the various law enforcement agencies on the border
* Understand the resources and funding for the various law enforcement agencies on the border

# Footnotes
[^1]: [TDPS Uniform Crime Reporting Program Overview](https://www.dps.texas.gov/section/crime-records/uniform-crime-reporting-program-ucr-overview)
[^2]: [FBI Unified Crime Reporting FAQs](https://www2.fbi.gov/ucr/faqs.htm)
[^3]: [FBI Crime Data Explorer](https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/explorer/crime/quarterly).
[^4]: [The Marshall Project: 4 Reasons We Should Worry About Missing Crime Data](https://www.themarshallproject.org/2023/07/13/fbi-crime-rates-data-gap-nibrs)
[^5]: [Insight Crime: The Geography of Human Trafficking on the US-Mexico Border](https://insightcrime.org/wp-content/uploads/2023/08/HGBF-Geography-of-Human-Trafficking-on-the-US-Mexico-Border-InSight-Crime-Aug-2023-FINAL.pdf)