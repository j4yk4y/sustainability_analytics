library(stats)
library(tseries)
library(astsa)
library(forecast)
library(dplyr)
library(magrittr)
library(lubridate)
library(tidyr)
library(imputeTS)
library(tidyverse)
library(ggfortify)

# Read-in and preparation
# data_A = Arosa            temperature
# data_M = Meiringen        temperature & snow

data_A <- read.csv("temperatur_arosa_tagesminimum_1950/order_105752_data.csv", header = TRUE, sep = ";")
#data_M <- read.csv("order105773/order_105773_data.txt", header = TRUE, sep = ";")

#PRE-ANALYSIS AROSA
str(data_A)
head(data_A)

colnames(data_A) <- c("Station", "Date", "Temperature")
data_A$Date <- as.Date(format(data_A$Date), "%Y%m%d")
data_A$Temperature <- as.numeric(data_A$Temperature)
data_A <- data_A %>% 
  select("Date", "Temperature")
data_A <- na_interpolation(data_A)
#data_A <- as.matrix(data_A)

summary(data_A$Temperature) #10202 NAs in Temperature


freq_daily <- 365.2422
ts_A <- ts(data_A$Temperature, start=c(year(min(data_A$Date)),yday(min(data_A$Date))), frequency=freq_daily)
ts_A <- na_interpolation(ts_A)

str(ts_A)
head(ts_A)

#write.csv("ts_A", "Arosa_TS.csv")

plot(ts_A)

data_A_yearly <- data_A %>% 
  mutate(year = format(Date, "%Y")) %>%
  select(-Date) %>% 
  group_by(year) %>% 
  summarise(mean = mean(Temperature, na.rm = TRUE))

head(data_A_yearly)

ggplot(data_A_yearly, mapping = aes(x = year, y = mean, group = 1)) +
  geom_line() +
  geom_smooth(method="lm") +
    #scale_y_discrete(limits = c(0, 7)) +
    #scale_x_discrete(limits = c(1950, 2020)) 
    theme(text = element_text(size=7),
          axis.text.x = element_text(angle=90, hjust=1)) +
    labs(title="Average Yearly Temperature of Arosa",
         x =" ", y = "Average Temperature in C",
         caption ="1878 m a.s.l")


stl(ts_A, s.window = )

# Visuals 

ggplot(data_A, mapping = aes(x = Date, y = Temperature)) +
  geom_boxplot()

ggplot(data_A, mapping = aes(x = Date, y = Temperature)) +
  geom_step()



decompose(ts_A)
acf(ts_A)

colnames(temp_M) <- c("Station", "Date", "Temperature", "SnowAuto", "SnowManual")
temp_M$SnowAuto <- as.numeric(temp_M$SnowAuto)
temp_M$SnowManual <- as.numeric(temp_M$SnowManual)
temp_M$Date <- as.Date(format(temp_M$Date), "%Y%m%d")
temp_M$Temperature <- as.numeric(temp_M$Temperature)

temp_A <- na.omit(temp_A)

# Split Disentis and Meiringen

data_M <- temp_M %>%
  filter(stn == "MER",)

str(data_M)
head(data_M)

table(data_M$SnowManual)

# TS generation



ts_M <- ts(temp_M)



# Subset generation

subset <- temp_A %>%
  filter(Date >= as.Date('1980-01-01') & Date <= as.Date('1910-01-01'))
str(subset)

sub_ts <- ts(subset$Temperature)

ggplot(subset, mapping = aes(x = Date, y = Temperature), Date >"1980") +
  geom_step()

ggplot(subset) +
  aes(x = Date, weight = Temperature) +
  geom_bar()

summer <- temp_A %>%
  filter(Temperature >= 0)
count(summer)

winter <- temp_A %>%
  filter(Temperature <= 0)
count(winter)


# Decomposition

stl(sub_ts)

