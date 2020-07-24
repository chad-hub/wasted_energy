# Created nor Destroyed: An exploratory analysis of energy wasted to flaring natural gas

The goal of this project is to explore and assess the scale of energy flared with publicly available data.  The scale of energy waste will be evaluated based on a normalized ratio, the "Waste Ratio", and I will focus specifically on Texas v. the US.  

# Background and Inspiration

Energy is a passion of mine. It drives the global economy and fuels human advancement. I believe it is vital that we improve existing means of energy generation while also focusing on renewables. If we neglect to continue improving existing means of energy generation, we risk missing out on opportunities to share these improvements globally, espeically in areas that are not able to embrace renewables as quickly as the US.  I am often frustrated by the energy industry's common practice of flaring natural gas - the burning of energy that is otherwise too costly to take to market. Natural gas is plentfiul in the US - the Energy Information Administration (EIA) estimates the total resevres in 2018 at 365 Tcf. Thats 365,000,000,000,000 cubic feet. Its impossible to comprehend that volume. To put that into a more digestable form - from a pure energy standpoint, that volume of gas represents enough energy to supply the entirety of the US energy demand for over 25 years. This gas is usually very difficult and costly to bring to market, even in areas where the infrastructure exists to do so. As we push the bounds of production into areas that do not have infrastructure to bring all produced gas to the market, the only economical solution is to flare off the gas. There are definite environmental concerns with flaring...it releases mass quantities of CO2, but becuase the ultimate fate of natural gas is to be burned somewhere, I decided to focus on flaring as a waste issue rather than environmental. 


Now that I am empowered with the tools and knowledge to explore and test the data, I take a  dive into the data available and visualize the scale of the waste. 

# Hypothesis
I decided to focus on Texas' energy waste vs. the overall waste in the US becuase Texas is, by a wide margin, the state that produces the most energy from hydrocarbons. 

![topstatespic](/plots/top_states.png)


Another driving factor for me is that Texas is the second largest state, and the productive reservoirs are spread across a wide swath of land in West Texas - many of these areas very remote with little or no infrastructure in place to bring the natural gas to market. 
  * Ho : The mean waste ratio for Texas is equivalent to that of the rest of the United States
  * Ha : The mean waste ratio for Texas is not equivalent to that of the rest of the United States
  
This test leveraged the two-tailed Welch's t-test between Texas and the US for reported production and flaring data dating back to 1980. This provided an adequate smaple size for the Central Limit Theorem to hold. Used alpha value of 0.05 as rejection criteria.

# Data

All data for this analysis was scraped from [U.S. Energy Information Administration](https://www.eia.gov/). The site reports every states reported oil and gas production, and the amount of gas vented / flared (wasted). Unfortunately, some states like Pennsylvania, home to massive quantities of natural gas, do not report flaring information. All innformation regarding the production volumes and flare volumes for every available year was scraped via Beautiful Soup and stashed in a MongoDB database. The databases were separated into collections of oil produced, gas produced, and gas flared for each reporting state. The DBs were read into Python Pandas via PyMongo. From there, Pandas allowed me to clean up the data to be used in my EDA. 

# EDA

After the data was merged and cleaned, I began performing some basic EDA forcusing on some of points of interest. I started with looking into the bigger picture, and then diving into testing my hypothesis. 

![total energy](/plots/tot_energy_produced.png)
 
 This plot shows the annual energy production of the US (including Texas) and Texas alone. The units depicted are kWh, combing both natural gas and oil values. Also on the graph is the percentage of energy consumed in the United States that comes from one of those two sources in the same time frame. I wanted to display the percentage from these sources as well because it speaks to why my topic is so important. These products, with all their flaws, still dominate our energy spectrum. As we wane off these goods for greener sources, we need to ensure that we still strive to optimize them. It will take decades to switch to fully renewable sources, and even longer for the developing world. This graph emphasizes this point for me.  
 
![cum_energy_waste](/plots/cum_waste.png)

The above plot shows, quite simply, the scale of the waster we are talking about over the years. Some perspective: 
  * The total amount of energy wasted to flare since 1980 could power 161 million US homes for a year (based on 2019 consumption average) 
  * The total amount of energy wasted to flare in 2018 *alone* could power around 12.5 million homes for a year (based on 2019 consumption average)
  * The same energy wasted in 2018 could power a Tesla journey to the sun and back over 3,000 times. (4.1 miles per kWh Tesla average)

Obviously the examples above don't facotor in the energy lost in converting thermal energy to mechanical and inefficiencies in power systems. I am speaking from a pure energy perspective. 

After getting familiar with the data and observing the large scale energy waste, I turned my attention to testing my Hypothesis. I sliced the data to only include Texas and the rest of the US, normalized the volumes produced / flared with kWh, and created the ratio of energy wasted / energy produced - a unitless value that provides a useful proving ground for how well Texas is utilizing its energy vs. the rest of the country. 

![texas_us_hist](/plots/TX_US_hist.png)


![texas_us_box](/plots/TX_US_box.png)


