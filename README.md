# Sustainability Analytics
### [Link to Presentation](/sites/other/SUA_Team_5_presentation.pdf)
## Report - Sustainable Ski Resorts - Arosa & Meiringen / Hasliberg
### 1. Introduction to the topic
During recent times, everyone can feel the impact of global warming on the planet and our everyday lifes. Although western societies are privileged in terms of their capacities and resources to take measures against global warming, they are also highly responsible to do so- mainly, because they emitted a large portion of the artificially released atmospheric greenhouse gases, both in the past and today. According to Lenzen et al. (2018) global tourism is the source of about 8% of human-made CO<sub>2</sub> emissions, with growing tendency. Although the share of alpine tourism to that number is not fully clear, it is one of the main touristic branches in Switzerland and therefore offers potential for our society to have an impact on global emission reduction. Furthermore, it has an impact on regional biodiversity, energy consumption, noise pollution, water usage as well as contamination levels of soil and ground. At the same time, tourism is one of the main sources of income for many people, also in Switzerland.
For this reason, the Arosa and Meiringen / Hasliberg Ski Resorts have kindly asked us to support with data generation and analysis in order to take and control measures, understand correlations and steer investments towards a more sustainable and future-oriented vision of recreational alpine areas, with  minimized environmental impact and maximized economical and societal benefit.

This report summarizes the first iteration of the project, which includes a presentation about the general settings and the framework of the project, applied methods for a structural analysis of stakeholders and context, gathered data about snow fall, temperature and overnight stays in the analyzed regions as well as the presentation of the Dashboard MVP with initial results of the visual data analysis and as a last step, limitations and next steps to be taken.

#### 1.1. SDGs
When it comes to sustainability, the overarching framework all measures should be oriented on are the 17 Sustainable Development Goals (SDGs) defined by the UN. This Framework of development goals was finally accepted by all member-countries of the UN in 2015 and acts as a blueprint for peace and prosperity for people and the planet. The 17 goals consist of 169 targets, which all ratifying countries should aim for until 2030. 
In the context of this project, we also want to orientate on the SDGs and identified several of them as strongly interconnected with the alpine recreational context, which are the following:
<br>

- **Goal 13: Climate Action**
- **Goal 9:  Industry, Innovation and Infrastructure**
- **Goal 12: Responsible Consumption and Production**
- **Goal 15: Life on Land**
<br>

**Climate Action**
<br>
Climate Action is one of the main topics of sustainable development. The topic summarizes everything in the context of environmental protection and global warming, one of the biggest challenges of humanity ever. This man-made problem needs to be solved and taken seriously, which is also our responsibility and overarching thread of this project.

**Industry, Innovation and Infrastructure**
<br>
Since changing the status quo and solving challenges with smart solutions asks for innovative ideas and products, this SDG is also clearly part of the path to sustainable alpine tourism. Impact can be generated through both innovative ideas and approaches to tourism and it's future form in general, but also with efficient and sophisticated solutions that minimize environmental impact through efficiency and indulgent utilization of resources. 

**Responsible Consumption and Production**
<br>
Tourism is one form of consumption, that most people in our modern society conduct. As stated above, about 8% of the global emission are routed here. Offering sustainable products, both physical and emotional, combined with a responsible consumption and use of recreational opportunities leads to an overall more sustainable future.

**Life on Land**
<br>
Alpine regions and ski resorts are situated around mountains, in this case within the alps. This region largely defines the swiss geography and landscape, offers immense economical and touristic value while also serving as home to great numbers of individual species and biodiversity. Maintaining this balance of interests, which means both protecting the home of an abundance of animals and plants, while also allowing residents and society to enjoy and utilize the great potential of mountainous regions. This balance is crucial for sustainability within alpine regions and in the interest of all.

