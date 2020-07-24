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

Luckily, there is a healthy trove of public information available to explore this information:

- **Texas Railroad Commission:**
  - [Natural Gas Production Data](https://rrc.texas.gov/oil-gas/research-and-statistics/production-data/historical-production-data/natural-gas-production-and-well-counts-since-1935/)
  - [Oil Production Data](https://rrc.texas.gov/oil-gas/research-and-statistics/production-data/historical-production-data/crude-oil-production-and-well-counts-since-1935/)
  - [TRRC Commissioner Report](https://rrc.texas.gov/media/56420/sitton-texas-flaring-report-q1-2020.pdf)
  
- **U.S. Energy Information:**
  - [Summary Statistics for Natural Gas - Texas](https://www.eia.gov/dnav/ng/ng_sum_lsum_dcu_STX_a.htm)
  - [Well Locations, Plant Locations, Volumes](https://www.eia.gov/beta/states/states/tx/data/dashboard/natural-gas)
 

  # Strategy
  1. Scrape as much information possible for multple publically available sources.
  2. Establish pipeline of clean, usable data.
  3. Generate visual representations that make the scale of the energy waste clear. Examples of questions I hope to answer:
    - Exactly how much energy have we wasted? How does this compare to historical oil / gas production and consumption?
    - What is the scale of waste in terms of other potential uses?
    - What are the economics driving the decision to flare? 
    - What does the flare volume look like going forward and what ways is this issue being solved?
  4. Leverage hypothesis testing methods to demonstrate ability to apply lessons to real problems. 