#### 1.2. Sustainability trends
This project will touch on some sustainability trends. On the one hand, there is the global trend to reduce greenhouse gas emission in order to mitigate climate change. On the other hand there is ESG Investing that promotes sustainability through business. Ski resorts are strongly affected by both trends, as they rely on a lot of energy to operate the chairlifts and produce artificial snow, especially in winter. Moreover, it is important for the whole region to find investors. As ESG investing becomes more and more important, innovative solutions that combine sustainability and business success are needed ([source](https://explodingtopics.com/blog/sustainability-trends)).

### 2. Methods
#### 2.1. Stakeholder Analysis
The overall framework of the project also includes a variety of stakeholders with different interests and goals. To picture the different groups, we created a Stakeholder-map:
<br>

![Stakeholders](sites/images/Stakeholder_Map.png)

The map is split into three overall categories: **direct, indirect and unintended Stakeholders**. These groups are then again split into three categories of their relationship towards the project: **accountable, to be consulted and to be informed**. The most important, direct Stakeholders are the two resorts themselves, Arosa & Meiringen / Hasliberg. They are the initiators of the project, steer important decisions and will employ potential future solutions. Other important stakeholders are tourists and guests that visit the resorts in both summer and winter as well as local businesses, that are dependent on those guests in combination with what the resorts can offer. Next to that, wildlife, environmental organizations and society in general are also affected and should clearly be taken into account when designing potential future solutions.
<br>

#### 2.2. System Dynamics
As a continuation of the stakeholder analysis, the relationships between the various stakeholders can be modeled. In this report, we have created a system model to show the impact of snow shortage on the economic success of a region. Affected stakeholders and processes in the social, industrial, and environmental sectors have been considered. In the model the input and output variable is colored orange, the positive nodes are colored green, the negative nodes are colored red and the neutral nodes are colored purple.
<br>
Under the following link the simulation can be started: [Loopy](https://ncase.me/loopy/v1.1/?data=[[[1,1073,68,0.5,%22Snow%2520Machines%22,5],[2,913,288,0.5,%22Snow%2520Shortage%22,1],[3,653,246,0.16,%22Water%2520Consumption%22,0],[4,1353,516,0.5,%22Flora%2520Growth%22,3],[5,1453,232,0.16,%22Acidic%2520Soil%22,0],[6,1283,297,0.16,%22Noise%2520Pollution%22,0],[7,907,502,0.5,%22Healthy%2520Wildlife%2520%252F%2520Nature%22,3],[8,573,517,0.5,%22Tourism%22,5],[9,217,770,0.5,%22Investors%22,5],[10,612,745,0.5,%22Local%2520Employment%22,3],[11,896,710,0.5,%22Economoc%2520Success%22,1],[12,524,146,0.16,%22Energy%2520Consumption%22,0],[13,304,389,0.16,%22Financial%2520Cost%22,0]],[[1,3,34,1,0],[1,6,-25,1,0],[2,1,49,1,0],[1,2,26,-1,0],[1,5,51,1,0],[5,4,33,-1,0],[4,7,127,1,0],[6,7,22,-1,0],[3,7,-102,-1,0],[7,8,59,1,0],[8,9,22,1,0],[9,10,37,1,0],[10,11,-34,1,0],[2,8,-21,-1,0],[1,12,43,1,0],[12,13,-296,1,0],[3,13,-310,1,0],[13,9,-78,-1,0],[9,8,362,1,0],[8,6,19,1,0]],[[1478,696,%22Orange%253A%2520Input%2520and%2520Output%2520Variable%250AGreen%253A%2520Positive%2520Variable%250ARed%253A%2520Negative%2520Variable%250APurple%253A%2520Neutral%2520Variable%22],[1015,300,%22Input%22],[1026,719,%22Output%22]],13%5D)
<br>
![Loopy](sites/output/loopy_system_dynamics.png)
<br>

### 3. Data
#### 3.1. Snow Days
For our analysis, we opted for the amount of snow that is comparable between regions. Therefore, we needed the same measurement for each region. The biggest database of meteorological comes from [MeteoSchweiz](https://www.meteoschweiz.admin.ch/home/messwerte.html?param=messwerte-lufttemperatur-10min), which hosts a special portal to make the data available to researcher and students alike called [IDAWEB](https://gate.meteoswiss.ch/idaweb/login.do;idaweb=84I8px26Yhs5I0nAJIGHDEPXlb8Fh0jtmQZqOLbk_O_GD2F937Is!850991741). Luckily, the ordered access was processed within 2 hours and we had a vast amount of data to look into.

We found comparable data with the measurement "Air temperature 2 m above ground; daily minimum".

#### 3.2. Temperature
Temperature data was extracted from the dataportal of MeteoSwiss, the swiss federal office for meteorology and climatology. Through the [IDAWEB](https://gate.meteoswiss.ch/idaweb/login.do;idaweb=84I8px26Yhs5I0nAJIGHDEPXlb8Fh0jtmQZqOLbk_O_GD2F937Is!850991741) portal data can be accessed, filtered and downloaded. The  data on temperature used for the first stage of the analysis consists of measures of the minimum temperature on any given day measured two meters above ground, from the year 1950 until the end of 2021 in Arosa and 1958 until the end of 2021 in Meiringen / Hasliberg. The reason for using the daily minimum temperature instead of the daily average or any other available measure, lies in the future potential to use the downloaded data to estimate potential for the use of snow cannons on the given days. 

#### 3.3. Overnight Stays
For overnight stays, data was drawn from the [STAT-TAB](https://www.bfs.admin.ch/bfs/en/home/services/recherche/stat-tab-online-data-search.html) of the Federal Statistical Office.
This tool was used to download the number of overnight stays in Arosa and Meiringen on a monthly basis between 2013 and 2022.
For the analysis, the data from Meiringen and Hasliberg was added together, as it is a combined ski region.
First, a time series was formed, which was broken down into trend, seasonality and noise.
Furthermore, an additional "season" variable was created. This shows whether a month is a winter or summer month. May to October is defined as summer and November to April as winter.
For each season, the trend between 2013 and 2019 was analyzed. The years affected by the corona pandemic were intentionally omitted because they are highly divergent due to external influences. 

### 4. Results
#### 4.1 Snow Days
In order to analyse the snow factor for tourisitc regions like Meiringen and Arosa, we are not particullarly interested in the total amount of snow, but rather the count of days, on which winter sports are possible. In general, winter sports is possible from 40 cm of natural snow and 20 cm of technical snow onwards ([source](https://www.slf.ch/de/schnee/schneesport/schnee-und-ressourcenmanagement/pistenpraeparation.html)).
The data dates back to 1950 for Arosa and 1960 for Meiringen. The data for Arosa was quite incomplete and offered much fewer data points in summer. We used interpolation for missing values to counter this behaviour.
<br>
![Count of Snow Days Arosa](sites/output/Count%20of%20Snow%20Days%20in%20Arosa.png)
<br>
![Count of Snow Days Meiringen](sites/output/Count%20of%20Snow%20Days%20in%20Meiringen.png)
<br>
Looking at the graphs, it is clear that a regression analyses was obsolete since there seems to be a heavy change in behaviour at around 1980 for both Arosa and Meiringen. Therefore, regression and time-series analysis are off the table and would not add additional insight.
The count of snow days in both locations are decreasing substantially since 1980. Possible explanations for this behaviour will be discussed and analysed in the coming sections. (Remo)

#### 4.2. Temperature
The Analysis of the temperature was conducted through an aggregation as a mean of all temperature measurements within any given year. The resulting datapoints were then plotted and visually analyzed for obvious patterns. 

**Arosa**

![Arosa_Temperature](sites/output/a_yearly_mean_temp.png)

The data on temperature in Arosa shows a very clear upwards-trend in the last decades. This trend is seems very strong and almost linear in a long term view. Average yearly minimum temperature has increased from about -1.4??C in 1950 to about 1.4??C degrees in 2021. 
<br>

**Meiringen/Hasliberg**
![Arosa_Temperature](sites/output/m_yearly_mean_temp.png)
<br>

The data on temperature in Meiringen draws a different picture than in Arosa. Although a slight temperature increase from a yearly minimum average of about 4.2??C to about 4.3??C is visible, there is no clear upwards trend but rather a constant development of the temperature observable over the years. The underlying reasons for this behaviour are not clear at this point of time and require further investigation in the future.
<br>

#### 4.3. Overnight Stays
For overnight stays there is a strong seasonality with peaks during the summer and winter vacation season. Also, the consequences of the Corona pandemic can be analyzed in 2020, 2021 and 2022. For the tourism industry, this pandemic was a black swan event, which had a disproportionate role and was hard-to-predict.
Some initial data from Switzerland as a whole has shown that overnight stays by foreign tourists have decreased by 56% in 2020 ([source](https://www.swissinfo.ch/eng/business/data-shows-dramatic-impact-of-covid-on-swiss-tourism/46741986)).

**Arosa**
<br>
In the winter vacation season overnight stays were historically around 80,000, while in the summer holiday season they were around 50,000. In the off-season in spring and fall, the overnight stays decrease very strongly and are close to zero.
<br><br>
![Arosa_Decomp](sites/output/a_overnight_decomp.png)
<br>
Looking at the two seasons from 2013 to 2019, one can see a very consistent trend in summer, while winter overnight stays are slightly decreasing. In addition, it is visually apparent that the ratio of the summer trend is not linear and one could take a different trend line.
<br>

Summer             |  Winter
:-------------------------:|:-------------------------:
![Arosa_Summer](sites/output/a_overnight_s_trend.png)  |  ![Arosa_Winter](sites/output/a_overnight_w_trend.png)
<br>

**Meiringen/Hasliberg**
<br>
In Meiringen and Hasliberg the summer and winter season have peaks around 22,250 overnight stays a month. Because summer season is slightly longer, there are more overnight stays in this period. In addition, there is a difference between spring and autumn in this region. In spring there are significantly higher numbers of overnight stays than in autumn, which can also be seen in the seasonal component.
<br><br>
![Meiringen_Decomp](sites/output/m_overnight_decomp.png)
<br>
Looking at the two seasons from 2013 to 2019, one can see a very consistent trend in winter, while summer overnight stays are slightly decreasing.
<br>

Summer             |  Winter
:-------------------------:|:-------------------------:
![Meiringen_Summer](sites/output/m_overnight_s_trend.png)  |  ![Meiringen_Winter](sites/output/m_overnight_w_trend.png)


### 5. Conclusion
#### 5.1. Outlook
Our analysis shows a clear trend towards less snow days in the touristic regions Arosa and Meiringen. When we consider the fact that the temperature behaves differently in Arosa and Meiringen, we rule out the temperature as a direct cause for this rapid decrease in snow days since 1980. There might still be indirect effects caused by the rise of average temperature on a global scale.
<br><br>
Thus, future research should focus on other direct factors that might reduce the total count of snowdays such as the frequency and moisture level of the southwind in december. Another direct effect can potentially be found in volcanic eruptions in 1980 ([source](https://www.sciencedaily.com/releases/2015/11/151124081517.htm)).
<br><br>
Nethertheless, the tourisitc regions are facing less snow days each year and should therefore build resilience for such weather conditions. The expansion of touristic activities in summer is therefore advised to keep these destinations attractive for tourists and with that keep local businesses that depend on the tourisitc regions attractiveness.
<br><br>
Furthermore, the need for snow canons will naturally increase, which is very energy and resource intensive. Energy prices are expected to rise, which is why we believe that winter tourism is going to be less profitable and also less environmental.

#### 5.2. Limitations
With the work presented we visualize the trends which affect the touristic regions Meiringen and Arosa. These insights are very useful for investors and are beneficial for the SDGs. However, there are other measurements which should be considered instead of the daily minimum of temperature. For example, the daily average will possibly yeald more accurate results in the analysis. Furthermore, this study does not include any indirect and direct effects of historical changes in wind directions.

#### 5.3. Reflection/Learnings
This report was very insightful and important to us. We understand, that in order to change the world for the better, it is not only wishful-thinking that helps us out of the climat crisis but rather improving complex systems. For this reason, we also focused on the role of the investors in this complex system and show them not only economic reasons, but also environmental reasons not to invest in technical snow and resource hungry assets.
We learned, that complex systems need to be assesed very carefully before making reccomendations. Furthermore, data is not always in good shape, even if it is collected by an official, trustworthy institution like MeteoSchweiz. Improving data quality of susch vast amounts of data is a challenge in itself.

## Appendix
### Short introduction to Git:

**Init**
```bash
git clone https://github.com/j4yk4y/sustainability_analytics.git
```

**Work mit Git**

- git pull: used to fetch and download content from a remote repository and immediately update the local repository to match that content
- git add "filename.xy": If a file has been changed, you should write this command
- git commit -m "write here what has been changed"
- git push: Gives the command to upload the changes to the main fork

### Instruction to open the Dashboard
First a Virtual Environment (venv) has to be created. Then run the two enclosed commands. 

```bash
pip install -r requirements.txt
```

```python
streamlit run app.py
```
